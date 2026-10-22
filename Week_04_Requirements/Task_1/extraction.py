"""Requirement schema and extraction prompt shared by the extractor node and the benchmark."""
from typing import Literal, Optional

from pydantic import BaseModel, Field

EXTRACTOR_PROMPT = """\
You extract software requirements from a fragment of a project document \
(email thread, meeting minutes, interview, survey, specification, reference text, ...).

A requirement is something the software system must do, must be, or must respect \
(a feature, a quality, a constraint). Statements of need, complaints about the current \
system's limits, and explicit wishes all imply requirements.

Rules:
- Extract every distinct requirement in the fragment; one atomic requirement per item.
- Ignore chit-chat and anything unrelated to the software (food, books, scheduling, greetings).
- Do not invent requirements. If the fragment contains none, return an empty list.
- title: short and descriptive (3-8 words).
- description: one self-contained paragraph explaining the requirement in neutral, \
consistent vocabulary, understandable without the source text.
- evidence: a verbatim quote copied exactly from the fragment (one or two sentences) that supports it.
- date: ISO date (YYYY-MM-DD) of the message/meeting the requirement comes from if the \
fragment shows it, otherwise null.
- type: functional, non-functional, or constraint.
"""


class Requirement(BaseModel):
    title: str
    description: str
    evidence: str = Field(description="Verbatim quote from the fragment")
    type: Literal["functional", "non-functional", "constraint"]
    date: Optional[str] = Field(default=None, description="YYYY-MM-DD or null")


class ExtractionResult(BaseModel):
    requirements: list[Requirement]


def build_user_message(doc_id: str, index: int, total: int, text: str) -> str:
    return f"Document: {doc_id} (fragment {index + 1} of {total})\n\n---\n{text}\n---"
