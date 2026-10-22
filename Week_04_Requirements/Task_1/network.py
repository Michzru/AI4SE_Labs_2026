"""Agentic network for software requirements refinement (LangGraph)."""
import argparse
import json
import operator
import re
import unicodedata
from pathlib import Path
from typing import Annotated, TypedDict

from dotenv import find_dotenv, load_dotenv
from langgraph.graph import END, START, StateGraph
from langgraph.types import Send
from openai import OpenAI

from extraction import EXTRACTOR_PROMPT, ExtractionResult, build_user_message
from merge import MERGER_PROMPT, MergeResult, apply_merge, build_merge_message
from review import REVIEWER_PROMPT, ReviewResult, build_review_message

TEXT_SUFFIXES = {".txt", ".eml", ".md"}
DEFAULT_MAX_CHUNK_CHARS = 4000
MODELS = {"extract": "gpt-5.6-luna", "review": "gpt-6-luna", "merge": "gpt-6-luna"}
MAX_REEXTRACTIONS = 2  # feedback-loop cap
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


def squash(text: str) -> str:
    """Normalize for quote matching: Unicode-fold, lowercase, keep letters and digits only.

    Makes the check immune to line wrapping, e-mail '>' prefixes, quote styles and dashes.
    """
    text = unicodedata.normalize("NFKC", text).casefold()
    return "".join(ch for ch in text if ch.isalnum())


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


def merge_and_resolve(state: State) -> dict:
    """LLM node: merge duplicate candidates, blacklist conflicting/nonsensical ones, unify vocabulary.

    The model only returns decisions (groups of candidate ids, blacklist); apply_merge builds the
    records from the original candidates.
    """
    candidates = state["candidates"]
    resp = get_client().chat.completions.parse(
        model=MODELS["merge"],
        messages=[
            {"role": "system", "content": MERGER_PROMPT},
            {"role": "user", "content": build_merge_message(candidates)},
        ],
        response_format=MergeResult,
        max_completion_tokens=64000,
    )
    parsed = resp.choices[0].message.parsed
    if parsed is None:
        raise RuntimeError("merge_and_resolve: model returned no parsable result")
    requirements, blacklist, stats = apply_merge(candidates, parsed)
    print(f"  merge stats: {stats}")
    return {"requirements": requirements, "blacklist": blacklist}


# Pipeline order; also the names of the checkpoint files (output/states/NN_<name>.json).
# review_gate may loop back to extract: the loop is wired in build_graph.
STAGES = ["load_corpus", "chunk_documents", "extract", "verify_evidence",
          "review_completeness", "review_gate", "merge_and_resolve"]
NODES = {
    "load_corpus": load_corpus,
    "chunk_documents": chunk_documents,
    "extract": extract,
    "verify_evidence": verify_evidence,
    "review_completeness": review_completeness,
    "review_gate": review_gate,
    "merge_and_resolve": merge_and_resolve,
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
