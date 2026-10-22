"""Agentic network for software requirements refinement (LangGraph)."""
import argparse
import json
import operator
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Annotated, TypedDict

from dotenv import find_dotenv, load_dotenv
from langgraph.graph import END, START, StateGraph
from langgraph.types import Send
from openai import OpenAI

from extraction import EXTRACTOR_PROMPT, ExtractionResult, build_user_message
from merge import MERGER_PROMPT, MergeResult, apply_merge, build_merge_message, cluster_batches, to_item
from priority import (LEVELS, PRIORITIZER_PROMPT, PriorityResult, baseline, build_priority_message,
                      clamp, signals)
from context import index_documents, retrieve
from elaborate import (NAME_PROMPT, PARAGRAPH_PROMPT, NameResult, ParagraphResult, build_name_message,
                       build_paragraph_message, name_ok, paragraph_ok)
from render import assign_ids as assign_requirement_ids, check_document, render_markdown
from review import REVIEWER_PROMPT, ReviewResult, build_review_message
from textutil import squash, squash_with_positions

TEXT_SUFFIXES = {".txt", ".eml", ".md"}
DEFAULT_MAX_CHUNK_CHARS = 4000
MODELS = {"extract": "gpt-5.6-luna", "review": "gpt-6-luna", "merge": "gpt-6-luna", "prioritize": "gpt-5.4-nano",
          "paragraph": "gpt-5.6-luna", "name": "gpt-5.4-nano"}
MAX_REEXTRACTIONS = 2  # feedback-loop cap
MERGE_BATCH_SIZE = 60  # items per merge call (one topical cluster)
PRIORITY_BATCH_SIZE = 40
PARAGRAPH_BATCH_SIZE = 6   # requirements per paragraph-writer call
NAME_BATCH_SIZE = 40
MERGE_ROUNDS = 2       # round 2 re-clusters the output of round 1 to catch cross-cluster duplicates
MAX_CONCURRENCY = 8  # parallel LLM calls

# Split points, strongest first: separator lines (=== / ---), blank lines, line breaks, spaces.
SPLIT_PATTERNS = [
    re.compile(r"\n[=\-]{3,}[ \t]*\n"),
    re.compile(r"\n[ \t]*\n"),
    re.compile(r"\n"),
    re.compile(r" "),
]


class Document(TypedDict):
    id: str    # path relative to the input directory, used for tracing
    text: str


class Chunk(TypedDict):
    doc_id: str   # Document.id this chunk comes from
    index: int    # 0-based position within the document
    total: int    # number of chunks of the document
    text: str


class Candidate(TypedDict):
    id: str            # C001, ... assigned by code in verify_evidence
    title: str
    description: str
    evidence: str      # verbatim quote
    type: str
    date: str | None
    source_doc: str    # Document.id the candidate was extracted from
    chunk_index: int
    evidence_ok: bool  # True if the quote was found in the source chunk


class State(TypedDict, total=False):
    input_dir: str
    max_chunk_chars: int
    documents: list[Document]
    chunks: list[Chunk]
    # `extract` runs once per chunk in parallel; the reducer (operator.add) concatenates the results.
    raw_candidates: Annotated[list[dict], operator.add]
    candidates: list[Candidate]
    # feedback loop: `iteration` = reviews finished so far; `feedback` maps doc_id -> missing items text
    iteration: int
    reviews: Annotated[list[dict], operator.add]
    feedback: dict[str, str]
    requirements: list[dict]
    blacklist: list[dict]
    output_path: str


def load_corpus(state: State) -> dict:
    """Deterministic node: recursively read all text documents under input_dir."""
    root = Path(state["input_dir"])
    if not root.is_dir():
        raise FileNotFoundError(f"Input directory not found: {root}")
    documents = [
        Document(
            id=path.relative_to(root).as_posix(),
            text=path.read_text(encoding="utf-8", errors="replace"),
        )
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES
    ]
    return {"documents": documents}


def _cut_after(text: str, pattern: re.Pattern) -> list[str]:
    """Cut text after every match of pattern, keeping the separator in the preceding piece."""
    pieces, pos = [], 0
    for match in pattern.finditer(text):
        pieces.append(text[pos:match.end()])
        pos = match.end()
    pieces.append(text[pos:])
    return [piece for piece in pieces if piece]


