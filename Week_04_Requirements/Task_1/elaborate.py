"""Paragraph writer and namer: prompts, schemas and code guards against invented content."""
import re

from pydantic import BaseModel, Field

PARAGRAPH_PROMPT = """\
You write the explanation paragraph of software requirements for a library reporting system.
For each requirement you get an ID, a short summary and excerpts from the source documents it comes from.

For each ID write ONE paragraph of 3-5 sentences (60-120 words): what the system must do, why or in which \
situation it is needed according to the sources, who needs it, and any condition or limit the sources state.
Rules:
- Use only information from the summary and the excerpts. Do not add numbers, names, systems or features \
that are not there.
- Neutral specification language ("The system must/should ..."); no quotes, no references to "the excerpt".
- Consistent vocabulary: "patron" (never user/borrower/customer) for library patrons, "staff" for library \
employees, "item" (not copy), "branch" for one library location.
- Never skip an ID and never invent one.
"""

NAME_PROMPT = """\
You give software requirements a short descriptive name from the requirement paragraph.
Rules: 3-6 words, Title Case, no articles, no trailing punctuation. Start with an action verb when the \
requirement is a capability (Report, Support, Provide, Allow, Track, Control, Prevent, Restrict, Export, ...), \
otherwise use a noun phrase (e.g. "Linux And Solaris Server Environment"). Say what makes this requirement \
different from similar ones. Use the words "patron", "staff", "item", "branch". Never skip an ID.
"""


class Paragraph(BaseModel):
    id: str
    paragraph: str


class ParagraphResult(BaseModel):
    items: list[Paragraph]


class Name(BaseModel):
    id: str
    name: str = Field(description="3-6 words, Title Case")


class NameResult(BaseModel):
    items: list[Name]


def build_paragraph_message(batch: list[dict]) -> str:
    parts = []
    for r in batch:
        excerpts = "\n".join(f"  [{c['source_doc']}]\n  " + c["text"].replace("\n", "\n  ") for c in r["contexts"])
        parts.append(f"ID: {r['_pid']}\nSummary: {r['title']}: {r['description']}\nExcerpts:\n{excerpts}")
    return "\n\n=====\n\n".join(parts)


def build_name_message(batch: list[dict]) -> str:
    return "\n\n".join(f"ID: {r['_pid']}\nParagraph: {r['description']}" for r in batch)


def paragraph_ok(paragraph: str, grounding: str) -> bool:
    """Guard: sensible length and no number that is absent from the summary and the excerpts."""
    if not 150 <= len(paragraph) <= 1200:
        return False
    numbers = set(re.findall(r"\d[\d,.]*\d|\d", paragraph))
    return all(n in grounding for n in numbers)


def name_ok(name: str) -> bool:
    words = name.split()
    return 2 <= len(words) <= 8 and len(name) <= 70 and not name.endswith((".", ":"))
