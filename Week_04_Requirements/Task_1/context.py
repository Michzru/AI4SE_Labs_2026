"""Retrieval of source passages for a requirement (deterministic, no embeddings).

Primary route: the requirement keeps verbatim quotes, so each quote is located exactly in its document and the
surrounding paragraph(s) are returned. Fallback route (source document without a usable quote): the paragraph of
that document most similar to the requirement text (TF-IDF cosine).
"""
import re

from merge import cosine, tfidf_vectors
from textutil import squash_with_positions

MAX_CONTEXTS = 4
MIN_CHARS, MAX_CHARS = 400, 1200
PARAGRAPH_BREAK = re.compile(r"\n[ \t]*\n|\n[=\-]{3,}[ \t]*\n")


def paragraphs(text: str) -> list[tuple[int, int]]:
    """(start, end) spans of paragraphs, split at blank lines and separator lines."""
    spans, pos = [], 0
    for m in PARAGRAPH_BREAK.finditer(text):
        if text[pos:m.start()].strip():
            spans.append((pos, m.start()))
        pos = m.end()
    if text[pos:].strip():
        spans.append((pos, len(text)))
    return spans


def _expand(text: str, spans: list[tuple[int, int]], k: int, pos: int | None) -> str:
    """Passage around paragraph k.

    Short paragraph: neighbours are added while it is shorter than MIN_CHARS, up to MAX_CHARS.
    Long paragraph (typically a bullet list): its first line (heading) plus the lines around the quote at pos.
    """
    a, b = spans[k]
    if b - a > MAX_CHARS:
        lines = text[a:b].split("\n")
        at, offset = 0, 0
        for i, line in enumerate(lines):                      # line containing pos
            if pos is not None and a + offset + len(line) >= pos:
                at = i
                break
            offset += len(line) + 1
        picked = lines[max(1, at - 3):at + 4]
        head = [lines[0]] + (["..."] if at - 3 > 1 else [])
        return "\n".join(head + picked)[:MAX_CHARS]
    lo = hi = k
    while spans[hi][1] - spans[lo][0] < MIN_CHARS and (lo > 0 or hi < len(spans) - 1):
        if lo > 0 and (hi == len(spans) - 1 or k - lo <= hi - k):
            lo -= 1
        else:
            hi += 1
        if spans[hi][1] - spans[lo][0] > MAX_CHARS:
            break
    return re.sub(r"[ \t]+\n", "\n", text[spans[lo][0]:spans[hi][1]]).strip()[:MAX_CHARS]


def locate(quote: str, doc_index: tuple) -> tuple[int, int] | None:
    """(paragraph index, text position) of the quote, or None. doc_index = (squashed, positions, text, spans)."""
    squashed, positions, _, spans = doc_index
    q, _ = squash_with_positions(quote)
    at = squashed.find(q) if q else -1
    if at < 0:
        return None
    start = positions[at]
    return next((k for k, (a, b) in enumerate(spans) if a <= start < b or start < a), len(spans) - 1), start


def index_documents(documents: list[dict]) -> dict[str, tuple]:
    return {d["id"]: (*squash_with_positions(d["text"]), d["text"], paragraphs(d["text"])) for d in documents}


def best_paragraph(query: str, doc_index: tuple) -> tuple[int, None] | None:
    """TF-IDF nearest paragraph of a document to the query text."""
    _, _, text, spans = doc_index
    if not spans:
        return None
    items = [{"title": "", "description": query}] + [{"title": "", "description": text[a:b]} for a, b in spans]
    vectors = tfidf_vectors(items)
    scores = [cosine(vectors[0], v) for v in vectors[1:]]
    return (max(range(len(spans)), key=scores.__getitem__), None) if max(scores) > 0 else None


def retrieve(req: dict, docs: dict[str, tuple]) -> list[dict]:
    """Up to MAX_CONTEXTS passages {source_doc, text, how} backing the requirement, one per document first."""
    found, seen = [], set()

    def add(doc_id: str, hit: tuple[int, int | None] | None, how: str):
        if hit is None or (doc_id, hit) in seen or len(found) >= MAX_CONTEXTS:
            return
        seen.add((doc_id, hit))
        _, _, text, spans = docs[doc_id]
        found.append({"source_doc": doc_id, "text": _expand(text, spans, *hit), "how": how})

    for ev in sorted(req["evidence"], key=lambda e: not e["verified"]):
        if ev["source_doc"] not in {f["source_doc"] for f in found}:   # one passage per document first
            add(ev["source_doc"], locate(ev["quote"], docs[ev["source_doc"]]), "quote")
    for doc_id in req["sources"]:
        if doc_id not in {f["source_doc"] for f in found}:
            add(doc_id, best_paragraph(f"{req['title']} {req['description']}", docs[doc_id]), "similarity")
    for ev in req["evidence"]:                                          # remaining budget: more quotes
        add(ev["source_doc"], locate(ev["quote"], docs[ev["source_doc"]]), "quote")
    return found
