"""Schema and prompt of the completeness reviewer (feedback-loop node)."""
from pydantic import BaseModel, Field

REVIEWER_PROMPT = """\
You review the completeness of a requirements extraction. You get one project document \
and the list of requirements already extracted from it.

Find software requirements that the document states or clearly implies but that NO extracted \
requirement covers. An extracted requirement covers a need if it expresses the same need, \
even in different words or at a different level of detail.

Rules:
- Report only genuinely missing requirements; do not repeat or rephrase extracted ones.
- Ignore chit-chat and anything unrelated to the software (food, books, scheduling, greetings).
- evidence: a verbatim quote copied exactly from the document that supports the missing requirement.
- If the extraction is complete, return an empty list.
"""


class MissingRequirement(BaseModel):
    description: str = Field(description="One sentence: what requirement is missing")
    evidence: str = Field(description="Verbatim quote from the document")


class ReviewResult(BaseModel):
    missing: list[MissingRequirement]


def build_review_message(doc_id: str, text: str, extracted: list[str]) -> str:
    listing = "\n".join(f"- {line}" for line in extracted) or "(nothing extracted)"
    return (f"Document: {doc_id}\n\n--- DOCUMENT ---\n{text}\n--- END DOCUMENT ---\n\n"
            f"Already extracted requirements ({len(extracted)}):\n{listing}")
