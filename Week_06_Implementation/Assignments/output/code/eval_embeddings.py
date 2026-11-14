"""Task 3 – sanity check of the embedding choice.

For each task in missing_code.json the "gold" chunk is the one containing the
target class + `def method`. We embed a query and check where the gold chunk ranks
(recall@1, recall@5, MRR) for several representations:

  summary  – embed_text from chunk_store.json (LLM description + locator)   <- chosen
  raw_code – the raw chunk text embedded by the same bge-small model
  tfidf    – lexical TF-IDF over raw chunk text (baseline, no model)

Two query styles:
  full     – "Implement <Class>.<method> in <file>. <docstring>"   (names given)
  doc_only – only the docstring (no identifiers -> pure semantic match)
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path

import numpy as np

from embed_chunks import embed_documents, embed_query

HERE = Path(__file__).resolve().parent
TASKS = HERE.parent.parent / "missing_code.json"


def tokenize(s: str) -> list[str]:
    words = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", s)
    out = []
    for w in words:  # split snake_case and CamelCase as well
        out.append(w.lower())
        out += [p.lower() for p in re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])|\d+", w)]
    return out


class TfIdf:
    def __init__(self, docs: list[str]):
        self.tfs = [Counter(tokenize(d)) for d in docs]
        df = Counter(t for tf in self.tfs for t in tf)
        self.idf = {t: math.log(len(docs) / n) + 1 for t, n in df.items()}
        self.vecs = [self._vec(tf) for tf in self.tfs]

    def _vec(self, tf: Counter) -> dict:
        v = {t: c * self.idf.get(t, 0) for t, c in tf.items()}
        n = math.sqrt(sum(x * x for x in v.values())) or 1
        return {t: x / n for t, x in v.items()}

    def scores(self, q: str) -> np.ndarray:
        qv = self._vec(Counter(tokenize(q)))
        return np.array([sum(w * d.get(t, 0) for t, w in qv.items()) for d in self.vecs])


def gold_index(store: list[dict], task: dict) -> int:
    for i, c in enumerate(store):
        code = c["text"]
        if c["file"] == task["file"] and f"def {task['method']}(" in code and (
                c["class_name"] == task["class"] or re.search(rf"class {task['class']}\b", code)):
            return i
    raise LookupError(task)


def main() -> None:
    store = json.loads((HERE / "chunk_store.json").read_text())
    tasks = json.loads(TASKS.read_text())
    gold = [gold_index(store, t) for t in tasks]
    queries = {
        "full": [f"Implement method {t['method']} of class {t['class']} in {t['file']}. "
                 f"{t['docstring'].strip().strip(chr(34))}" for t in tasks],
        "doc_only": [t["docstring"].strip().strip('"') for t in tasks],
    }
    summary_m = np.array([c["embedding"] for c in store], dtype=np.float32)
    raw_m = embed_documents([c["text"] for c in store])
    tfidf = TfIdf([c["text"] for c in store])

    methods = {
        "summary": lambda q: summary_m @ embed_query(q),
        "raw_code": lambda q: raw_m @ embed_query(q),
        "tfidf": tfidf.scores,
    }
    print(f"{'method':9s} {'query':9s} R@1   R@5   MRR   ranks")
    for qname, qs in queries.items():
        for mname, score in methods.items():
            ranks = []
            for q, g in zip(qs, gold):
                order = np.argsort(-score(q))
                ranks.append(int(np.where(order == g)[0][0]) + 1)
            r1 = np.mean([r <= 1 for r in ranks]); r5 = np.mean([r <= 5 for r in ranks])
            mrr = np.mean([1 / r for r in ranks])
            print(f"{mname:9s} {qname:9s} {r1:.2f}  {r5:.2f}  {mrr:.2f}  {ranks}")


if __name__ == "__main__":
    main()
