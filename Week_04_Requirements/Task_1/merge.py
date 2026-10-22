"""Merge/resolve step: clustering, prompt, schema and the deterministic application of the model's decisions.

Work unit = "item": a candidate, or a requirement already merged from several candidates in an earlier round.
"""
import math
import re
from collections import Counter
from typing import Literal

from pydantic import BaseModel, Field

MERGER_PROMPT = """\
You consolidate candidate requirements, extracted from many project documents, into one clean set.
Input: lines "ID | documents | date | title: description". The items are a topical cluster; some may \
already be merged results of an earlier pass.

Do two things.

1. MERGE duplicates. Items that express the same need (even in different words, or from \
different documents) form one group. For each group write ONE merged title (3-8 words) and ONE \
self-contained description paragraph that covers all members. Merge only true duplicates: distinct \
testable requirements stay separate even if they concern the same topic. Use consistent vocabulary: \
one term per concept in everything you write (e.g. always the same word for patron/user, item/copy, \
branch/library; choose the term the sources use most).

2. BLACKLIST items that must be discarded, each with a clear reason and a category:
 - conflict: contradicts another item. Blacklist the weaker one (superseded by a later \
decision, or less authoritative) and put the IDs of the contradicting item(s) you keep in \
conflicts_with. Never merge conflicting items.
 - nonsense: unrelated to the software, or too vague to be a testable requirement.
 - out_of_scope: only describes what an existing system already does, with no need for the new \
software expressed. Limitations and gaps of the existing system ARE requirements; keep them.

Items you do not mention are kept unchanged. So output only: groups with 2+ members (a \
single-member group only if its wording must change for consistent vocabulary) and the blacklist. \
Every ID appears at most once in the whole output. Do not invent requirements or IDs.
"""


class MergedGroup(BaseModel):
    member_ids: list[str]
    title: str
    description: str


class BlacklistItem(BaseModel):
    item_ids: list[str]
    title: str
    reason: str
    category: Literal["conflict", "nonsense", "out_of_scope"]
    conflicts_with: list[str] = Field(default_factory=list, description="IDs of the kept conflicting items")


class MergeResult(BaseModel):
    groups: list[MergedGroup]
    blacklist: list[BlacklistItem]


STOPWORDS = {"the", "and", "for", "that", "with", "this", "from", "are", "can", "any", "all", "should",
             "must", "shall", "system", "able", "allow", "provide", "support", "into", "their", "such",
             "have", "has", "not", "which", "when", "using", "used", "use", "also", "each", "than"}


def to_item(candidate: dict) -> dict:
    """A candidate is an item that merged nothing."""
    return {
        "id": candidate["id"], "title": candidate["title"], "description": candidate["description"],
        "type": candidate["type"], "date": candidate["date"], "member_ids": [candidate["id"]],
        "mentions": 1, "sources": [candidate["source_doc"]],
        "evidence": [{"source_doc": candidate["source_doc"], "quote": candidate["evidence"],
                      "verified": candidate["evidence_ok"]}],
    }


def cluster_batches(items: list[dict], batch_size: int) -> list[list[dict]]:
    """Group topically similar items (TF-IDF cosine) so that duplicates and conflicts land in one batch.

    Greedy: the first unassigned item seeds a batch, its nearest unassigned neighbours fill it.
    """
    if len(items) <= batch_size:
        return [items]
    docs = [Counter(w for w in re.findall(r"[a-z]{3,}", f"{it['title']} {it['description']}".lower())
                    if w not in STOPWORDS) for it in items]
    df = Counter(w for d in docs for w in d)
    vectors = []
    for d in docs:
        vec = {w: tf * math.log(len(items) / df[w]) for w, tf in d.items()}
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        vectors.append({w: v / norm for w, v in vec.items()})

    def sim(i: int, j: int) -> float:
        a, b = vectors[i], vectors[j]
        if len(a) > len(b):
            a, b = b, a
        return sum(v * b.get(w, 0.0) for w, v in a.items())

    unassigned = list(range(len(items)))
    batches = []
    while unassigned:
        seed, rest = unassigned[0], unassigned[1:]
        rest.sort(key=lambda j: (-sim(seed, j), j))
        take = [seed] + rest[:batch_size - 1]
        batches.append([items[i] for i in sorted(take)])
        taken = set(take)
        unassigned = [i for i in unassigned if i not in taken]
    return batches


def build_merge_message(items: list[dict]) -> str:
    lines = [f"{it['id']} | {', '.join(it['sources'])} | {it['date'] or '-'} | {it['title']}: {it['description']}"
             for it in items]
    return f"{len(items)} items:\n" + "\n".join(lines)


def _combine(members: list[dict], item_id: str, title: str, description: str) -> dict:
    dates = [m["date"] for m in members if m["date"]]
    types = Counter()
    for m in members:
        types[m["type"]] += m["mentions"]
    seen, evidence = set(), []
    for ev in sorted((e for m in members for e in m["evidence"]), key=lambda e: not e["verified"]):
        if ev["quote"] not in seen and len(evidence) < 5:
            seen.add(ev["quote"])
            evidence.append(ev)
    return {
        "id": item_id, "title": title, "description": description,
        "type": types.most_common(1)[0][0],
        "date": min(dates) if dates else None,
        "member_ids": [i for m in members for i in m["member_ids"]],
        "mentions": sum(m["mentions"] for m in members),
        "sources": sorted({s for m in members for s in m["sources"]}),
        "evidence": evidence,
    }


def apply_merge(items: list[dict], result: MergeResult, id_prefix: str) -> tuple[list[dict], list[dict], dict]:
    """Turn the model's decisions into merged items and blacklist records.

    Code, not the model, builds sources/evidence/counts from the original items, so tracing cannot be
    damaged. Unknown or repeated ids are ignored; blacklist wins over groups; whatever the model did
    not mention stays unchanged.
    """
    by_id = {it["id"]: it for it in items}
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
    for entry in result.blacklist:
        members = take(entry.item_ids)
        if members:
            combined = _combine(members, "", entry.title, entry.reason)
            blacklist.append({
                "title": entry.title, "reason": entry.reason, "category": entry.category,
                # item ids -> candidate ids, which stay valid across rounds
                "conflicts_with": [by_id[i]["member_ids"][0] for i in dict.fromkeys(entry.conflicts_with)
                                   if i in by_id],
                "member_ids": combined["member_ids"], "sources": combined["sources"],
                "evidence": combined["evidence"],
            })
    merged = []
    for n, group in enumerate(result.groups, start=1):
        members = take(group.member_ids)
        if members:
            merged.append(_combine(members, f"{id_prefix}-{n:02d}", group.title, group.description))
    merged += [it for it in items if it["id"] not in used]
    stats = {"in": len(items), "out": len(merged),
             "blacklisted": sum(len(b["member_ids"]) for b in blacklist), "ignored_ids": ignored}
    return merged, blacklist, stats
