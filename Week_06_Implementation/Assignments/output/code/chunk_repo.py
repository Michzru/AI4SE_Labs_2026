"""Task 2 – AST-based chunking of the AI4SE_Playground repository.

Splits every .py file along syntactic boundaries (top-level classes / functions /
statements, and class methods for large classes) and merges small neighbouring
units until a token budget is reached. Output: a JSON list of chunks.

Usage:
    python chunk_repo.py [REPO_ROOT] [OUTPUT_JSON]
"""
from __future__ import annotations

import ast
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

TARGET_TOKENS = 500  # merge neighbouring units up to this size
MAX_TOKENS = 800     # a single unit above this is split further
MIN_TOKENS = 100     # smaller groups are folded into a neighbour

HERE = Path(__file__).resolve().parent
DEFAULT_REPO = HERE.parent / "week6" / "AI4SE_Playground"
DEFAULT_OUT = HERE / "chunks.json"

try:
    import tiktoken

    _ENC = tiktoken.get_encoding("o200k_base")  # tokenizer of gpt-4o / 4.1 / 5 models

    def count_tokens(text: str) -> int:
        return len(_ENC.encode(text))
except ImportError:  # fallback: measured ratio for this repo is ~4.2 chars/token
    def count_tokens(text: str) -> int:
        return max(1, len(text) // 4)


@dataclass
class Chunk:
    id: str
    file: str
    kind: str            # "module" | "class" | "class_part"
    names: list[str]     # top-level names / methods contained in the chunk
    class_name: str | None
    start_line: int      # 1-based, inclusive
    end_line: int
    n_tokens: int
    header: str          # short locator prepended to the code in `text`
    code: str            # raw source lines
    text: str            # header + code (what later steps embed / show the LLM)


@dataclass
class Unit:
    """Contiguous line range [start, end] (1-based) belonging to one AST node."""
    start: int
    end: int
    name: str
    node: ast.AST | None


def _node_start(node: ast.AST) -> int:
    decos = getattr(node, "decorator_list", None) or []
    return min([node.lineno] + [d.lineno for d in decos])


def _node_name(node: ast.AST) -> str:
    if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
        return node.name
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        return "<imports>"
    if isinstance(node, (ast.Assign, ast.AnnAssign)):
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        return ",".join(ast.unparse(t) for t in targets)
    if isinstance(node, ast.Expr) and isinstance(getattr(node, "value", None), ast.Constant):
        return "<docstring>"
    return f"<{type(node).__name__.lower()}>"


def _units(body: list[ast.stmt], first_line: int, last_line: int) -> list[Unit]:
    """Turn statements into units that together cover every line in the range.

    Lines between two statements (comments, blank lines) are attached to the
    following statement; trailing lines go to the last one.
    """
    units: list[Unit] = []
    prev_end = first_line - 1
    for node in body:
        units.append(Unit(prev_end + 1, node.end_lineno, _node_name(node), node))
        prev_end = node.end_lineno
    if units:
        units[-1].end = max(units[-1].end, last_line)
    return units


def _slice(lines: list[str], start: int, end: int) -> str:
    return "\n".join(lines[start - 1:end]).strip("\n")


class FileChunker:
    def __init__(self, rel_path: str, source: str):
        self.rel = rel_path
        self.lines = source.splitlines()
        self.tree = ast.parse(source)
        self.chunks: list[Chunk] = []

    def tok(self, start: int, end: int) -> int:
        return count_tokens(_slice(self.lines, start, end))

    def emit(self, kind: str, names: list[str], start: int, end: int,
             class_name: str | None = None, prefix: str = "") -> None:
        code = _slice(self.lines, start, end)
        if not code.strip():
            return
        names = list(dict.fromkeys(names))  # dedupe, keep order
        if prefix:
            code = prefix + "\n    # ...\n" + code
        header = f"# file: {self.rel} (lines {start}-{end})"
        if class_name:
            header += f"\n# class: {class_name}"
        text = header + "\n" + code
        self.chunks.append(Chunk(
            id=f"{self.rel}::{len(self.chunks):03d}", file=self.rel, kind=kind,
            names=names, class_name=class_name, start_line=start, end_line=end,
            n_tokens=count_tokens(text), header=header, code=code, text=text))

    # -- grouping -----------------------------------------------------------
    def group(self, units: list[Unit], budget: int) -> list[list[Unit]]:
        """Greedily merge consecutive units while the group stays within budget."""
        groups: list[list[Unit]] = []
        cur: list[Unit] = []
        for u in units:
            if cur and self.tok(cur[0].start, u.end) > budget:
                groups.append(cur)
                cur = []
            cur.append(u)
        if cur:
            groups.append(cur)
        return self.merge_small(groups)

    def merge_small(self, groups: list[list[Unit]]) -> list[list[Unit]]:
        """Fold groups below MIN_TOKENS (lone imports, `if __name__` tails, short
        last parts) into a neighbour, as long as the result stays within MAX_TOKENS."""
        i = 0
        while i < len(groups) and len(groups) > 1:
            g = groups[i]
            if self.tok(g[0].start, g[-1].end) >= MIN_TOKENS:
                i += 1
                continue
            prev_ok = i > 0 and self.tok(groups[i - 1][0].start, g[-1].end) <= MAX_TOKENS
            next_ok = i + 1 < len(groups) and self.tok(g[0].start, groups[i + 1][-1].end) <= MAX_TOKENS
            if prev_ok:
                groups[i - 1] += groups.pop(i)
            elif next_ok:
                groups[i + 1] = g + groups[i + 1]
                groups.pop(i)
            else:
                i += 1
        return groups

    def split_lines(self, kind, name, start, end, class_name=None, prefix=""):
        """Last-resort split of one oversized unit into line windows."""
        s = start
        while s <= end:
            e = s
            while e < end and self.tok(s, e + 1) <= TARGET_TOKENS:
                e += 1
            self.emit(kind, [name], s, e, class_name, prefix)
            s = e + 1

    # -- main -----------------------------------------------------------------
    def run(self) -> list[Chunk]:
        if not self.lines:
            return []
        units = _units(self.tree.body, 1, len(self.lines))
        for grp in self.group(units, TARGET_TOKENS):
            start, end = grp[0].start, grp[-1].end
            if len(grp) == 1 and self.tok(start, end) > MAX_TOKENS:
                self.split_large(grp[0])
                continue
            only_classes = all(isinstance(u.node, ast.ClassDef) for u in grp)
            kind = "class" if only_classes else "module"
            cls = grp[0].name if (only_classes and len(grp) == 1) else None
            self.emit(kind, [u.name for u in grp], start, end, cls)
        return self.chunks

    def split_large(self, unit: Unit) -> None:
        node = unit.node
        if not isinstance(node, ast.ClassDef):
            self.split_lines("module", unit.name, unit.start, unit.end)
            return
        # class header = everything before the first method (signature, docstring, fields)
        first_def = next((n for n in node.body
                          if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))), None)
        head_end = (_node_start(first_def) - 1) if first_def else node.body[0].lineno
        prefix = _slice(self.lines, unit.start, head_end)
        body = [n for n in node.body if _node_start(n) > head_end]
        members = _units(body, head_end + 1, unit.end)
        budget = max(TARGET_TOKENS - count_tokens(prefix), 150)
        for grp in self.group(members, budget):
            start, end = grp[0].start, grp[-1].end
            if len(grp) == 1 and self.tok(start, end) > MAX_TOKENS:
                self.split_lines("class_part", grp[0].name, start, end, node.name, prefix)
            else:
                self.emit("class_part", [u.name for u in grp], start, end, node.name, prefix)


def chunk_repo(repo: Path) -> list[Chunk]:
    chunks: list[Chunk] = []
    for path in sorted(repo.rglob("*.py")):
        if any(part.startswith(".") for part in path.relative_to(repo).parts):
            continue
        rel = path.relative_to(repo).as_posix()
        chunks.extend(FileChunker(rel, path.read_text(encoding="utf-8")).run())
    return chunks


def main() -> None:
    repo = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_REPO
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    chunks = chunk_repo(repo)
    out.write_text(json.dumps([asdict(c) for c in chunks], indent=2, ensure_ascii=False),
                   encoding="utf-8")
    sizes = sorted(c.n_tokens for c in chunks)
    print(f"{len(chunks)} chunks -> {out}")
    print(f"tokens: total={sum(sizes)} min={sizes[0]} median={sizes[len(sizes)//2]} max={sizes[-1]}")


if __name__ == "__main__":
    main()
