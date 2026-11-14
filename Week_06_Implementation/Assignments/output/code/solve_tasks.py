"""Task 5 – solve the coding tasks from missing_code.json with the RAG pipeline.

    solve(task_text) : top-5 chunks (Task 4) -> prompt -> LLM -> method source
    write_method(...) : replace the stub `def` in the target file (AST-located)

Run:
    python solve_tasks.py                                   # gpt-5-mini, default store, leaves code written
    python solve_tasks.py --gen-model gpt-5-nano --summary-model gpt-5-nano
    python solve_tasks.py --reset                           # restore original stub files

Every run starts from the original files (backup_original/). Results (prompt context,
generated code, test outcome) are written to results/run_<gen>__sum-<summary>__<i>.json.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import shutil
import subprocess
import sys
import textwrap
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from embed_chunks import SUMMARY_MODEL, store_paths
from llm import chat
from retrieve import search

HERE = Path(__file__).resolve().parent
REPO = HERE.parent / "week6" / "AI4SE_Playground"
PKG_ROOT = REPO / "playground"                 # contains playground/ and tests/
TASKS_FILE = HERE.parent.parent / "missing_code.json"
BACKUP = HERE / "backup_original"
RESULTS = HERE / "results"
TEST_MAP = RESULTS / "test_map.json"

TOP_K = 5
GEN_MODEL = "gpt-5-mini"

SYSTEM_PROMPT = """You are an expert Python developer implementing one missing method in an existing codebase.
The method currently exists only as a stub whose body is `pass`.
You get the task and code chunks retrieved from the repository (the class with the stub, related classes, unit tests).

Rules:
- Return ONLY the complete method definition (the `def` line and its body) in a single ```python code block.
- Keep the exact name, parameters, type hints and return type of the stub.
- Do not include the class statement, decorators, imports or any explanation.
- Use only names that already exist in the shown code or Python builtins; do not add imports.
- Follow the behaviour required by the docstring and by the unit tests shown in the context
  (exact return types, raised exception types and messages, laziness of generators, etc.)."""


# ---------------------------------------------------------------- tasks / prompt
def load_tasks() -> list[dict]:
    return json.loads(TASKS_FILE.read_text(encoding="utf-8"))


def clean_docstring(task: dict) -> str:
    return task["docstring"].strip().strip('"').strip()


def task_text(task: dict) -> str:
    """Textual task = what the RAG gets as input (format validated in Task 3/4)."""
    return (f"Implement method {task['method']} of class {task['class']} in {task['file']}. "
            f"{clean_docstring(task)}")


def build_prompt(text: str, retrieved: list[tuple[dict, float]]) -> str:
    parts = [f"## Task\n{text}\n", f"## Retrieved repository context (top {len(retrieved)})"]
    for i, (chunk, score) in enumerate(retrieved, 1):
        parts.append(f"### Chunk {i} (similarity {score:.3f})\n```python\n{chunk['text']}\n```")
    return "\n\n".join(parts)


def solve(text: str, gen_model: str = GEN_MODEL, store_path: Path | None = None) -> dict:
    """RAG step: textual task -> top-5 chunks -> LLM -> raw answer."""
    store_path = store_path or store_paths()[1]
    retrieved = search(text, TOP_K, store_path)
    prompt = build_prompt(text, retrieved)
    answer = chat(gen_model, SYSTEM_PROMPT, prompt)
    answer["retrieved"] = [{"id": c["id"], "score": round(s, 4)} for c, s in retrieved]
    answer["prompt_chars"] = len(prompt)
    return answer


# ---------------------------------------------------------------- code extraction / writing
def extract_method(answer: str, method: str) -> ast.FunctionDef:
    """Find `def method` in the LLM answer (code block preferred, nested in a class allowed)."""
    blocks = re.findall(r"```(?:python|py)?\s*\n(.*?)```", answer, re.S) or [answer]
    for block in blocks:
        try:
            tree = ast.parse(textwrap.dedent(block))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == method:
                node.source = textwrap.dedent(block)  # type: ignore[attr-defined]
                return node
    raise ValueError(f"no parsable `def {method}` in answer")


def method_source(fn: ast.FunctionDef, docstring: str, indent: str) -> list[str]:
    """Source of fn without decorators, re-indented, with the task docstring if missing."""
    lines = fn.source.splitlines()  # type: ignore[attr-defined]
    seg = textwrap.dedent("\n".join(lines[fn.lineno - 1:fn.end_lineno])).splitlines()
    has_doc = isinstance(fn.body[0], ast.Expr) and isinstance(getattr(fn.body[0], "value", None), ast.Constant) \
        and isinstance(fn.body[0].value.value, str)
    body_line = fn.body[0].lineno - fn.lineno  # index of first body stmt inside seg (0 = one-liner)
    if not has_doc and body_line > 0:
        body_indent = re.match(r"\s*", seg[body_line]).group(0)
        seg.insert(body_line, body_indent + docstring)
    return [indent + line if line.strip() else "" for line in seg]


def find_stub(tree: ast.Module, cls: str, method: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == cls:
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and item.name == method:
                    return item
    raise LookupError(f"{cls}.{method} not found")


def write_method(task: dict, answer: str) -> None:
    """Replace the method (def line .. end, decorators kept) in the target file."""
    path = REPO / task["file"]
    src = path.read_text(encoding="utf-8")
    lines = src.splitlines()
    stub = find_stub(ast.parse(src), task["class"], task["method"])
    indent = " " * stub.col_offset
    new = method_source(extract_method(answer, task["method"]), '"""' + clean_docstring(task) + '"""', indent)
    out = lines[:stub.lineno - 1] + new + lines[stub.end_lineno:]
    new_src = "\n".join(out) + "\n"
    ast.parse(new_src)  # raises SyntaxError -> caller keeps the original
    path.write_text(new_src, encoding="utf-8")


# ---------------------------------------------------------------- backup / tests
def target_files() -> list[str]:
    return sorted({t["file"] for t in load_tasks()})


def ensure_backup() -> None:
    for rel in target_files():
        dst = BACKUP / rel
        if not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / rel, dst)


def reset() -> None:
    ensure_backup()
    for rel in target_files():
        shutil.copy2(BACKUP / rel, REPO / rel)


def run_tests() -> dict:
    proc = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", "."],
                          cwd=PKG_ROOT, capture_output=True, text=True)
    out = proc.stderr
    ran = int(re.search(r"Ran (\d+) test", out).group(1)) if "Ran " in out else 0
    failing = sorted(set(m.group(1) for m in
                         re.finditer(r"^(?:FAIL|ERROR): \w+ \(([\w.]+)\)", out, re.M)))
    import_error = ran == 0 or "ImportError" in out and ran < 10
    return {"ran": ran, "failed": len(failing), "passed": ran - len(failing),
            "failing": failing, "import_error": import_error, "raw_tail": out[-600:] if import_error else ""}


def build_test_map() -> dict[str, list[str]]:
    """Attribute tests to tasks: every stub raises a marker, failing tests reveal which stub they hit."""
    if TEST_MAP.exists():
        return json.loads(TEST_MAP.read_text())
    reset()
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        write_method(t, f"```python\ndef {t['method']}(self, *a, **k):\n"
                        f"    raise NotImplementedError('TASK_{i}')\n```")
    proc = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", "."],
                          cwd=PKG_ROOT, capture_output=True, text=True)
    reset()
    mapping: dict[str, list[str]] = {f"{t['class']}.{t['method']}": [] for t in tasks}
    for block in re.split(r"^={50,}$", proc.stderr, flags=re.M):
        m = re.search(r"^(?:FAIL|ERROR): (\w+) \(([\w.]+)\)", block, re.M)
        hits = set(re.findall(r"TASK_(\d+)", block))
        if m:
            for h in hits:
                t = tasks[int(h)]
                mapping[f"{t['class']}.{t['method']}"].append(m.group(2))
    RESULTS.mkdir(exist_ok=True)
    TEST_MAP.write_text(json.dumps(mapping, indent=2))
    return mapping


