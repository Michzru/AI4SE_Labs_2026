#!/usr/bin/env python3
"""Build an HTML page that renders every ```mermaid block of a Markdown file.

Usage: python3 mermaid_check.py <file.md> [--out page.html]

Open the printed page in a browser. The element with id="summary" lists each
diagram as OK or with the Mermaid error, so it can be read as plain text
(e.g. get_page_text) without looking at screenshots.
"""
import argparse
import json
import re
import tempfile
from pathlib import Path

MERMAID_VERSION = "11.4.1"
BLOCK_RE = re.compile(r"^```mermaid[ \t]*\n(.*?)^```", re.MULTILINE | re.DOTALL)

PAGE = """<!doctype html>
<html><head><meta charset="utf-8"><title>Mermaid check: __NAME__</title>
<style>
 body { font-family: system-ui, sans-serif; margin: 16px; background: #fff; color: #111; }
 #summary { white-space: pre-wrap; font-family: ui-monospace, monospace; padding: 8px; border: 1px solid #ccc; }
 .diagram { border-top: 1px solid #ddd; margin-top: 24px; padding-top: 8px; overflow-x: auto; }
 .err { color: #b00020; white-space: pre-wrap; font-family: ui-monospace, monospace; }
</style></head>
<body>
<h1>Mermaid check: __NAME__</h1>
<div id="summary">Rendering…</div>
<div id="diagrams"></div>
<script id="blocks" type="application/json">__BLOCKS__</script>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@__VERSION__/dist/mermaid.esm.min.mjs";
mermaid.initialize({ startOnLoad: false, securityLevel: "loose" });
const blocks = JSON.parse(document.getElementById("blocks").textContent);
const lines = [];
for (const [i, b] of blocks.entries()) {
  const box = document.createElement("div");
  box.className = "diagram";
  box.innerHTML = `<h2>Diagram ${i + 1} (line ${b.line})</h2>`;
  document.getElementById("diagrams").appendChild(box);
  try {
    const { svg } = await mermaid.render(`d${i}`, b.code);
    box.insertAdjacentHTML("beforeend", svg);
    lines.push(`Diagram ${i + 1} (line ${b.line}): OK`);
  } catch (e) {
    const msg = String(e && e.message ? e.message : e);
    box.insertAdjacentHTML("beforeend", `<div class="err"></div>`);
    box.lastChild.textContent = msg;
    lines.push(`Diagram ${i + 1} (line ${b.line}): ERROR ${msg.split("\\n").slice(0, 4).join(" | ")}`);
  }
}
const failed = lines.filter(l => l.includes("ERROR")).length;
document.getElementById("summary").textContent =
  `${blocks.length} diagram(s), ${failed} failed\\n` + lines.join("\\n");
</script>
</body></html>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    text = args.markdown.read_text(encoding="utf-8")
    blocks = [
        {"line": text.count("\n", 0, m.start()) + 1, "code": m.group(1)}
        for m in BLOCK_RE.finditer(text)
    ]
    if not blocks:
        print(f"No mermaid blocks in {args.markdown}")
        return

    out = args.out or Path(tempfile.gettempdir()) / f"mermaid_check_{args.markdown.stem}.html"
    payload = json.dumps(blocks).replace("</", "<\\/")
    html = (PAGE.replace("__NAME__", args.markdown.name)
                .replace("__VERSION__", MERMAID_VERSION)
                .replace("__BLOCKS__", payload))
    out.write_text(html, encoding="utf-8")
    print(f"{len(blocks)} mermaid block(s) found. Open: file://{out.resolve()}")


if __name__ == "__main__":
    main()
