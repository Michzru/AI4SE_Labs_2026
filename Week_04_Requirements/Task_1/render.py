"""Deterministic final steps: stable ids, Markdown rendering and a self-check of the document."""
import re
from datetime import date

from priority import LEVELS, PRIORITY_SCALE

CATEGORY_TEXT = {
    "conflict": "Conflicts with another requirement",
    "nonsense": "Too vague or not a software requirement",
    "out_of_scope": "Describes existing behaviour, not a new need",
}
QUOTES_SHOWN = 2


def assign_ids(requirements: list[dict], blacklist: list[dict]) -> tuple[list[dict], list[dict]]:
    """REQ-/BL- ids after dedup (never by a model). Order: priority, then first mention, then title."""
    ordered = sorted(requirements, key=lambda r: (LEVELS.index(r["priority"]), r["date"] or "9999", r["title"]))
    reqs = [{**r, "id": f"REQ-{n:03d}"} for n, r in enumerate(ordered, start=1)]
    owner = {cid: r["id"] for r in reqs for cid in r["member_ids"]}   # candidate id -> requirement id
    ordered_bl = sorted(blacklist, key=lambda b: (b["category"], b["title"]))
    # the merge model sometimes cites internal ids (C050, M1.2-03) in its reason; show REQ ids instead
    ref = re.compile(r"\b(C\d+|M\d\.\d+-\d+)\b")
    bl = [{**b, "id": f"BL-{n:03d}",
           "reason": ref.sub(lambda m: owner.get(m.group(1), "a related requirement"), b["reason"]),
           "conflicts_with": sorted({owner[c] for c in b["conflicts_with"] if c in owner})}
          for n, b in enumerate(ordered_bl, start=1)]
    return reqs, bl


def _line(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _cell(text: str) -> str:
    return _line(text).replace("|", "\\|")


def render_markdown(requirements: list[dict], blacklist: list[dict], documents: list[str]) -> str:
    out = ["# Software Requirements", "",
           f"Generated {date.today().isoformat()} from {len(documents)} source documents by an agentic "
           f"LangGraph pipeline. {len(requirements)} requirements, {len(blacklist)} blacklisted items.", "",
           "## Priority scale", "",
           "Priorities use three MoSCoW levels. Each requirement states below why it got its level.", ""]
    for level in LEVELS:
        n = sum(r["priority"] == level for r in requirements)
        out.append(f"- **{level}** ({n}): {PRIORITY_SCALE[level]}")
    out += ["",
            "How a level is chosen: an explicit priority tag in a source document is final. Otherwise it is "
            "computed from the number of distinct documents that mention the requirement and from emphatic "
            "wording in the stakeholders' own words; a language model may move the result by one level for "
            "content reasons.", "",
            "## Overview", "", "| ID | Requirement | Priority | Type | Sources |", "|---|---|---|---|---|"]
    out += [f"| {r['id']} | {_cell(r['title'])} | {r['priority']} | {r['type']} | {len(r['sources'])} |"
            for r in requirements]
    for level in LEVELS:
        group = [r for r in requirements if r["priority"] == level]
        if not group:
            continue
        out += ["", f"## {level} requirements", ""]
        for r in group:
            out += [f"### {r['id']} - {_line(r['title'])}", "",
                    f"**Priority:** {r['priority']} - {_line(r['priority_basis'])}  ",
                    f"**Type:** {r['type']}  ",
                    f"**First mentioned:** {r['date'] or 'unknown'}  ",
                    "**Sources:** " + ", ".join(f"`{s}`" for s in r["sources"]), "",
                    _line(r["description"]), ""]
            for ev in r["evidence"][:QUOTES_SHOWN]:
                quote = _line(ev["quote"])
                out.append(f"> {quote[:300]}{'...' if len(quote) > 300 else ''} (`{ev['source_doc']}`)")
            out.append("")
    out += ["## Blacklist", "",
            "Items found in the sources but discarded, with the reason. They are not part of the requirements above.", ""]
    if not blacklist:
        out.append("No items were discarded.")
    for b in blacklist:
        out += [f"### {b['id']} - {_line(b['title'])}", "",
                f"**Reason ({CATEGORY_TEXT[b['category']]}):** {_line(b['reason'])}  "]
        if b["conflicts_with"]:
            out.append("**Conflicts with:** " + ", ".join(b["conflicts_with"]) + "  ")
        out += ["**Sources:** " + ", ".join(f"`{s}`" for s in b["sources"]), ""]
    return "\n".join(out) + "\n"


def check_document(markdown: str, requirements: list[dict], blacklist: list[dict]) -> list[str]:
    """Self-check against the output spec; returns a list of problems (empty = OK)."""
    problems = []
    ids = [r.get("id") for r in requirements]
    if len(set(ids)) != len(ids) or None in ids:
        problems.append("OS2: requirement ids are missing or not unique")
    for r in requirements:
        rid = r.get("id", "?")
        if not r.get("title", "").strip() or not r.get("description", "").strip():
            problems.append(f"OS5: {rid} lacks a name or description")
        if r.get("priority") not in LEVELS:
            problems.append(f"OS6: {rid} has no valid priority")
        if not r.get("sources"):
            problems.append(f"OS4: {rid} has no source document")
        if f"### {rid} - " not in markdown:
            problems.append(f"OS1: {rid} is not in the document")
    for b in blacklist:
        if not b.get("reason", "").strip():
            problems.append(f"OS9: {b.get('id', '?')} has no reason")
        if f"### {b.get('id')} - " not in markdown:
            problems.append(f"OS9: {b.get('id')} is not in the document")
    for needed in ("## Priority scale", "## Blacklist"):
        if needed not in markdown:
            problems.append(f"missing section {needed}")
    return problems
