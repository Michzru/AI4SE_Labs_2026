#!/usr/bin/env python3
"""Task 2 runner: text-to-SQL on the restaurants dataset with 3 prompting frameworks.

Calls the `claude` CLI (no Anthropic API key needed) once per (question, prompt),
each call being a fresh, stateless session. Measures wall-clock time, API time,
time-to-first-token and token usage, executes the predicted SQL against the
database, compares with the labels, and writes predictions, a summary, a chart
and a markdown report to ./output/.

Usage (from the Task_2 folder):
    .venv/bin/python run_task2.py --limit 3                 # smoke test: 3 questions x 3 prompts
    .venv/bin/python run_task2.py                           # full run, Sonnet 5.5 (resumable) -> output/sonnet-5.5/
    .venv/bin/python run_task2.py --model opus              # full run, Opus 5.5 -> output/opus-5.5/
    .venv/bin/python run_task2.py --model opus --report-only  # rebuild summary/chart/report from saved raw results
"""
import argparse
import csv
import json
import re
import sqlite3
import statistics
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "data"
OUT_DIR = HERE / "output" / "sonnet-5.5"  # overridden by --model
PROMPTS_PATH = HERE.parent / "Task_1" / "prompts.json"
LABELS_PATH = DATA_DIR / "restaurants_dataset.csv"
SCHEMA_PATH = DATA_DIR / "restaurants-schema.csv"

sys.path.insert(0, str(DATA_DIR))
import evaluate_retrieval_predictions as ev  # noqa: E402  (reuses its DB loader)

MODELS = {  # --model choice -> (model id, label, output sub-folder)
    "sonnet": ("claude-sonnet-5-5", "Sonnet 5.5", "sonnet-5.5"),
    "opus": ("claude-opus-5-5", "Opus 5.5", "opus-5.5"),
}
MODEL, MODEL_LABEL, _ = MODELS["sonnet"]
EFFORT = "medium"
SYSTEM_PROMPT = "You are an expert SQL assistant. Follow the user's output instructions exactly."
TIMEOUT_S = 240
RETRIES = 2

_lock = threading.Lock()


# ----------------------------------------------------------------- data loading
def load_prompts():
    prompts = json.loads(PROMPTS_PATH.read_text(encoding="utf-8"))
    schema = SCHEMA_PATH.read_text(encoding="utf-8").strip()
    for p in prompts:
        p["short"] = p["framework"].split(" ")[0]  # ICIO / Few-Shot / CoT
    return prompts, schema


def load_labels():
    csv.field_size_limit(1_000_000_000)
    with LABELS_PATH.open(encoding="utf-8", newline="") as f:
        return [(r["question"], json.loads(r["result"])) for r in csv.DictReader(f)]


def fewshot_questions(prompts):
    """Questions that appear as worked examples in the Few-Shot prompt (leakage)."""
    out = set()
    for p in prompts:
        if "few-shot" in p["framework"].lower():
            out |= {q.strip() for q in re.findall(r"^Question: (.*?)\nSQL:", p["template"], re.M)}
    return out


# ----------------------------------------------------------------- calling claude
def extract_sql(text):
    text = text.strip()
    marks = list(re.finditer(r"^\s*SQL:\s*", text, re.M))
    if marks:
        text = text[marks[-1].end():]
    fence = re.search(r"```(?:sql)?\s*(.*?)```", text, re.S | re.I)
    if fence:
        text = fence.group(1)
    text = text.strip().strip("`").strip()
    return text


def call_claude(prompt_text, workdir):
    cmd = [
        "claude", "-p", prompt_text,
        "--model", MODEL, "--effort", EFFORT,
        "--output-format", "json",
        "--no-session-persistence",          # fresh, stateless session per call
        "--tools", "",                       # no tools: pure text answer
        "--setting-sources", "",             # ignore user/project settings, CLAUDE.md, hooks
        "--system-prompt", SYSTEM_PROMPT,
    ]
    last_err = ""
    for attempt in range(RETRIES + 1):
        t0 = time.perf_counter()
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT_S, cwd=workdir)
            wall = time.perf_counter() - t0
            data = json.loads(proc.stdout[proc.stdout.index("{"):proc.stdout.rindex("}") + 1])
            if proc.returncode == 0 and not data.get("is_error"):
                return wall, data, attempt
            last_err = (data.get("result") or proc.stderr)[:300]
            if "reasoning_extraction" in last_err or "usage policy" in last_err.lower():
                break  # policy block: retrying the same prompt is pointless
        except Exception as e:  # timeout, bad JSON, missing CLI ...
            wall = time.perf_counter() - t0
            last_err = f"{type(e).__name__}: {e}"[:300]
        time.sleep(2 * (attempt + 1))
    return wall, {"error": last_err}, attempt