def split_text(text: str, max_chars: int, level: int = 0) -> list[str]:
    """Split text into chunks of at most max_chars, preferring the strongest boundaries.

    Lossless: "".join(result) == text.
    """
    if len(text) <= max_chars:
        return [text]
    if level == len(SPLIT_PATTERNS):
        return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]
    pieces = _cut_after(text, SPLIT_PATTERNS[level])
    if len(pieces) == 1:
        return split_text(text, max_chars, level + 1)
    chunks, current = [], ""
    for piece in pieces:
        for part in split_text(piece, max_chars, level + 1):
            if current and len(current) + len(part) > max_chars:
                chunks.append(current)
                current = part
            else:
                current += part
    if current:
        chunks.append(current)
    return chunks


def chunk_documents(state: State) -> dict:
    """Deterministic node: split documents into chunks of at most max_chunk_chars."""
    max_chars = state.get("max_chunk_chars", DEFAULT_MAX_CHUNK_CHARS)
    chunks = []
    for doc in state["documents"]:
        parts = split_text(doc["text"], max_chars)
        chunks.extend(
            Chunk(doc_id=doc["id"], index=i, total=len(parts), text=part)
            for i, part in enumerate(parts)
        )
    return {"chunks": chunks}


def fan_out(state: State) -> list[Send]:
    """Conditional edge: one parallel `extract` task per chunk."""
    return [Send("extract", {"chunk": chunk}) for chunk in state["chunks"]]


def fan_out_feedback(state: State) -> list[Send]:
    """Re-extraction round: only chunks of documents the reviewer complained about, with the feedback."""
    return [Send("extract", {"chunk": chunk, "feedback": state["feedback"][chunk["doc_id"]]})
            for chunk in state["chunks"] if chunk["doc_id"] in state["feedback"]]


def fan_out_review(state: State) -> list[Send]:
    """Conditional edge: one parallel review task per document."""
    round_ = state.get("iteration", 0)
    docs = {d["id"]: d for d in state["documents"]}
    return [Send("review_completeness", {
        "doc": doc,
        "candidates": [c for c in state["candidates"] if c["source_doc"] == doc_id],
        "round": round_,
    }) for doc_id, doc in docs.items()]


_client: OpenAI | None = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI()  # reads OPENAI_API_KEY from the environment
    return _client


def extract(task: dict) -> dict:
    """LLM node: extract candidate requirements from one chunk (input is a Send payload, not State)."""
    chunk: Chunk = task["chunk"]
    resp = get_client().chat.completions.parse(
        model=MODELS["extract"],
        messages=[
            {"role": "system", "content": EXTRACTOR_PROMPT},
            {"role": "user", "content": build_user_message(
                chunk["doc_id"], chunk["index"], chunk["total"], chunk["text"],
                task.get("feedback"))},
        ],
        response_format=ExtractionResult,
        max_completion_tokens=16000,
    )
    parsed = resp.choices[0].message.parsed
    requirements = parsed.requirements if parsed else []
    return {"raw_candidates": [
        {**req.model_dump(), "doc_id": chunk["doc_id"], "chunk_index": chunk["index"]}
        for req in requirements
    ]}


def verify_evidence(state: State) -> dict:
    """Deterministic node: check each quote against its chunk, assign candidate ids, add source_doc."""
    chunk_text = {(c["doc_id"], c["index"]): squash(c["text"]) for c in state["chunks"]}
    # parallel extract tasks finish in arbitrary order; sort (stable) so ids are reproducible
    raw = sorted(state["raw_candidates"], key=lambda r: (r["doc_id"], r["chunk_index"]))
    candidates = []
    for n, item in enumerate(raw, start=1):
        quote = squash(item["evidence"])
        candidates.append(Candidate(
            id=f"C{n:03d}",
            title=item["title"],
            description=item["description"],
            evidence=item["evidence"],
            type=item["type"],
            date=item["date"],
            source_doc=item["doc_id"],
            chunk_index=item["chunk_index"],
            evidence_ok=bool(quote) and quote in chunk_text[(item["doc_id"], item["chunk_index"])],
        ))
    return {"candidates": candidates}


