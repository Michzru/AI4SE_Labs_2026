"""Agentic network for software requirements refinement (LangGraph)."""
import argparse
from pathlib import Path
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

TEXT_SUFFIXES = {".txt", ".eml", ".md"}


class Document(TypedDict):
    id: str    # path relative to the input directory, used for tracing
    text: str


class State(TypedDict, total=False):
    input_dir: str
    documents: list[Document]


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


def build_graph():
    graph = StateGraph(State)
    graph.add_node("load_corpus", load_corpus)
    graph.add_edge(START, "load_corpus")
    graph.add_edge("load_corpus", END)
    return graph.compile()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", help="directory with the input corpus")
    args = parser.parse_args()
    result = build_graph().invoke({"input_dir": args.input_dir})
    for doc in result["documents"]:
        print(f"{len(doc['text']):>6}  {doc['id']}")
    print(f"{len(result['documents'])} documents loaded")


if __name__ == "__main__":
    main()