def run_one(prompt, schema, idx, question, workdir):
    text = prompt["template"].replace("{{SCHEMA}}", schema).replace("{{QUESTION}}", question)
    wall, data, retries = call_claude(text, workdir)
    rec = {"row": idx, "question": question, "prompt_id": prompt["prompt_id"],
           "framework": prompt["short"], "model": MODEL, "effort": EFFORT,
           "wall_s": round(wall, 3), "retries": retries}
    if "error" in data:
        rec.update(error=data["error"], raw_output="", predicted_sql="")
        return rec
    u = data.get("usage", {})
    raw = data.get("result", "")
    rec.update(
        raw_output=raw, predicted_sql=extract_sql(raw),
        api_ms=data.get("duration_api_ms"), ttft_ms=data.get("ttft_ms"),
        input_tokens=u.get("input_tokens", 0),
        cache_creation_tokens=u.get("cache_creation_input_tokens", 0),
        cache_read_tokens=u.get("cache_read_input_tokens", 0),
        output_tokens=u.get("output_tokens", 0),
        thinking_tokens=(u.get("output_tokens_details") or {}).get("thinking_tokens", 0),
        cost_usd=data.get("total_cost_usd", 0.0),
    )
    return rec


# ----------------------------------------------------------------- main run
def raw_path(prompt_id):
    return OUT_DIR / f"raw_{prompt_id}.jsonl"


def load_raw(prompt_id):
    p = raw_path(prompt_id)
    recs = {}
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                if not r.get("error"):
                    recs[r["row"]] = r
    return recs


def run_all(prompts, schema, labels, limit, workers, only):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    selected = [p for p in prompts if not only or p["prompt_id"] in only or p["short"].lower() in only]
    n = len(labels) if not limit else min(limit, len(labels))
    done = {p["prompt_id"]: load_raw(p["prompt_id"]) for p in selected}
    # interleave prompts per question so time-of-day effects hit all prompts equally
    jobs = [(p, i) for i in range(n) for p in selected if i not in done[p["prompt_id"]]]
    print(f"{len(jobs)} calls to make ({n} questions x {len(selected)} prompts, "
          f"{sum(len(v) for v in done.values())} already done), workers={workers}")
    workdir = tempfile.mkdtemp(prefix="task2_")
    finished = 0
    t_start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(run_one, p, schema, i, labels[i][0], workdir): (p, i) for p, i in jobs}
        for fut in as_completed(futs):
            rec = fut.result()
            with _lock:
                with raw_path(rec["prompt_id"]).open("a", encoding="utf-8") as f:
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                finished += 1
                tag = "ERR" if rec.get("error") else f'{rec["wall_s"]:.1f}s'
                if finished % 10 == 0 or rec.get("error") or finished == len(jobs):
                    el = time.perf_counter() - t_start
                    print(f"[{finished}/{len(jobs)}] {rec['framework']:<8} row {rec['row']:>3} {tag}  "
                          f"elapsed {el/60:.1f} min", flush=True)
    return selected, n


# ----------------------------------------------------------------- evaluation
def evaluate(prompts, labels, n, leak):
    conn = ev.load_database()
    results = {}
    for p in prompts:
        recs = load_raw(p["prompt_id"])
        rows = []
        for i in range(n):
            r = recs.get(i)
            if r is None:
                continue
            label = labels[i][1]
            status, ok = "wrong", False
            try:
                pred = conn.execute(r["predicted_sql"]).fetchall()
                ok = ev.row_multiset(pred) == ev.row_multiset(label)
                status = "correct" if ok else "wrong"
            except (sqlite3.Error, ValueError) as e:
                status = "invalid_sql"
            r = dict(r, correct=ok, status=status, leaked=labels[i][0].strip() in leak,
                     expected=json.dumps(label, ensure_ascii=False))
            rows.append(r)
        results[p["prompt_id"]] = rows
    conn.close()
    return results


def pct(values, q):
    v = sorted(values)
    return v[min(len(v) - 1, int(round(q * (len(v) - 1))))] if v else float("nan")