def review_completeness(task: dict) -> dict:
    """LLM node: given a document and its candidates, list requirements the extraction missed."""
    doc, candidates = task["doc"], task["candidates"]
    extracted = [f"{c['title']}: {c['description']}" for c in candidates]
    resp = get_client().chat.completions.parse(
        model=MODELS["review"],
        messages=[
            {"role": "system", "content": REVIEWER_PROMPT},
            {"role": "user", "content": build_review_message(doc["id"], doc["text"], extracted)},
        ],
        response_format=ReviewResult,
        max_completion_tokens=16000,
    )
    parsed = resp.choices[0].message.parsed
    text = squash(doc["text"])
    missing = [
        {"description": m.description, "evidence": m.evidence,
         "quote_ok": bool(squash(m.evidence)) and squash(m.evidence) in text}
        for m in (parsed.missing if parsed else [])
    ]
    return {"reviews": [{"doc_id": doc["id"], "round": task["round"], "missing": missing}]}


def review_gate(state: State) -> dict:
    """Deterministic node: join the parallel reviews and decide whether another extraction round runs.

    Reviewer items whose quote is not in the document are ignored (hallucination guard).
    """
    done = state.get("iteration", 0)
    feedback = {}
    for review in state["reviews"]:
        if review["round"] != done:
            continue
        items = [m["description"] for m in review["missing"] if m["quote_ok"]]
        if items:
            feedback[review["doc_id"]] = "\n".join(f"- {item}" for item in items)
    return {"iteration": done + 1, "feedback": feedback if done < MAX_REEXTRACTIONS else {}}


def merge_batch(batch: list[dict]) -> MergeResult:
    """One LLM call: duplicates and conflicts inside one topical cluster."""
    if len(batch) < 2:
        return MergeResult(groups=[], blacklist=[])
    resp = get_client().chat.completions.parse(
        model=MODELS["merge"],
        messages=[
            {"role": "system", "content": MERGER_PROMPT},
            {"role": "user", "content": build_merge_message(batch)},
        ],
        response_format=MergeResult,
        max_completion_tokens=32000,
    )
    parsed = resp.choices[0].message.parsed
    if parsed is None:
        print("  warning: unparsable merge result, batch kept unchanged")
        return MergeResult(groups=[], blacklist=[])
    return parsed


def merge_and_resolve(state: State) -> dict:
    """LLM node: merge duplicates, blacklist conflicting/nonsensical items, unify vocabulary.

    A single call over all ~800 candidates was lazy (many duplicates left), so each round clusters the items
    by topic in code (cluster_batches), calls the model per cluster in parallel and repeats on the output.
    The model returns only decisions; apply_merge builds the records from the original items.
    """
    items = [to_item(c) for c in state["candidates"]]
    blacklist = []
    for rnd in range(1, MERGE_ROUNDS + 1):
        batches = cluster_batches(items, MERGE_BATCH_SIZE)
        with ThreadPoolExecutor(MAX_CONCURRENCY) as pool:
            results = list(pool.map(merge_batch, batches))
        items = []
        for n, (batch, result) in enumerate(zip(batches, results), start=1):
            merged, bl, stats = apply_merge(batch, result, f"M{rnd}.{n}")
            items += merged
            blacklist += bl
        print(f"  round {rnd}: {len(batches)} clusters -> {len(items)} items, {len(blacklist)} blacklist entries")
    requirements = sorted(items, key=lambda r: r["member_ids"][0])
    for r in requirements:
        del r["id"]
    return {"requirements": requirements, "blacklist": blacklist}


def prioritize_batch(batch: list[dict]) -> dict[str, tuple[str, str]]:
    """One nano call: {pid: (level, note)} for a batch of requirements."""
    resp = get_client().chat.completions.parse(
        model=MODELS["prioritize"],
        messages=[
            {"role": "system", "content": PRIORITIZER_PROMPT},
            {"role": "user", "content": build_priority_message(batch)},
        ],
        response_format=PriorityResult,
        max_completion_tokens=8000,
    )
    parsed = resp.choices[0].message.parsed
    return {i.id: (i.priority, i.note) for i in parsed.items} if parsed else {}


