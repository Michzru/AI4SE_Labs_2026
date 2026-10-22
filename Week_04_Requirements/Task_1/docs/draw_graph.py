"""Draws the network diagram (docs/graph.svg) without external tools: python docs/draw_graph.py"""
from pathlib import Path
from xml.sax.saxutils import escape

# (name, kind, model, note); kind: start | end | code | llm
NODES = [
    ("START", "start", "", ""),
    ("load_corpus", "code", "", "read all .txt / .eml / .md recursively"),
    ("chunk_documents", "code", "", "lossless split, max 4000 characters"),
    ("extract", "llm", "gpt-5.6-luna", "parallel: one call per chunk (Send)"),
    ("verify_evidence", "code", "", "quote check, candidate ids, source_doc"),
    ("review_completeness", "llm", "gpt-6-luna", "parallel: one call per document"),
    ("review_gate", "code", "", "join reviews, decide whether to loop"),
    ("merge_and_resolve", "llm", "gpt-6-luna", "topic clusters, 2 rounds: duplicates, conflicts, blacklist"),
    ("prioritize", "llm", "gpt-5.4-nano", "code baseline from signals, model moves it by <= 1 level"),
    ("retrieve_context", "code", "", "source passages found by quote anchoring"),
    ("write_paragraphs", "llm", "gpt-5.6-luna", "paragraph grounded in the passages, guarded"),
    ("name_requirements", "llm", "gpt-5.4-nano", "short descriptive name"),
    ("assign_ids", "code", "", "REQ- / BL- ids, ordering by priority and date"),
    ("render_doc", "code", "", "Markdown document + spec self-check"),
    ("END", "end", "", ""),
]
STYLE = {"code": ("#e8eef7", "#5b7aa6"), "llm": ("#fff1d6", "#d08a1c"), "start": ("#2b2b2b", "#2b2b2b"),
         "end": ("#2b2b2b", "#2b2b2b")}
W, CX, BW, BH, GAP, TOP = 820, 330, 380, 56, 26, 110


def main():
    out, centers = [], {}
    height = TOP + len(NODES) * (BH + GAP) + 20
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height}" width="{W}" height="{height}" '
               f'font-family="Helvetica, Arial, sans-serif">')
    out.append('<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
               'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker>'
               '<marker id="r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
               'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#b3402a"/></marker></defs>')
    out.append(f'<rect width="{W}" height="{height}" fill="#ffffff"/>')
    out.append('<text x="30" y="38" font-size="22" font-weight="bold" fill="#222">Requirements refinement network (LangGraph)</text>')
    for i, (label, fill) in enumerate([("deterministic node (code)", "code"), ("agentic node (LLM call)", "llm")]):
        x = 30 + i * 260
        out.append(f'<rect x="{x}" y="58" width="22" height="16" rx="3" fill="{STYLE[fill][0]}" stroke="{STYLE[fill][1]}" stroke-width="1.5"/>'
                   f'<text x="{x + 30}" y="71" font-size="13" fill="#333">{label}</text>')
    out.append('<line x1="530" y1="66" x2="570" y2="66" stroke="#b3402a" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#r)"/>'
               '<text x="578" y="71" font-size="13" fill="#333">feedback loop</text>')
    for n, (name, kind, model, note) in enumerate(NODES):
        y = TOP + n * (BH + GAP)
        fill, stroke = STYLE[kind]
        centers[name] = y
        if kind in ("start", "end"):
            out.append(f'<rect x="{CX - 60}" y="{y + 12}" width="120" height="32" rx="16" fill="{fill}"/>'
                       f'<text x="{CX}" y="{y + 34}" font-size="14" fill="#fff" text-anchor="middle" font-weight="bold">{name}</text>')
        else:
            out.append(f'<rect x="{CX - BW // 2}" y="{y}" width="{BW}" height="{BH}" rx="9" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
            title = f"{name}" + (f"  ·  {model}" if model else "")
            out.append(f'<text x="{CX}" y="{y + 23}" font-size="15" font-weight="bold" fill="#222" text-anchor="middle">{escape(title)}</text>'
                       f'<text x="{CX}" y="{y + 43}" font-size="12" fill="#444" text-anchor="middle">{escape(note)}</text>')
        if n:
            prev_y = y - (BH + GAP)
            prev_bottom = prev_y + (44 if NODES[n - 1][1] == "start" else BH)
            out.append(f'<line x1="{CX}" y1="{prev_bottom}" x2="{CX}" y2="{y + (12 if kind == "end" else 0) - 2}" '
                       f'stroke="#555" stroke-width="2" marker-end="url(#a)"/>')
    # feedback loop: review_gate -> extract (right side)
    gate_y, ext_y = centers["review_gate"] + BH // 2, centers["extract"] + BH // 2
    x0, x1 = CX + BW // 2, CX + BW // 2 + 70
    out.append(f'<path d="M{x0},{gate_y} H{x1} V{ext_y} H{x0 + 2}" fill="none" stroke="#b3402a" stroke-width="2.5" '
               f'stroke-dasharray="7 5" marker-end="url(#r)"/>')
    out.append(f'<text x="{x1 + 10}" y="{(gate_y + ext_y) // 2 - 14}" font-size="12" fill="#b3402a">missing items found</text>'
               f'<text x="{x1 + 10}" y="{(gate_y + ext_y) // 2}" font-size="12" fill="#b3402a">and round &lt; 2:</text>'
               f'<text x="{x1 + 10}" y="{(gate_y + ext_y) // 2 + 14}" font-size="12" fill="#b3402a">re-extract only the</text>'
               f'<text x="{x1 + 10}" y="{(gate_y + ext_y) // 2 + 28}" font-size="12" fill="#b3402a">affected documents</text>')
    out.append(f'<text x="{x1 + 10}" y="{gate_y + 24}" font-size="12" fill="#555">otherwise: continue</text>')
    out.append("</svg>")
    path = Path(__file__).with_name("graph.svg")
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
