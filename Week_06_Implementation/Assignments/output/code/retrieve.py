"""Task 4 – match an input embedding against the chunk store and return the n most relevant chunks.

Similarity: cosine. Stored vectors are L2-normalised (bge via fastembed), the query is
normalised here, so cosine similarity == dot product -> one matrix-vector product.
Search: exact brute force over all chunks (95 x 384) with numpy; no ANN index needed.

Usage:
    python retrieve.py "Implement method can_afford of class Customer in playground/playground/models.py. ..." [n]
"""
from __future__ import annotations

import json
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
STORE = HERE / "chunk_store.json"


@lru_cache(maxsize=8)
def load_store(path: Path = STORE) -> tuple[list[dict], np.ndarray]:
    """Load chunks and their embedding matrix once (cached for repeated queries)."""
    store = json.loads(path.read_text(encoding="utf-8"))
    matrix = np.array([c["embedding"] for c in store], dtype=np.float32)
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True)  # guard: rounding in JSON
    return store, matrix


def cosine_scores(query_embedding: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    q = np.asarray(query_embedding, dtype=np.float32)
    q = q / np.linalg.norm(q)
    return matrix @ q


def top_n(query_embedding: np.ndarray, n: int = 5, store_path: Path = STORE) -> list[tuple[dict, float]]:
    """Return the n chunks with the highest cosine similarity, best first."""
    store, matrix = load_store(store_path)
    scores = cosine_scores(query_embedding, matrix)
    n = min(n, len(store))
    idx = np.argpartition(-scores, n - 1)[:n]          # O(N) selection of the top n
    idx = idx[np.argsort(-scores[idx])]                 # sort only those n
    return [(store[i], float(scores[i])) for i in idx]


def search(task_text: str, n: int = 5, store_path: Path = STORE) -> list[tuple[dict, float]]:
    """Convenience for Task 5: embed the textual task and return top-n chunks."""
    from embed_chunks import embed_query
    return top_n(embed_query(task_text), n, store_path)


if __name__ == "__main__":
    text = sys.argv[1]
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    for chunk, score in search(text, k):
        print(f"{score:.3f}  {chunk['id']:45s}  {chunk['kind']:10s}  {chunk['class_name'] or ''}")