def prioritize(state: State) -> dict:
    """LLM node (small model) with code guardrails.

    Code computes signals and a baseline level from them; a stated priority in the source is final. The
    model sees the baseline and may move it by one level; its answer is matched by id, clamped, and any
    missing id falls back to the baseline. Ordering is done later by code, not by the model.
    """
    doc_index = {d["id"]: (*squash_with_positions(d["text"]), d["text"]) for d in state["documents"]}
    work = []
    for n, req in enumerate(state["requirements"], start=1):
        sig = signals(req, doc_index)
        level, basis = baseline(sig)
        work.append({**req, "_pid": f"P{n:03d}", "_base": level, "_basis": basis, "_sig": sig})
    todo = [r for r in work if not r["_sig"]["stated"]]   # stated priorities need no opinion
    batches = [todo[i:i + PRIORITY_BATCH_SIZE] for i in range(0, len(todo), PRIORITY_BATCH_SIZE)]
    with ThreadPoolExecutor(MAX_CONCURRENCY) as pool:
        answers = {k: v for part in pool.map(prioritize_batch, batches) for k, v in part.items()}
    requirements, changed, missing = [], 0, 0
    for r in work:
        proposed, note = answers.get(r["_pid"], (None, ""))
        locked = bool(r["_sig"]["stated"])
        final = clamp(r["_base"], proposed, locked)
        missing += not locked and proposed is None
        changed += final != r["_base"]
        basis = r["_basis"]
        if final != r["_base"]:
            basis += f" Adjusted from {r['_base']} by model: {note}"
        requirements.append({
            **{k: v for k, v in r.items() if not k.startswith("_")},
            "priority": final, "priority_basis": basis,
            "priority_source": "stated" if locked else "signals+model" if final != r["_base"] else "signals",
        })
    counts = {lvl: sum(r["priority"] == lvl for r in requirements) for lvl in LEVELS}
    print(f"  priorities {counts}; model changed {changed}, no answer for {missing}, "
          f"stated in source {sum(r['priority_source'] == 'stated' for r in requirements)}")
    return {"requirements": requirements}


def retrieve_context(state: State) -> dict:
    """Deterministic node: attach source passages to each requirement (quote anchoring, TF-IDF fallback)."""
    docs = index_documents(state["documents"])
    requirements = [{**r, "contexts": retrieve(r, docs)} for r in state["requirements"]]
    via = {k: sum(c["how"] == k for r in requirements for c in r["contexts"]) for k in ("quote", "similarity")}
    print(f"  passages: {via}; requirements without any passage: {sum(not r['contexts'] for r in requirements)}")
    return {"requirements": requirements}


def _batches(items: list[dict], size: int) -> list[list[dict]]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def write_batch(batch: list[dict]) -> dict[str, str]:
    resp = get_client().chat.completions.parse(
        model=MODELS["paragraph"],
        messages=[{"role": "system", "content": PARAGRAPH_PROMPT},
                  {"role": "user", "content": build_paragraph_message(batch)}],
        response_format=ParagraphResult,
        max_completion_tokens=16000,
    )
    parsed = resp.choices[0].message.parsed
    return {i.id: i.paragraph for i in parsed.items} if parsed else {}


def write_paragraphs(state: State) -> dict:
    """LLM node: rewrite each requirement's description as a grounded paragraph from its source passages.

    The model sees only the summary and the retrieved passages, in batches. Code accepts a paragraph only if it
    has a sensible length and contains no number absent from its grounding; otherwise the old description stays.
    """
    work = [{**r, "_pid": f"P{n:03d}"} for n, r in enumerate(state["requirements"], start=1)]
    with ThreadPoolExecutor(MAX_CONCURRENCY) as pool:
        answers = {k: v for part in pool.map(write_batch, _batches(work, PARAGRAPH_BATCH_SIZE))
                   for k, v in part.items()}
    requirements, rejected = [], 0
    for r in work:
        grounding = r["title"] + " " + r["description"] + " " + " ".join(c["text"] for c in r["contexts"])
        paragraph = answers.get(r["_pid"], "")
        ok = paragraph_ok(paragraph, grounding)
        rejected += not ok
        requirements.append({**{k: v for k, v in r.items() if k != "_pid"},
                             "summary": r["description"], "description": paragraph if ok else r["description"],
                             "paragraph_source": "model" if ok else "merge_summary"})
    print(f"  paragraphs written: {len(work) - rejected}, rejected by guard or missing (old text kept): {rejected}")
    return {"requirements": requirements}


