#!/usr/bin/env python3
"""Task 3: extra metrics for the text-to-SQL predictions produced in Task 2.

No model calls are made. The saved predictions
(Task_2/output/<model>/predictions_prompt_*.csv) are re-executed on the database
and compared with the labels.

Metrics
  A  Efficiency      cost / billed tokens / time per CORRECT answer (cost-effectiveness)
  B  Row F1          partial credit: F1 between predicted and expected result rows
                     (multiset based, so duplicate rows count) + exact match rate
  C  Noise robustness accuracy on questions with a distractor sentence vs clean ones
  +  Bootstrap 95% confidence intervals for accuracy and F1 (resampling questions)

Run from the Task_3 folder:   ../Task_2/.venv/bin/python metrics.py
"""
import csv
import json
import random
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
T2 = HERE.parent / "Task_2"
OUT = HERE / "output"
sys.path.insert(0, str(T2 / "data"))
import evaluate_retrieval_predictions as ev  # noqa: E402

csv.field_size_limit(10**9)

PROMPTS = [("prompt_a", "ICIO"), ("prompt_b", "Few-Shot"), ("prompt_c", "CoT")]
MODELS = [("Sonnet 5.5", "sonnet-5.5"), ("Opus 5.5", "opus-5.5")]  # (label, Task_2/output sub-folder)
COLORS = {"ICIO": "#4C78A8", "Few-Shot": "#F58518", "CoT": "#54A24B"}

# Distractor sentences in the dataset talk about food comparisons, picnics, etc.
NOISE_KEYWORDS = [
    "picnic", "pancake", "dumpling", "imaginary", "fictional", "hypothetical", "unrelated", "umbrella",
    "lunchbox", "flowerpot", "stuffed animal", "moon", "journey", "feast", "voyage", "muffin", "cracker",
    "debate", "torn between", "weighing", "comparing", "cannot decide", "not settled", "still cannot",
    "wonder", "puzzle", "dilemma", "choosing between", "curry", "apple pie", "soup", "snack", "omelet",
    "biscuit", "deciding whether", "cereal", "better hat", "cannot choose", "separate food note", "taco or",
]


def is_noisy(question):
    q = question.lower()
    return any(k in q for k in NOISE_KEYWORDS)


def row_f1(pred_rows, exp_rows):
    """Multiset F1 of result rows. Both empty -> 1.0 (correctly returned nothing)."""
    p, e = Counter(map(tuple, pred_rows)), Counter(map(tuple, exp_rows))
    if not p and not e:
        return 1.0, 1.0, 1.0
    overlap = sum((p & e).values())
    prec = overlap / sum(p.values()) if p else 0.0
    rec = overlap / sum(e.values()) if e else 0.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    return f1, prec, rec


def complete(path, n=155):
    """A model is used only when its predictions cover every question."""
    if not path.exists():
        return False
    with path.open(encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f)) == n


def available_models():
    out = []
    for lab, sub in MODELS:
        if all(complete(T2 / "output" / sub / f"predictions_{pid}.csv") for pid, _ in PROMPTS):
            out.append((lab, sub))
        else:
            print(f"skipping {lab}: predictions missing or incomplete")
    return out


def load():
    with (T2 / "data" / "restaurants_dataset.csv").open(encoding="utf-8", newline="") as f:
        labels = [(r["question"], json.loads(r["result"])) for r in csv.DictReader(f)]
    conn = ev.load_database()
    data = {}
    for model, sub in available_models():
        for pid, name in PROMPTS:
            with (T2 / "output" / sub / f"predictions_{pid}.csv").open(encoding="utf-8", newline="") as f:
                preds = list(csv.DictReader(f))
            assert len(preds) == len(labels), (model, pid, len(preds), len(labels))
            rows = []
            for (q, exp), r in zip(labels, preds):
                assert r["question"] == q
                try:
                    got = [list(x) for x in conn.execute(r["predicted_sql"]).fetchall()]
                    valid = True
                except Exception:
                    got, valid = [], False
                f1, prec, rec = row_f1(got, exp)
                billed = (int(r["input_tokens"]) + int(r["cache_creation_tokens"])
                          + int(r["cache_read_tokens"]) + int(r["output_tokens"]))
                rows.append({
                    "question": q, "noisy": is_noisy(q), "valid": valid,
                    "exact": ev.row_multiset(got) == ev.row_multiset(exp),
                    "f1": f1, "precision": prec, "recall": rec,
                    "n_expected": len(exp), "n_predicted": len(got),
                    "cost": float(r["cost_usd"]), "billed_tokens": billed,
                    "output_tokens": int(r["output_tokens"]), "wall_s": float(r["wall_s"]),
                })
            data[(model, name)] = rows
    return data


