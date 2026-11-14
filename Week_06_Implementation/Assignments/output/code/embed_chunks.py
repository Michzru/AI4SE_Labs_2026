"""Task 3 – turn every chunk into an embedding.

Pipeline per chunk:
  1. LLM (gpt-5-mini) writes a short natural-language description of the code.
  2. embed_text = locator (file / class / defined names) + description
  3. local model BAAI/bge-small-en-v1.5 (fastembed, 384 dims, L2-normalised)

The OpenAI project has no access to embedding models, so the embedding itself is
computed locally; the LLM is only used to describe the chunk.

Output: chunk_store.json – list of {chunk metadata, text, summary, embed_text, embedding}.
Summaries are cached in summaries.json so re-runs do not call the LLM again.

Usage:
    python embed_chunks.py
"""
from __future__ import annotations

import json
import os
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from fastembed import TextEmbedding
from openai import OpenAI

HERE = Path(__file__).resolve().parent
CHUNKS = HERE / "chunks.json"
SUMMARIES = HERE / "summaries.json"
STORE = HERE / "chunk_store.json"

SUMMARY_MODEL = "gpt-5-mini"
EMBED_MODEL = "BAAI/bge-small-en-v1.5"

SYSTEM_PROMPT = """You describe Python code chunks for a code-search index.
Write a precise English description (3-6 sentences, max ~120 words) of the chunk:
- name the classes / functions / methods it defines and what each one does;
- mention important behaviour: validation, raised exceptions, return values, side effects;
- if a method body is only `pass` (not implemented), say "<Class.method> is not implemented yet"
  and state what it is supposed to do based on its name, signature and docstring;
- for test code, say which class/method is tested and which behaviours the tests check.
Plain prose only, no code, no bullet points, no preamble."""

_embedder: TextEmbedding | None = None


def get_embedder() -> TextEmbedding:
    global _embedder
    if _embedder is None:
        _embedder = TextEmbedding(EMBED_MODEL)
    return _embedder


def summarize(client: OpenAI, chunk: dict) -> str:
    resp = client.chat.completions.create(
        model=SUMMARY_MODEL,
        reasoning_effort="low",
        messages=[{"role": "system", "content": SYSTEM_PROMPT},
                  {"role": "user", "content": chunk["text"]}],
    )
    return resp.choices[0].message.content.strip()


def build_embed_text(chunk: dict, summary: str) -> str:
    names = [n for n in chunk["names"] if not n.startswith("<")]
    # whole-class chunks only list the class name -> add the methods defined in the code
    names += [m for m in re.findall(r"^\s*(?:async\s+)?def (\w+)", chunk["text"], re.M) if m not in names]
    parts = [f"File: {chunk['file']}"]
    if chunk["class_name"]:
        parts.append(f"Class: {chunk['class_name']}")
    if names:
        parts.append("Defines: " + ", ".join(names))
    parts.append(summary)
    return "\n".join(parts)


def embed_documents(texts: list[str]) -> np.ndarray:
    return np.array(list(get_embedder().passage_embed(texts)), dtype=np.float32)


def embed_query(text: str) -> np.ndarray:
    """Embed a task/query; bge uses an instruction prefix for queries (added by fastembed)."""
    return np.array(next(iter(get_embedder().query_embed(text))), dtype=np.float32)


def main() -> None:
    load_dotenv(HERE / ".env")
    client = OpenAI(api_key=os.environ["API_KEY"])
    chunks = json.loads(CHUNKS.read_text(encoding="utf-8"))

    cache: dict[str, str] = json.loads(SUMMARIES.read_text()) if SUMMARIES.exists() else {}
    todo = [c for c in chunks if c["id"] not in cache]
    print(f"summaries: {len(cache)} cached, {len(todo)} to generate with {SUMMARY_MODEL}")
    with ThreadPoolExecutor(max_workers=8) as pool:
        for c, s in zip(todo, pool.map(lambda c: summarize(client, c), todo)):
            cache[c["id"]] = s
    SUMMARIES.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")

    embed_texts = [build_embed_text(c, cache[c["id"]]) for c in chunks]
    vectors = embed_documents(embed_texts)
    store = [{
        "id": c["id"], "file": c["file"], "kind": c["kind"], "class_name": c["class_name"],
        "names": c["names"], "start_line": c["start_line"], "end_line": c["end_line"],
        "text": c["text"], "summary": cache[c["id"]], "embed_text": t,
        "embedding": [round(float(x), 6) for x in v],
    } for c, t, v in zip(chunks, embed_texts, vectors)]
    STORE.write_text(json.dumps(store, ensure_ascii=False), encoding="utf-8")
    print(f"{len(store)} chunks x {vectors.shape[1]} dims ({EMBED_MODEL}) -> {STORE}")


if __name__ == "__main__":
    main()