def summarize(prompts, results):
    summary = []
    for p in prompts:
        rows = results[p["prompt_id"]]
        if not rows:
            continue
        clean = [r for r in rows if not r["leaked"]]
        wall = [r["wall_s"] for r in rows]
        s = {
            "prompt_id": p["prompt_id"], "framework": p["short"], "model": MODEL_LABEL, "effort": EFFORT,
            "n": len(rows),
            "accuracy": sum(r["correct"] for r in rows) / len(rows),
            "accuracy_excl_fewshot_examples": (sum(r["correct"] for r in clean) / len(clean)) if clean else None,
            "n_excl": len(clean),
            "invalid_sql": sum(r["status"] == "invalid_sql" for r in rows),
            "wall_mean_s": statistics.mean(wall), "wall_median_s": statistics.median(wall),
            "wall_p95_s": pct(wall, 0.95), "wall_total_min": sum(wall) / 60,
            "api_mean_s": statistics.mean(r["api_ms"] for r in rows if r.get("api_ms") is not None) / 1000,
            "ttft_mean_s": statistics.mean(r["ttft_ms"] for r in rows if r.get("ttft_ms") is not None) / 1000,
            "output_tokens_mean": statistics.mean(r["output_tokens"] for r in rows),
            "output_tokens_total": sum(r["output_tokens"] for r in rows),
            "input_tokens_total": sum(r["input_tokens"] for r in rows),
            "cache_creation_total": sum(r["cache_creation_tokens"] for r in rows),
            "cache_read_total": sum(r["cache_read_tokens"] for r in rows),
            "prompt_tokens_mean": statistics.mean(
                r["input_tokens"] + r["cache_creation_tokens"] + r["cache_read_tokens"] for r in rows),
            "cost_total_usd": sum(r["cost_usd"] for r in rows),
            "cost_per_q_usd": statistics.mean(r["cost_usd"] for r in rows),
        }
        summary.append(s)
    return summary


