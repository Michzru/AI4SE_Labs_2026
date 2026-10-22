"""Quality analysis of a finished run (run: python tools/analyze_output.py output/states). Code only, no API calls.

Reads the last checkpoint (render_doc input = assign_ids) and the rendered document and prints metrics
per output spec (OS1-OS9), plus near-duplicate pairs and vocabulary variants for manual review.
"""
import argparse
import sys
from pathlib import Path
import json
import re
from collections import Counter
from itertools import combinations

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # modules live one level up
from merge import cosine, tfidf_vectors
from render import check_document

NOISE = re.compile(r"costco|evelyn hugo|snacks|cookie|lunch|vacation", re.I)
# groups of words that name the same concept; several variants in use = inconsistent vocabulary
SYNONYMS = {
    "patron / user / borrower / customer": ["patron", "user", "borrower", "customer"],
    "item / copy": ["item", "copy"],
    "branch / library / location": ["branch", "library", "location"],
    "staff / librarian / employee": ["staff", "librarian", "employee"],
}


def latest_state(states_dir: Path, stage: str) -> dict:
    files = sorted(states_dir.glob(f"*_{stage}*.json"), key=lambda p: (len(p.name), p.name))
    return json.loads(files[-1].read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("states_dir")
    parser.add_argument("--document", default="output/requirements.md")
    parser.add_argument("--dup-threshold", type=float, default=0.6)
    args = parser.parse_args()
    state = latest_state(Path(args.states_dir), "assign_ids")
    reqs, bl = state["requirements"], state["blacklist"]
    cands = state["candidates"]
    markdown = Path(args.document).read_text(encoding="utf-8")
    doc_ids = [d["id"] for d in state["documents"]]

    print("== Pipeline")
    print(f"documents {len(doc_ids)}, chunks {len(state['chunks'])}, candidates {len(cands)} "
          f"-> requirements {len(reqs)} + blacklist {len(bl)}")
    print(f"unverified quotes among candidates: {sum(not c['evidence_ok'] for c in cands)} of {len(cands)}")
    last = max(r["round"] for r in state["reviews"])
    rounds = Counter()
    for r in state["reviews"]:
        rounds[r["round"]] += sum(m["quote_ok"] for m in r["missing"])
    print("reviewer-found missing items per round:", dict(sorted(rounds.items())),
          f"(still open after the last round: {rounds[last]}, ~{rounds[last] / len(cands):.1%} of candidates)")

    print("\n== Spec checks (OS1, OS2, OS4, OS5, OS6, OS9)")
    problems = check_document(markdown, reqs, bl)
    print("self-check problems:", problems or "none")
    print("priority distribution:", dict(Counter(r["priority"] for r in reqs)),
          "| priority source:", dict(Counter(r["priority_source"] for r in reqs)))
    print("avg description length:", round(sum(len(r["description"]) for r in reqs) / len(reqs)), "chars")
    print("blacklist categories:", dict(Counter(b["category"] for b in bl)),
          "| with conflicts_with:", sum(bool(b["conflicts_with"]) for b in bl))

    print("\n== Tracing (OS4): requirements per source document")
    per_doc = Counter(s for r in reqs for s in r["sources"])
    for d in doc_ids:
        print(f"{per_doc[d]:>4}  {d}")
    print("documents with no requirement:", [d for d in doc_ids if not per_doc[d]] or "none")
    print("requirements from 1 / 2 / 3+ documents:",
          sum(len(r["sources"]) == 1 for r in reqs), sum(len(r["sources"]) == 2 for r in reqs),
          sum(len(r["sources"]) >= 3 for r in reqs))

    print("\n== Noise leaking into requirements")
    leaks = [r["id"] + " " + r["title"] for r in reqs if NOISE.search(r["title"] + " " + r["description"])]
    print(leaks or "none")

    print(f"\n== Possible remaining duplicates (OS3): TF-IDF cosine >= {args.dup_threshold}")
    vectors = tfidf_vectors(reqs)
    pairs = sorted(((cosine(vectors[i], vectors[j]), i, j) for i, j in combinations(range(len(reqs)), 2)),
                   reverse=True)
    close = [p for p in pairs if p[0] >= args.dup_threshold]
    same_title = Counter(r["title"].lower() for r in reqs)
    print(f"{len(close)} pairs of {len(reqs)} requirements; identical titles: "
          f"{sum(n > 1 for n in same_title.values())}")
    for score, i, j in close[:15]:
        print(f"  {score:.2f}  {reqs[i]['id']} {reqs[i]['title']}  <->  {reqs[j]['id']} {reqs[j]['title']}")

    print("\n== Vocabulary (OS7): word-variant usage in requirement titles + descriptions")
    text = " ".join(r["title"] + " " + r["description"] for r in reqs).lower()
    for label, words in SYNONYMS.items():
        counts = {w: len(re.findall(rf"\b{w}s?\b", text)) for w in words}
        print(f"  {label}: {counts}")


if __name__ == "__main__":
    main()