def bootstrap_ci(values, n=5000, seed=1):
    rng = random.Random(seed)
    k = len(values)
    means = sorted(sum(rng.choices(values, k=k)) / k for _ in range(n))
    return means[int(0.025 * n)], means[int(0.975 * n)]


def summarize(data):
    out = []
    mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")
    for (model, name), rows in data.items():
        n = len(rows)
        correct = sum(r["exact"] for r in rows)
        noisy = [r for r in rows if r["noisy"]]
        clean = [r for r in rows if not r["noisy"]]
        acc_lo, acc_hi = bootstrap_ci([float(r["exact"]) for r in rows])
        f1_lo, f1_hi = bootstrap_ci([r["f1"] for r in rows])
        total_cost = sum(r["cost"] for r in rows)
        out.append({
            "model": model, "prompt": name, "n": n, "correct": correct,
            "accuracy": correct / n, "acc_ci_low": acc_lo, "acc_ci_high": acc_hi,
            "mean_f1": mean([r["f1"] for r in rows]), "f1_ci_low": f1_lo, "f1_ci_high": f1_hi,
            "mean_precision": mean([r["precision"] for r in rows]),
            "mean_recall": mean([r["recall"] for r in rows]),
            "wrong_but_partial": sum(1 for r in rows if not r["exact"] and r["f1"] > 0),
            "wrong_total": n - correct,
            "mean_f1_of_wrong": mean([r["f1"] for r in rows if not r["exact"]]),
            "cost_per_correct_usd": total_cost / correct,
            "billed_tokens_per_correct": sum(r["billed_tokens"] for r in rows) / correct,
            "output_tokens_per_correct": sum(r["output_tokens"] for r in rows) / correct,
            "seconds_per_correct": sum(r["wall_s"] for r in rows) / correct,
            "correct_per_dollar": correct / total_cost,
            "n_noisy": len(noisy), "n_clean": len(clean),
            "acc_noisy": mean([float(r["exact"]) for r in noisy]),
            "acc_clean": mean([float(r["exact"]) for r in clean]),
            "f1_noisy": mean([r["f1"] for r in noisy]),
            "f1_clean": mean([r["f1"] for r in clean]),
            "noise_drop_acc": mean([float(r["exact"]) for r in clean]) - mean([float(r["exact"]) for r in noisy]),
        })
    return out


def paired_compare(data):
    """Per model: on how many questions does prompt X get a higher F1 than prompt Y."""
    res = []
    models = sorted({m for m, _ in data}, key=[m for m, _ in MODELS].index)
    names = [n for _, n in PROMPTS]
    for model in models:
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                a, b = data[(model, names[i])], data[(model, names[j])]
                better = sum(x["f1"] > y["f1"] for x, y in zip(a, b))
                worse = sum(x["f1"] < y["f1"] for x, y in zip(a, b))
                res.append({"model": model, "a": names[i], "b": names[j], "a_better": better,
                            "b_better": worse, "tie": len(a) - better - worse})
    return res