# ----------------------------------------------------------------- outputs
def write_outputs(prompts, results, summary):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = ["question", "predicted_sql", "model", "effort", "prompt_id", "framework", "wall_s", "api_ms", "ttft_ms",
            "input_tokens", "cache_creation_tokens", "cache_read_tokens", "output_tokens", "cost_usd",
            "status", "correct", "leaked"]
    for p in prompts:
        rows = results[p["prompt_id"]]
        with (OUT_DIR / f"predictions_{p['prompt_id']}.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=meta, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
    (OUT_DIR / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    with (OUT_DIR / "summary.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0]))
        w.writeheader()
        w.writerows(summary)


def make_chart(summary):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed -> chart skipped (pip install matplotlib)")
        return False
    names = [s["framework"] for s in summary]
    colors = ["#4C78A8", "#F58518", "#54A24B", "#B279A2"][: len(names)]
    fig, ax = plt.subplots(2, 3, figsize=(15, 8.5))
    ax = ax.ravel()

    def bars(a, vals, title, ylabel, fmt="{:.2f}", ylim=None):
        b = a.bar(names, vals, color=colors)
        a.set_title(title, fontsize=11, fontweight="bold")
        a.set_ylabel(ylabel)
        if ylim:
            a.set_ylim(*ylim)
        for rect, v in zip(b, vals):
            a.annotate(fmt.format(v), (rect.get_x() + rect.get_width() / 2, rect.get_height()),
                       ha="center", va="bottom", fontsize=9)
        a.spines[["top", "right"]].set_visible(False)

    bars(ax[0], [s["accuracy"] * 100 for s in summary], "Accuracy (all questions)", "% correct", "{:.1f}%", (0, 105))
    bars(ax[1], [(s["accuracy_excl_fewshot_examples"] or 0) * 100 for s in summary],
         "Accuracy (excl. few-shot example questions)", "% correct", "{:.1f}%", (0, 105))
    bars(ax[2], [s["invalid_sql"] for s in summary], "Invalid SQL (does not execute)", "count", "{:.0f}")
    bars(ax[3], [s["wall_mean_s"] for s in summary], "Mean inference time per question (wall clock)", "seconds", "{:.2f}s")
    bars(ax[4], [s["output_tokens_mean"] for s in summary], "Mean output tokens per question", "tokens", "{:.0f}")
    bars(ax[5], [s["cost_per_q_usd"] * 1000 for s in summary], "Mean cost per question (reported by CLI)", "milli-USD", "{:.2f}")
    fig.suptitle(f"Text-to-SQL on restaurants DB - {MODEL_LABEL}, effort {EFFORT}", fontsize=13, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "comparison.png", dpi=150)
    return True


def write_report(summary, results, chart_ok):
    L = [f"# Task 2 report - prompt comparison on text-to-SQL ({MODEL_LABEL}, effort {EFFORT})", ""]
    L += ["Each question was sent as an independent, stateless `claude -p` call (new session, no tools, no settings/"
          "CLAUDE.md). Time = wall clock of the whole CLI call; API time and time-to-first-token are as reported by the CLI. "
          "Correctness = executing the predicted SQL on the database and comparing the row multiset with the label "
          "(same rule as `evaluate_retrieval_predictions.py`); SQL that fails to execute counts as wrong.", ""]
    L += ["| Prompt | n | Accuracy | Acc. excl. few-shot ex. | Invalid SQL | Mean time | Median | P95 | Mean API time | Mean out tokens | Mean prompt tokens | Total cost |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in summary:
        ae = s["accuracy_excl_fewshot_examples"]
        L.append(f"| {s['framework']} | {s['n']} | {s['accuracy']:.1%} | {ae:.1%} (n={s['n_excl']}) | {s['invalid_sql']} | "
                 f"{s['wall_mean_s']:.2f}s | {s['wall_median_s']:.2f}s | {s['wall_p95_s']:.2f}s | {s['api_mean_s']:.2f}s | "
                 f"{s['output_tokens_mean']:.0f} | {s['prompt_tokens_mean']:.0f} | ${s['cost_total_usd']:.2f} |")
    L.append("")
    if chart_ok:
        L += ["![comparison](comparison.png)", ""]
    best = max(summary, key=lambda s: s["accuracy"])
    fast = min(summary, key=lambda s: s["wall_mean_s"])
    L += ["## Findings", "",
          f"- Most accurate: **{best['framework']}** ({best['accuracy']:.1%}).",
          f"- Fastest: **{fast['framework']}** ({fast['wall_mean_s']:.2f}s mean per question).", ""]
    # failure breakdown
    L += ["## Where prompts disagree", ""]
    ids = list(results)
    if len(ids) > 1:
        by_row = {}
        for pid, rows in results.items():
            for r in rows:
                by_row.setdefault(r["row"], {})[pid] = r
        all_ok = sum(all(v["correct"] for v in d.values()) and len(d) == len(ids) for d in by_row.values())
        none_ok = sum(not any(v["correct"] for v in d.values()) and len(d) == len(ids) for d in by_row.values())
        L += [f"- Questions solved by all prompts: {all_ok}; solved by none: {none_ok}.", ""]
        wrong = [(i, d) for i, d in by_row.items() if not all(v["correct"] for v in d.values())][:8]
        for i, d in wrong:
            q = next(iter(d.values()))["question"]
            L.append(f"- row {i}: _{q[:110]}_ -> " + ", ".join(f"{v['framework']}: {v['status']}" for v in d.values()))
    L += ["", "_Add your own interpretation here (why a prompt failed, error categories, trade-off accuracy vs. time/tokens)._", ""]
    (OUT_DIR / "report.md").write_text("\n".join(L), encoding="utf-8")


# ----------------------------------------------------------------- cli
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=0, help="only the first N questions (smoke test)")
    ap.add_argument("--workers", type=int, default=4, help="parallel claude calls (1 = cleanest timings)")
    ap.add_argument("--only", nargs="*", default=[], help="subset: prompt_a prompt_b prompt_c or icio few-shot cot")
    ap.add_argument("--report-only", action="store_true", help="skip calls, rebuild outputs from raw_*.jsonl")
    ap.add_argument("--model", choices=list(MODELS), default="sonnet", help="model to run (output/<model>/)")
    ap.add_argument("--effort", default="medium", help="effort level passed to the CLI")
    args = ap.parse_args()

    global MODEL, MODEL_LABEL, EFFORT, OUT_DIR
    MODEL, MODEL_LABEL, sub = MODELS[args.model]
    EFFORT = args.effort
    OUT_DIR = HERE / "output" / sub

    prompts, schema = load_prompts()
    labels = load_labels()
    leak = fewshot_questions(prompts)
    only = {o.lower() for o in args.only}
    if args.report_only:
        selected, n = [p for p in prompts if not only or p["prompt_id"] in only or p["short"].lower() in only], \
            (min(args.limit, len(labels)) if args.limit else len(labels))
    else:
        selected, n = run_all(prompts, schema, labels, args.limit, args.workers, only)
    results = evaluate(selected, labels, n, leak)
    summary = summarize(selected, results)
    if not summary:
        sys.exit("No results found.")
    write_outputs(selected, results, summary)
    chart_ok = make_chart(summary)
    write_report(summary, results, chart_ok)
    print("\n" + "=" * 70)
    for s in summary:
        print(f"{s['framework']:<9} acc {s['accuracy']:.1%} (excl. few-shot ex. {s['accuracy_excl_fewshot_examples']:.1%})  "
              f"invalid {s['invalid_sql']}  mean {s['wall_mean_s']:.2f}s  out-tok {s['output_tokens_mean']:.0f}  "
              f"cost ${s['cost_total_usd']:.2f}")
    print(f"\nOutputs in {OUT_DIR}")


if __name__ == "__main__":
    main()