def name_batch(batch: list[dict]) -> dict[str, str]:
    resp = get_client().chat.completions.parse(
        model=MODELS["name"],
        messages=[{"role": "system", "content": NAME_PROMPT},
                  {"role": "user", "content": build_name_message(batch)}],
        response_format=NameResult,
        max_completion_tokens=8000,
    )
    parsed = resp.choices[0].message.parsed
    return {i.id: i.name.strip() for i in parsed.items} if parsed else {}


def name_requirements(state: State) -> dict:
    """LLM node (small model): short descriptive name from the final paragraph; the old title is the fallback."""
    work = [{**r, "_pid": f"P{n:03d}"} for n, r in enumerate(state["requirements"], start=1)]
    with ThreadPoolExecutor(MAX_CONCURRENCY) as pool:
        answers = {k: v for part in pool.map(name_batch, _batches(work, NAME_BATCH_SIZE)) for k, v in part.items()}
    requirements, renamed = [], 0
    for r in work:
        name = answers.get(r["_pid"], "")
        ok = name_ok(name)
        renamed += ok and name != r["title"]
        requirements.append({**{k: v for k, v in r.items() if k != "_pid"}, "title": name if ok else r["title"]})
    print(f"  names changed: {renamed} of {len(work)}")
    return {"requirements": requirements}


def assign_ids(state: State) -> dict:
    """Deterministic node: REQ-/BL- ids and final ordering, assigned after dedup and never by a model."""
    requirements, blacklist = assign_requirement_ids(state["requirements"], state["blacklist"])
    return {"requirements": requirements, "blacklist": blacklist}


