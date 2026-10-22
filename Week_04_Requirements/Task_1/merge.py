"""Merge/resolve step: prompt, schema and the deterministic application of the model's decisions."""
from collections import Counter
from typing import Literal

from pydantic import BaseModel, Field

MERGER_PROMPT = """\
You consolidate candidate requirements, extracted from many project documents, into one clean set.
Input: lines "ID | document | date | title: description".

Do two things.

1. MERGE duplicates. Candidates that express the same need (even in different words, or from \
different documents) form one group. For each group write ONE merged title (3-8 words) and ONE \
self-contained description paragraph that covers all members. Merge only true duplicates: distinct \
testable requirements stay separate even if they concern the same topic. Use consistent vocabulary: \
one term per concept in everything you write (e.g. always the same word for patron/user, item/copy, \
branch/library; choose the term the sources use most).

2. BLACKLIST candidates that must be discarded, each with a clear reason and a category:
 - conflict: contradicts another candidate. Blacklist the weaker one (superseded by a later \
decision, or less authoritative) and put the IDs of the contradicting candidate(s) you keep in \
conflicts_with. Never merge conflicting candidates.
 - nonsense: unrelated to the software, or too vague to be a testable requirement.
 - out_of_scope: only describes what an existing system already does, with no need for the new \
software expressed. Limitations and gaps of the existing system ARE requirements; keep them.

Candidates you do not mention are kept unchanged. So output only: groups with 2+ members (a \
single-member group only if its wording must change for consistent vocabulary) and the blacklist. \
Every ID appears at most once in the whole output. Do not invent requirements or IDs.
"""


class MergedGroup(BaseModel):
    member_ids: list[str]
    title: str
    description: str


class BlacklistItem(BaseModel):
    candidate_ids: list[str]
    title: str
    reason: str
    category: Literal["conflict", "nonsense", "out_of_scope"]
    conflicts_with: list[str] = Field(default_factory=list, description="IDs of the kept conflicting candidates")


class MergeResult(BaseModel):
    groups: list[MergedGroup]
    blacklist: list[BlacklistItem]


def build_merge_message(candidates: list[dict]) -> str:
    lines = [f"{c['id']} | {c['source_doc']} | {c['date'] or '-'} | {c['title']}: {c['description']}"
             for c in candidates]
    return f"{len(candidates)} candidates:\n" + "\n".join(lines)


def _quotes(members: list[dict], limit: int = 5) -> list[dict]:
    """Verified quotes first, one per distinct text."""
    seen, out = set(), []
    for c in sorted(members, key=lambda c: not c["evidence_ok"]):
        if c["evidence"] not in seen and len(out) < limit:
            seen.add(c["evidence"])
            out.append({"source_doc": c["source_doc"], "quote": c["evidence"], "verified": c["evidence_ok"]})
    return out


def _requirement(members: list[dict], title: str, description: str) -> dict:
    dates = [c["date"] for c in members if c["date"]]
    return {
        "title": title,
        "description": description,
        "type": Counter(c["type"] for c in members).most_common(1)[0][0],
        "date": min(dates) if dates else None,
        "member_ids": [c["id"] for c in members],
        "mentions": len(members),                                   # merged candidates
        "sources": sorted({c["source_doc"] for c in members}),      # distinct documents
        "evidence": _quotes(members),
    }


def apply_merge(candidates: list[dict], result: MergeResult) -> tuple[list[dict], list[dict], dict]:
    """Turn the model's decisions into requirement and blacklist records.

    Code, not the model, builds sources/evidence/counts from the original candidates, so tracing cannot
    be damaged. Unknown or repeated ids are ignored; blacklist wins over groups; whatever the model did
    not mention stays as a single requirement.
    """
    by_id = {c["id"]: c for c in candidates}
    used: set[str] = set()
    ignored = 0

    def take(ids: list[str]) -> list[dict]:
        nonlocal ignored
        members = []
        for i in dict.fromkeys(ids):
            if i in by_id and i not in used:
                members.append(by_id[i])
                used.add(i)
            else:
                ignored += 1
        return members

    blacklist = []
    for item in result.blacklist:
        members = take(item.candidate_ids)
        if members:
            blacklist.append({
                "title": item.title, "reason": item.reason, "category": item.category,
                "conflicts_with": [i for i in dict.fromkeys(item.conflicts_with) if i in by_id],
                "member_ids": [c["id"] for c in members],
                "sources": sorted({c["source_doc"] for c in members}),
                "evidence": _quotes(members),
            })
    requirements = []
    for group in result.groups:
        members = take(group.member_ids)
        if members:
            requirements.append(_requirement(members, group.title, group.description))
    for c in candidates:
        if c["id"] not in used:
            requirements.append(_requirement([c], c["title"], c["description"]))
    requirements.sort(key=lambda r: r["member_ids"][0])
    stats = {"candidates": len(candidates), "requirements": len(requirements),
             "blacklisted": sum(len(b["member_ids"]) for b in blacklist), "ignored_ids": ignored}
    return requirements, blacklist, stats
