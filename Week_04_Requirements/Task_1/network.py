"""Agentic network for software requirements refinement (LangGraph)."""
import argparse
import re
from pathlib import Path
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

TEXT_SUFFIXES = {".txt", ".eml", ".md"}
DEFAULT_MAX_CHUNK_CHARS = 4000

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


class State(TypedDict, total=False):
    input_dir: str
    max_chunk_chars: int
    documents: list[Document]
    chunks: list[Chunk]


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


def build_graph():
    graph = StateGraph(State)
    graph.add_node("load_corpus", load_corpus)
    graph.add_node("chunk_documents", chunk_documents)
    graph.add_edge(START, "load_corpus")
    graph.add_edge("load_corpus", "chunk_documents")
    graph.add_edge("chunk_documents", END)
    return graph.compile()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", help="directory with the input corpus")
    parser.add_argument("--max-chunk-chars", type=int, default=DEFAULT_MAX_CHUNK_CHARS,
                        help="maximum size of one chunk in characters")
    args = parser.parse_args()
    result = build_graph().invoke(
        {"input_dir": args.input_dir, "max_chunk_chars": args.max_chunk_chars}
    )
    for doc in result["documents"]:
        n = sum(c["doc_id"] == doc["id"] for c in result["chunks"])
        print(f"{len(doc['text']):>6} chars  {n:>2} chunks  {doc['id']}")
    print(f"{len(result['documents'])} documents -> {len(result['chunks'])} chunks")


if __name__ == "__main__":
    main()
