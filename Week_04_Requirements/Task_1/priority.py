"""Prioritization: deterministic signals and baseline, a tightly bounded model opinion, a clamp.

The model can only pick one of three levels per requirement id and may move the baseline by one step;
code computes the baseline, validates the answer and falls back to the baseline on anything unexpected.
"""
import re
from typing import Literal

from pydantic import BaseModel, Field

from textutil import squash_with_positions

LEVELS = ["Must", "Should", "Could"]   # high -> low

PRIORITY_SCALE = {
    "Must": "Essential. Stated as high priority in a source document, or confirmed by several independent "
            "documents and strong wording. The system is not acceptable without it.",
    "Should": "Important. Wanted by more than one document, or stated with strong wording, "
              "or marked medium priority. Include unless time is short.",
    "Could": "Desirable. Mentioned once and without emphasis. Include if capacity allows.",
}

# Explicit priority tags of the source, e.g. "[* High Priority]" at the end of an SRS item.
STATED = re.compile(r"\[\*\s*(High|Medium|Low)\s+Priority\]", re.I)
STATED_LEVEL = {"high": "Must", "medium": "Should", "low": "Could"}
# Emphatic wording in the stakeholders' own words (the verbatim quotes, not the model's paraphrase).
STRONG = re.compile(r"\b(must|critical|essential|crucial|mandatory|vital|imperative|"
                    r"top priority|high priority)\b", re.I)

PRIORITIZER_PROMPT = """\
You rate the priority of software requirements for a library reporting system with MoSCoW levels: \
Must, Should, Could.
For each requirement you get an ID, title, description and a BASELINE level computed from objective \
signals (how many documents mention it, emphatic wording, explicit tags in the sources).
Return for every ID your own level and a short note (max 15 words). Keep the baseline unless the \
content clearly deserves one level higher or lower: core reporting/data-integrity/security/legal needs \
rate higher, cosmetic or convenience features rate lower. Never skip an ID and never invent one.
"""


class PriorityItem(BaseModel):
    id: str
    priority: Literal["Must", "Should", "Could"]
    note: str = Field(description="Max 15 words")


class PriorityResult(BaseModel):
    items: list[PriorityItem]


def stated_priority(req: dict, doc_index: dict[str, tuple[str, list[int], str]]) -> str | None:
    """Explicit priority tag found next to the requirement's quotes in the source documents.

    doc_index maps doc id -> (squashed text, positions, original text).
    """
    levels = []
    for ev in req["evidence"]:
        squashed, positions, text = doc_index[ev["source_doc"]]
        quote, _ = squash_with_positions(ev["quote"])
        at = squashed.find(quote) if quote else -1
        if at < 0:
            continue
        start = positions[at]
        end = re.search(r"\n[ \t]*\n", text[start:])
        window = text[start:start + end.start()] if end else text[start:]
        tag = STATED.search(window)
        if tag:
            levels.append(STATED_LEVEL[tag.group(1).lower()])
    return min(levels, key=LEVELS.index) if levels else None


def signals(req: dict, doc_index: dict) -> dict:
    quotes = " ".join(ev["quote"] for ev in req["evidence"])
    return {
        "stated": stated_priority(req, doc_index),
        "source_count": len(req["sources"]),
        "mentions": req["mentions"],
        "strong_words": sorted({m.group(0).lower() for m in STRONG.finditer(quotes)}),
    }


def baseline(sig: dict) -> tuple[str, str]:
    """Deterministic level and its explanation. A stated tag is authoritative."""
    if sig["stated"]:
        return sig["stated"], "Marked as priority in the source document."
    score = sig["source_count"] - 1 + bool(sig["strong_words"])
    level = "Must" if score >= 3 else "Should" if score >= 1 else "Could"
    parts = [f"mentioned in {sig['source_count']} document{'s' * (sig['source_count'] != 1)}"]
    if sig["strong_words"]:
        parts.append("strong wording (" + ", ".join(sig["strong_words"]) + ")")
    return level, "; ".join(parts).capitalize() + "."


def clamp(base: str, proposed: str | None, locked: bool) -> str:
    """The model may move the baseline by at most one level; a stated priority is never changed."""
    if locked or proposed not in LEVELS:
        return base
    i = LEVELS.index(base)
    return LEVELS[min(max(LEVELS.index(proposed), i - 1), i + 1)]


def build_priority_message(batch: list[dict]) -> str:
    return "\n".join(f"{r['_pid']} | baseline: {r['_base']} | {r['title']}: {r['description']}" for r in batch)