# ---------------------------------------------------------------- one full run
def generate(gen_model: str, summary_model: str) -> list[dict]:
    """LLM calls for all tasks in parallel (writing happens afterwards, sequentially)."""
    store = store_paths(summary_model)[1]
    tasks = load_tasks()
    with ThreadPoolExecutor(max_workers=10) as pool:
        answers = list(pool.map(lambda t: solve(task_text(t), gen_model, store), tasks))
    for t, a in zip(tasks, answers):
        a["task"] = f"{t['class']}.{t['method']}"
        a["file"] = t["file"]
    return answers


def apply_and_test(answers: list[dict], test_map: dict[str, list[str]], baseline: dict) -> dict:
    reset()
    tasks = load_tasks()
    for t, a in zip(tasks, answers):
        try:
            write_method(t, a["text"])
            a["written"], a["write_error"] = True, None
        except (ValueError, SyntaxError, LookupError) as e:
            a["written"], a["write_error"] = False, f"{type(e).__name__}: {e}"
    tests = run_tests()
    failing = set(tests["failing"])
    for a in answers:
        own = test_map.get(a["task"], [])
        a["tests_total"] = len(own)
        a["tests_passed"] = sum(tid not in failing for tid in own) if not tests["import_error"] else 0
        a["solved"] = a["written"] and a["tests_passed"] == a["tests_total"] and not tests["import_error"]
    newly_broken = sorted(failing - set(baseline["failing"]))
    task_tests = {tid for v in test_map.values() for tid in v}
    return {"tests": tests, "newly_broken": newly_broken,
            "broken_outside_task_tests": [t for t in newly_broken if t not in task_tests],
            "tasks_solved": sum(a["solved"] for a in answers), "answers": answers}


def run(gen_model: str, summary_model: str, tag: str = "0", keep: bool = False) -> dict:
    ensure_backup()
    test_map = build_test_map()
    reset()
    baseline = run_tests()
    answers = generate(gen_model, summary_model)
    result = apply_and_test(answers, test_map, baseline)
    result.update({"gen_model": gen_model, "summary_model": summary_model,
                   "baseline": {k: baseline[k] for k in ("ran", "failed", "passed")},
                   "prompt_tokens": sum(a["prompt_tokens"] for a in answers),
                   "completion_tokens": sum(a["completion_tokens"] for a in answers)})
    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / f"run_{gen_model}__sum-{summary_model}__{tag}.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    if not keep:
        reset()
    t = result["tests"]
    print(f"{gen_model:13s} sum={summary_model:13s} #{tag}: tasks {result['tasks_solved']}/10 | "
          f"tests {t['passed']}/{t['ran']} passed (baseline {baseline['passed']}) | "
          f"broken outside task tests {len(result['broken_outside_task_tests'])} | -> {out.name}")
    return result


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen-model", default=GEN_MODEL)
    ap.add_argument("--summary-model", default=SUMMARY_MODEL)
    ap.add_argument("--tag", default="main")
    ap.add_argument("--reset", action="store_true", help="restore original stub files and exit")
    args = ap.parse_args()
    if args.reset:
        reset()
        print("restored original files from", BACKUP)
    else:
        run(args.gen_model, args.summary_model, args.tag, keep=True)