def make_chart(summary):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    models = [m for m, _ in MODELS if any(s["model"] == m for s in summary)]
    names = [n for _, n in PROMPTS]
    S = {(s["model"], s["prompt"]): s for s in summary}
    x = np.arange(len(names))
    w = 0.8 / len(models)
    hatches = ["", "//"]
    fig, ax = plt.subplots(2, 3, figsize=(16, 9))
    ax = ax.ravel()

    def grouped(a, key, title, ylabel, fmt, scale=1.0, ci=None, ylim=None):
        for mi, m in enumerate(models):
            vals = [S[(m, n)][key] * scale for n in names]
            errs = None
            if ci:
                errs = [[(S[(m, n)][key] - S[(m, n)][ci[0]]) * scale for n in names],
                        [(S[(m, n)][ci[1]] - S[(m, n)][key]) * scale for n in names]]
            pos = x + (mi - (len(models) - 1) / 2) * w
            a.bar(pos, vals, w, color=[COLORS[n] for n in names], hatch=hatches[mi], edgecolor="white",
                  yerr=errs, capsize=4, ecolor="#444", label=m)
            base = ylim[0] if ylim else 0
            for p_, v in zip(pos, vals):
                if v < 0:  # negative bar: label below its end
                    a.annotate(fmt.format(v), (p_, v), xytext=(0, -12), textcoords="offset points", ha="center", fontsize=8)
                else:
                    a.annotate(fmt.format(v), (p_, base), xytext=(0, 4), textcoords="offset points", ha="center",
                               fontsize=8, color="white", fontweight="bold")
        a.set_xticks(x, names)
        a.set_title(title, fontsize=11, fontweight="bold")
        a.set_ylabel(ylabel + (f" (axis starts at {ylim[0]})" if ylim and ylim[0] > 0 else ""))
        if ylim:
            a.set_ylim(*ylim)
        a.spines[["top", "right"]].set_visible(False)

    grouped(ax[0], "accuracy", "Exact-match accuracy (95% bootstrap CI)", "%", "{:.1f}", 100, ("acc_ci_low", "acc_ci_high"), (70, 100))
    grouped(ax[1], "mean_f1", "Mean row-F1 (95% bootstrap CI)", "%", "{:.1f}", 100, ("f1_ci_low", "f1_ci_high"), (70, 100))
    grouped(ax[2], "mean_f1_of_wrong", "Mean F1 on the WRONG answers", "%", "{:.0f}", 100, ylim=(0, 100))
    grouped(ax[3], "cost_per_correct_usd", "Cost per correct answer", "milli-USD", "{:.1f}", 1000)
    grouped(ax[4], "seconds_per_correct", "Seconds per correct answer", "seconds", "{:.2f}")
    grouped(ax[5], "noise_drop_acc", "Noise robustness: accuracy clean - noisy\n(> 0 = worse on noisy questions)", "percentage points", "{:+.1f}", 100)
    ax[5].axhline(0, color="#999", lw=0.8)
    from matplotlib.patches import Patch
    fig.legend(handles=[Patch(facecolor="#888", hatch=h, edgecolor="white", label=m) for m, h in zip(models, hatches)],
               loc="upper right", frameon=False, ncol=len(models))
    fig.suptitle("Task 3 - additional metrics (effort medium; solid = " + " , hatched = ".join(models) + ")",
                 fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT / "metrics_comparison.png", dpi=150)


def main():
    OUT.mkdir(exist_ok=True)
    data = load()
    summary = summarize(data)
    pairs = paired_compare(data)
    with (OUT / "metrics_summary.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0]))
        w.writeheader(); w.writerows(summary)
    with (OUT / "metrics_per_question.csv").open("w", encoding="utf-8", newline="") as f:
        cols = ["model", "prompt"] + list(next(iter(data.values()))[0])
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for (model, name), rows in data.items():
            for r in rows:
                w.writerow({"model": model, "prompt": name, **r})
    (OUT / "metrics_summary.json").write_text(json.dumps({"summary": summary, "paired_f1": pairs}, indent=2))
    make_chart(summary)
    for s in summary:
        print(f"{s['model']:<10} {s['prompt']:<9} acc {s['accuracy']:.1%} [{s['acc_ci_low']:.1%},{s['acc_ci_high']:.1%}]  "
              f"F1 {s['mean_f1']:.3f} [{s['f1_ci_low']:.3f},{s['f1_ci_high']:.3f}]  F1(wrong) {s['mean_f1_of_wrong']:.2f} "
              f"partial {s['wrong_but_partial']}/{s['wrong_total']}  $/correct {s['cost_per_correct_usd']:.4f}  "
              f"tok/correct {s['billed_tokens_per_correct']:.0f}  s/correct {s['seconds_per_correct']:.2f}  "
              f"clean {s['acc_clean']:.1%} noisy {s['acc_noisy']:.1%} (n={s['n_clean']}/{s['n_noisy']})")
    for p in pairs:
        print(p)


if __name__ == "__main__":
    main()
