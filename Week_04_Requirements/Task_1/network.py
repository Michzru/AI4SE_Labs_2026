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

TEXT_SUFFIXES = {".txt", ".eml", ".md"}
DEFAULT_MAX_CHUNK_CHARS = 4000
MODELS = {"extract": "gpt-5.6-luna"}
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
                chunk["doc_id"], chunk["index"], chunk["total"], chunk["text"])},
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


# Pipeline order; also the names of the checkpoint files (output/states/NN_<name>.json).
STAGES = ["load_corpus", "chunk_documents", "extract", "verify_evidence"]
NODES = {
    "load_corpus": load_corpus,
    "chunk_documents": chunk_documents,
    "extract": extract,
    "verify_evidence": verify_evidence,
}


def build_graph(start_at: str = STAGES[0], stop_after: str = STAGES[-1]):
    """Compile the graph for the stages start_at..stop_after (lets us resume from a checkpoint)."""
    stages = STAGES[STAGES.index(start_at):STAGES.index(stop_after) + 1]
    graph = StateGraph(State)
    previous = START
    for name in stages:
        graph.add_node(name, NODES[name])
        if name == "extract":
            graph.add_conditional_edges(previous, fan_out, ["extract"])
        else:
            graph.add_edge(previous, name)
        previous = name
    graph.add_edge(previous, END)
    return graph.compile()


def snapshot_path(output_dir: Path, stage: str) -> Path:
    return output_dir / "states" / f"{STAGES.index(stage) + 1:02d}_{stage}.json"


def save_snapshot(output_dir: Path, stage: str, state: dict) -> None:
    path = snapshot_path(output_dir, stage)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")


def load_snapshot(output_dir: Path, stage: str) -> dict:
    return json.loads(snapshot_path(output_dir, stage).read_text(encoding="utf-8"))


def summarize(stage: str, state: dict) -> str:
    counts = {k: len(state[k]) for k in ("documents", "chunks", "raw_candidates", "candidates") if k in state}
    text = ", ".join(f"{n} {k}" for k, n in counts.items())
    if "candidates" in state:
        text += f" ({sum(not c['evidence_ok'] for c in state['candidates'])} with unverified quote)"
    return f"[{stage}] {text}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", help="directory with the input corpus")
    parser.add_argument("--max-chunk-chars", type=int, default=DEFAULT_MAX_CHUNK_CHARS,
                        help="maximum size of one chunk in characters")
    parser.add_argument("--output-dir", default="output", help="where checkpoints and the result go")
    parser.add_argument("--start-at", choices=STAGES, default=STAGES[0],
                        help="resume: load the checkpoint of the previous stage and run from this stage")
    parser.add_argument("--stop-after", choices=STAGES, default=STAGES[-1],
                        help="stop after this stage")
    args = parser.parse_args()
    load_dotenv(find_dotenv(usecwd=True))
    output_dir = Path(args.output_dir)

    if args.start_at == STAGES[0]:
        state = {"input_dir": args.input_dir, "max_chunk_chars": args.max_chunk_chars}
    else:
        state = load_snapshot(output_dir, STAGES[STAGES.index(args.start_at) - 1])

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