def render_doc(state: State) -> dict:
    """Deterministic node: write the Markdown document and check it against the output spec."""
    markdown = render_markdown(state["requirements"], state["blacklist"], [d["id"] for d in state["documents"]])
    problems = check_document(markdown, state["requirements"], state["blacklist"])
    if problems:
        raise RuntimeError("Document self-check failed:\n" + "\n".join(problems))
    path = Path(state["output_path"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown, encoding="utf-8")
    print(f"  wrote {path} ({len(markdown) // 1024} kB), self-check passed")
    return {}


# Pipeline order; also the names of the checkpoint files (output/states/NN_<name>.json).
# review_gate may loop back to extract: the loop is wired in build_graph.
STAGES = ["load_corpus", "chunk_documents", "extract", "verify_evidence",
          "review_completeness", "review_gate", "merge_and_resolve", "prioritize",
          "retrieve_context", "write_paragraphs", "name_requirements", "assign_ids", "render_doc"]
NODES = {
    "load_corpus": load_corpus,
    "chunk_documents": chunk_documents,
    "extract": extract,
    "verify_evidence": verify_evidence,
    "review_completeness": review_completeness,
    "review_gate": review_gate,
    "merge_and_resolve": merge_and_resolve,
    "prioritize": prioritize,
    "retrieve_context": retrieve_context,
    "write_paragraphs": write_paragraphs,
    "name_requirements": name_requirements,
    "assign_ids": assign_ids,
    "render_doc": render_doc,
}
FAN_OUT = {"extract": fan_out, "review_completeness": fan_out_review}


def build_graph(start_at: str = STAGES[0], stop_after: str = STAGES[-1]):
    """Compile the graph for the stages start_at..stop_after (lets us resume from a checkpoint)."""
    stages = STAGES[STAGES.index(start_at):STAGES.index(stop_after) + 1]
    looped = "review_gate" in stages  # the feedback loop needs these nodes even when resuming mid-loop
    nodes = set(stages) | ({"extract", "verify_evidence", "review_completeness"} if looped else set())
    graph = StateGraph(State)
    for name in STAGES:
        if name in nodes:
            graph.add_node(name, NODES[name])

    def link(source, target):
        if target in FAN_OUT:
            graph.add_conditional_edges(source, FAN_OUT[target], [target])
        else:
            graph.add_edge(source, target)

    for source, target in zip([START] + stages, stages):
        if source != "review_gate":  # the gate's outgoing edge is conditional (loop or move on), see below
            link(source, target)
    if looped:
        if "extract" not in stages:  # resumed after extract: reachable only through the loop
            graph.add_edge("extract", "verify_evidence")
        if "verify_evidence" not in stages:
            link("verify_evidence", "review_completeness")
        after = stages[stages.index("review_gate") + 1:]
        target = after[0] if after else END

        def route(state: State):
            return fan_out_feedback(state) if state.get("feedback") else target

        graph.add_conditional_edges("review_gate", route, ["extract", target])
    if stages[-1] != "review_gate":  # a gate that is last already routes to END
        graph.add_edge(stages[-1], END)
    return graph.compile()


def snapshot_path(output_dir: Path, stage: str, iteration: int = 0) -> Path:
    """Checkpoint file; later passes of the feedback loop get an .iN suffix so the first pass stays."""
    suffix = f".i{iteration}" if iteration else ""
    return output_dir / "states" / f"{STAGES.index(stage) + 1:02d}_{stage}{suffix}.json"


def save_snapshot(output_dir: Path, stage: str, state: dict) -> None:
    path = snapshot_path(output_dir, stage, state.get("iteration", 0))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")


def load_snapshot(output_dir: Path, stage: str, iteration: int | None = None) -> dict:
    """Load a checkpoint: the given loop pass, or the latest one if iteration is None."""
    if iteration is None:
        iteration = max((i for i in range(MAX_REEXTRACTIONS + 2)
                         if snapshot_path(output_dir, stage, i).exists()), default=0)
    return json.loads(snapshot_path(output_dir, stage, iteration).read_text(encoding="utf-8"))


def summarize(stage: str, state: dict) -> str:
    counts = {k: len(state[k]) for k in ("documents", "chunks", "raw_candidates", "candidates", "requirements", "blacklist") if k in state}
    text = ", ".join(f"{n} {k}" for k, n in counts.items())
    if "candidates" in state:
        text += f" ({sum(not c['evidence_ok'] for c in state['candidates'])} with unverified quote)"
    if state.get("reviews"):
        latest = max(r["round"] for r in state["reviews"])
        missing = [m for r in state["reviews"] if r["round"] == latest for m in r["missing"]]
        text += (f"; review round {latest}: {sum(m['quote_ok'] for m in missing)} missing "
                 f"({len(missing)} reported)")
    return f"[{stage}] {text}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", help="directory with the input corpus")
    parser.add_argument("--max-chunk-chars", type=int, default=DEFAULT_MAX_CHUNK_CHARS,
                        help="maximum size of one chunk in characters")
    parser.add_argument("--output-dir", default="output", help="where checkpoints and the result go")
    parser.add_argument("--start-at", choices=STAGES, default=STAGES[0],
                        help="resume: load the checkpoint of the previous stage and run from this stage")
    parser.add_argument("--snapshot-iteration", type=int, default=None,
                        help="with --start-at: use the checkpoint of this loop pass (default: latest)")
    parser.add_argument("--stop-after", choices=STAGES, default=STAGES[-1],
                        help="stop after this stage")
    args = parser.parse_args()
    load_dotenv(find_dotenv(usecwd=True))
    output_dir = Path(args.output_dir)

    if args.start_at == STAGES[0]:
        state = {"input_dir": args.input_dir, "max_chunk_chars": args.max_chunk_chars}
    else:
        state = load_snapshot(output_dir, STAGES[STAGES.index(args.start_at) - 1], args.snapshot_iteration)

    state["output_path"] = str(output_dir / "requirements.md")
    graph = build_graph(args.start_at, args.stop_after)
    stage = None
    # "updates" tells us which node just ran, "values" gives the full state after the step
    for mode, data in graph.stream(state, {"max_concurrency": MAX_CONCURRENCY},
                                   stream_mode=["updates", "values"]):
        if mode == "updates":
            stage = next(iter(data))
        elif stage:
            save_snapshot(output_dir, stage, data)
            print(summarize(stage, data))
            stage = None


if __name__ == "__main__":
    main()
