#!/usr/bin/env python3
"""Task 4: statistical comparison and error analysis of the three prompts and two models.

Uses only saved results (Task_2/output/<model>/predictions_*.csv); no model calls.
Writes output/<model>/ (prompt comparison within one model) and
output/model_comparison/ (Sonnet 5.5 vs Opus 5.5, prompt x model).
Run from the Task_4 folder:   ../Task_2/.venv/bin/python analysis.py
"""
import csv
import itertools
import json
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
T2, T3 = HERE.parent / "Task_2", HERE.parent / "Task_3"
OUT = HERE / "output"
sys.path.insert(0, str(T2 / "data"))
import evaluate_retrieval_predictions as ev  # noqa: E402

MODELS = [("Sonnet 5.5", "sonnet-5.5"), ("Opus 5.5", "opus-5.5")]  # (label, Task_2/output sub-folder)
NAMES = ["ICIO", "Few-Shot", "CoT"]
PIDS = {"ICIO": "prompt_a", "Few-Shot": "prompt_b", "CoT": "prompt_c"}
COLORS = {"ICIO": "#4C78A8", "Few-Shot": "#F58518", "CoT": "#54A24B"}
RNG = np.random.default_rng(7)
N_BOOT = 10000


# ------------------------------------------------------------------ data
def load_predictions(path, labels, conn):
    with path.open(encoding="utf-8", newline="") as f:
        preds = list(csv.DictReader(f))
    assert len(preds) == len(labels), (path, len(preds))
    out = []
    for i, ((q, exp), p) in enumerate(zip(labels, preds)):
        assert p["question"] == q
        sql = p["predicted_sql"]
        try:
            got = [tuple(x) for x in conn.execute(sql).fetchall()]
        except Exception:
            got = []
        exact = ev.row_multiset(got) == ev.row_multiset(exp)
        c1, c2 = Counter(got), Counter(map(tuple, exp))
        ov = sum((c1 & c2).values())
        pr = ov / len(got) if got else (1.0 if not exp else 0.0)
        rc = ov / len(exp) if exp else (1.0 if not got else 0.0)
        f1 = 1.0 if (not got and not exp) else (2 * pr * rc / (pr + rc) if pr + rc else 0.0)
        out.append(dict(i=i, q=q, sql=sql, exp=exp, got=got, exact=exact, f1=f1,
                        wall=float(p["wall_s"]), api=float(p["api_ms"]) / 1000, out_tok=int(p["output_tokens"]),
                        cost=float(p["cost_usd"]),
                        billed=sum(int(p[k]) for k in ("input_tokens", "cache_creation_tokens",
                                                       "cache_read_tokens", "output_tokens"))))
    return out


def load():
    """-> labels, {model: {prompt: [row dicts]}}, db connection, set of region values"""
    csv.field_size_limit(10**9)
    with (T2 / "data" / "restaurants_dataset.csv").open(encoding="utf-8", newline="") as f:
        labels = [(r["question"], json.loads(r["result"])) for r in csv.DictReader(f)]
    conn = ev.load_database()
    regions = {r[0] for r in conn.execute("SELECT DISTINCT REGION FROM GEOGRAPHIC")}
    by_model = {}
    for model, sub in MODELS:
        paths = {n: T2 / "output" / sub / f"predictions_{PIDS[n]}.csv" for n in NAMES}
        if all(p.exists() and sum(1 for _ in csv.DictReader(p.open(encoding="utf-8", newline=""))) == len(labels)
               for p in paths.values()):
            by_model[model] = {n: load_predictions(paths[n], labels, conn) for n in NAMES}
        else:
            print(f"skipping {model}: predictions missing or incomplete")
    return labels, by_model, conn, regions


# ------------------------------------------------------------------ question types
REGION_STEMS = ["bay area", "napa valley", "monterey", "lake tahoe", "los angeles", "northern california",
                "sacramento", "yosemite", "mono lake"]


def qtype(q):
    ql = q.lower()
    if re.search(r"\b(in|of) (the )?(unknown)\s*\?", ql) or any(s in ql for s in REGION_STEMS):
        return "region"
    if re.search(r"\bon .+ in ", ql):
        return "street"
    if "best" in ql:
        return "best"
    if "rating above" in ql:
        return "city + rating"
    return "other"


# ------------------------------------------------------------------ error causes
def fix_city(sql):
    return (sql.replace("RESTAURANT.CITY_NAME", "LOCATION.CITY_NAME")
               .replace("R.CITY_NAME", "L.CITY_NAME"))


def cause(r, labels, conn, regions):
    sql, q, ql = r["sql"], r["q"].lower(), r["q"].lower()
    if len(r["exp"]) > 1000 and not r["got"]:
        return "nonsense question / label"
    # 1. wrong city column: switching the city filter to LOCATION fixes it
    if "GEOGRAPHIC" not in sql.upper() and fix_city(sql) != sql:
        try:
            if ev.row_multiset(conn.execute(fix_city(sql)).fetchall()) == ev.row_multiset(r["exp"]):
                return "city filter on RESTAURANT instead of LOCATION"
        except Exception:
            pass
    lits = re.findall(r"REGION\s*(?:=|LIKE)\s*'([^']*)'", sql, re.I)
    if lits and any(l.rstrip("%") not in regions for l in lits):
        return "region value not as stored ('sacramento' vs 'sacramento area')"
    if "GEOGRAPHIC" not in sql.upper() and any(s in ql for s in REGION_STEMS + ["unknown"]) and "unknown" not in ql.split("restaurants in the")[-1:][0][:0]:
        return "region treated as a city / region ignored"
    if re.search(r"GEOGRAPHIC\s+ON\s+LOCATION\.CITY_NAME|G\.CITY_NAME\s*=\s*L\.CITY_NAME", sql, re.I):
        return "region joined through LOCATION city"
    if re.search(r"MAX\s*\(", sql, re.I) and "best" not in ql:
        return "added 'best' (MAX) that was not asked"
    if re.search(r"FOOD_TYPE\s*=\s*'[^']*food'", sql, re.I) and "bar food" not in "":
        return "filler word 'food' kept in food type"
    if re.search(r"FOOD_TYPE\s+IN", sql, re.I) or ("/" in ql and "FOOD_TYPE" in sql):
        return "compound food type split"
    if ("#" in ql or " apt " in ql or " ste " in ql):
        m = re.search(r"STREET_NAME\s*=\s*'([^']*)'", sql)
        if not m or not any(ch in m.group(1) for ch in "#"):
            return "street name with suffix split (number / '#')"
    if re.search(r"HOUSE_NUMBER\s*=", sql):
        return "street name with suffix split (number / '#')"
    if not r["got"] and r["exp"]:
        return "empty result, other reason"
    return "other"


# ------------------------------------------------------------------ statistics
def holm(ps):
    order = np.argsort(ps)
    adj = np.empty(len(ps))
    run = 0.0
    for rank, idx in enumerate(order):
        run = max(run, (len(ps) - rank) * ps[idx])
        adj[idx] = min(1.0, run)
    return adj


def mcnemar_exact(a, b):
    n10 = int(np.sum(a & ~b))
    n01 = int(np.sum(~a & b))
    n = n10 + n01
    p = 1.0 if n == 0 else stats.binomtest(n10, n, 0.5).pvalue
    return n10, n01, p


def cochran_q(M):
    k = M.shape[1]
    T = M.sum()
    cj, ri = M.sum(0), M.sum(1)
    q = (k - 1) * (k * (cj ** 2).sum() - T ** 2) / (k * T - (ri ** 2).sum())
    return q, stats.chi2.sf(q, k - 1)


def boot_diff(x, y, stat=np.mean):
    d = np.asarray(x, float) - np.asarray(y, float)
    idx = RNG.integers(0, len(d), (N_BOOT, len(d)))
    s = np.array([stat(d[ix]) for ix in idx]) if stat is not np.mean else d[idx].mean(1)
    return float(stat(d)), float(np.percentile(s, 2.5)), float(np.percentile(s, 97.5))


def boot_ci(x):
    x = np.asarray(x, float)
    s = x[RNG.integers(0, len(x), (N_BOOT, len(x)))].mean(1)
    return float(x.mean()), float(np.percentile(s, 2.5)), float(np.percentile(s, 97.5))


def analyze_model(model, rows, labels, conn, regions, out):
    """Prompt comparison within one model (tests, tables, figures) -> out/"""
    out.mkdir(parents=True, exist_ok=True)
    n = len(labels)
    acc = {k: np.array([r["exact"] for r in v]) for k, v in rows.items()}
    res = {"model": model, "n": n}

    # --- accuracy: omnibus + pairwise
    M = np.column_stack([acc[k] for k in NAMES]).astype(int)
    q, p = cochran_q(M)
    res["cochran_q"] = {"Q": q, "df": 2, "p": p}
    pairs = list(itertools.combinations(NAMES, 2))
    mc = []
    for a, b in pairs:
        n10, n01, pv = mcnemar_exact(acc[a], acc[b])
        d, lo, hi = boot_diff(acc[a], acc[b])
        mc.append(dict(a=a, b=b, only_a=n10, only_b=n01, diff=d, ci_lo=lo, ci_hi=hi, p=pv))
    adj = holm([m["p"] for m in mc])
    for m, ad in zip(mc, adj):
        m["p_holm"] = float(ad)
    res["mcnemar"] = mc
    res["acc_ci"] = {k: boot_ci(acc[k]) for k in NAMES}

    # --- other metrics: Friedman + pairwise Wilcoxon
    metrics = {"row-F1": "f1", "wall time (s)": "wall", "API time (s)": "api",
               "output tokens": "out_tok", "billed tokens": "billed", "cost (USD)": "cost"}
    res["metrics"] = {}
    for label, key in metrics.items():
        X = {k: np.array([r[key] for r in rows[k]], float) for k in NAMES}
        fr = stats.friedmanchisquare(*[X[k] for k in NAMES])
        pw = []
        for a, b in pairs:
            d = X[a] - X[b]
            try:
                w = stats.wilcoxon(X[a], X[b], zero_method="wilcox")
                pv = float(w.pvalue)
            except ValueError:
                pv = 1.0
            md, lo, hi = boot_diff(X[a], X[b])
            dz = float(d.mean() / d.std(ddof=1)) if d.std(ddof=1) > 0 else 0.0
            pw.append(dict(a=a, b=b, mean_diff=md, ci_lo=lo, ci_hi=hi, dz=dz, p=pv))
        for m, ad in zip(pw, holm([m["p"] for m in pw])):
            m["p_holm"] = float(ad)
        res["metrics"][label] = {"friedman_chi2": float(fr.statistic), "friedman_p": float(fr.pvalue),
                                 "means": {k: float(X[k].mean()) for k in NAMES},
                                 "medians": {k: float(np.median(X[k])) for k in NAMES}, "pairwise": pw}

    # --- agent overhead (wall - API time)
    res["overhead_s"] = {k: float(np.mean([r["wall"] - r["api"] for r in rows[k]])) for k in NAMES}

    # --- agreement patterns
    pat = Counter(tuple(int(acc[k][i]) for k in NAMES) for i in range(n))
    res["agreement"] = {"".join(map(str, k)): v for k, v in sorted(pat.items(), reverse=True)}

    # --- question types
    types = [qtype(qq) for qq, _ in labels]
    res["types"] = {}
    for t in ["city + rating", "best", "street", "region", "other"]:
        idx = [i for i, x in enumerate(types) if x == t]
        res["types"][t] = {"n": len(idx), **{k: float(np.mean([acc[k][i] for i in idx])) for k in NAMES}}

    # --- error causes
    causes = {k: Counter() for k in NAMES}
    per_error = []
    for k in NAMES:
        for r in rows[k]:
            if not r["exact"]:
                c = cause(r, labels, conn, regions)
                causes[k][c] += 1
                per_error.append(dict(model=model, prompt=k, row=r["i"], cause=c, question=r["q"][:140], sql=r["sql"][:400]))
    res["causes"] = {k: dict(v) for k, v in causes.items()}
    with (out / "error_causes_per_question.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(per_error[0]))
        w.writeheader(); w.writerows(per_error)

    (out / "stats_results.json").write_text(json.dumps(res, indent=2, default=float), encoding="utf-8")
    write_tables(res, out)
    make_figs(res, rows, acc, n, out, model)
    print("=" * 30, model)
    print(json.dumps({k: res[k] for k in ("cochran_q", "mcnemar", "agreement", "types", "causes", "overhead_s")},
                     indent=1, default=float))
    for lab, m in res["metrics"].items():
        print(lab, "friedman p=%.4g" % m["friedman_p"], {k: round(v, 3) for k, v in m["means"].items()},
              [(x["a"], x["b"], round(x["mean_diff"], 3), "p_holm=%.3g" % x["p_holm"]) for x in m["pairwise"]])
    return res


# ------------------------------------------------------------------ outputs
def write_tables(res, out):
    L = [f"# Tables (auto-generated) - {res['model']}\n"]
    L.append("## Accuracy, pairwise (exact McNemar, Holm-adjusted)\n")
    L.append("| A | B | only A correct | only B correct | acc A - acc B [95 % CI] | p | p (Holm) |\n|---|---|---|---|---|---|---|")
    for m in res["mcnemar"]:
        L.append(f"| {m['a']} | {m['b']} | {m['only_a']} | {m['only_b']} | {m['diff']*100:+.1f} pt [{m['ci_lo']*100:+.1f}, {m['ci_hi']*100:+.1f}] | {m['p']:.4f} | {m['p_holm']:.4f} |")
    q = res["cochran_q"]
    L.append(f"\nCochran's Q (all three prompts): Q = {q['Q']:.2f}, df = 2, p = {q['p']:.4f}\n")
    L.append("## Other metrics (Friedman + pairwise Wilcoxon, Holm-adjusted)\n")
    L.append("| Metric | Friedman p | ICIO | Few-Shot | CoT | Pair | mean diff [95 % CI] | p (Holm) |\n|---|---|---|---|---|---|---|---|")
    for lab, m in res["metrics"].items():
        for j, pw in enumerate(m["pairwise"]):
            head = f"| {lab} | {m['friedman_p']:.3g} | {m['means']['ICIO']:.3g} | {m['means']['Few-Shot']:.3g} | {m['means']['CoT']:.3g} " if j == 0 else "| | | | | "
            L.append(head + f"| {pw['a']} - {pw['b']} | {pw['mean_diff']:+.3g} [{pw['ci_lo']:+.3g}, {pw['ci_hi']:+.3g}] | {pw['p_holm']:.3g} |")
    (out / "tables.md").write_text("\n".join(L), encoding="utf-8")


def make_figs(res, rows, acc, n, out, model):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # fig1: accuracy with CI + pairwise differences
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    for i, k in enumerate(NAMES):
        m, lo, hi = res["acc_ci"][k]
        ax[0].bar(i, m * 100, color=COLORS[k]); ax[0].errorbar(i, m * 100, yerr=[[(m - lo) * 100], [(hi - m) * 100]], color="#333", capsize=6)
        ax[0].text(i, 72, f"{m*100:.1f}%", ha="center", color="white", fontweight="bold")
    ax[0].set_xticks(range(3), NAMES); ax[0].set_ylim(70, 100); ax[0].set_ylabel("exact-match accuracy % (axis starts at 70)")
    ax[0].set_title(f"{model}: accuracy with 95 % bootstrap CI", fontweight="bold")
    for i, m in enumerate(res["mcnemar"]):
        ax[1].errorbar(m["diff"] * 100, i, xerr=[[(m["diff"] - m["ci_lo"]) * 100], [(m["ci_hi"] - m["diff"]) * 100]], fmt="o", color="#333", capsize=6)
        ax[1].text(max(m["ci_hi"], 0) * 100 + 1.0, i, f"only {m['a']}: {m['only_a']} / only {m['b']}: {m['only_b']}\np(Holm)={m['p_holm']:.3f}", va="center", fontsize=9)
    ax[1].axvline(0, color="#999", ls="--")
    ax[1].set_yticks(range(3), [f"{m['a']} - {m['b']}" for m in res["mcnemar"]]); ax[1].invert_yaxis()
    ax[1].set_xlim(-12, 24); ax[1].set_xlabel("accuracy difference, percentage points (paired bootstrap 95 % CI)")
    ax[1].set_title("Pairwise differences (right of 0 = first prompt better)", fontweight="bold")
    for a in ax: a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out / "fig1_accuracy_and_differences.png", dpi=150); plt.close(fig)

    # fig2: agreement patterns
    pat = res["agreement"]
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    labs = {"111": "all three", "000": "none", "010": "Few-Shot only", "110": "ICIO + Few-Shot", "011": "Few-Shot + CoT",
            "100": "ICIO only", "101": "ICIO + CoT", "001": "CoT only"}
    keys = [k for k in labs if k in pat]
    keys.sort(key=lambda k: -pat[k])
    ax.barh([labs[k] for k in keys], [pat[k] for k in keys], color="#7A8FA6")
    for i, k in enumerate(keys): ax.text(pat[k] + 1, i, str(pat[k]), va="center")
    ax.invert_yaxis(); ax.set_xlabel("number of questions"); ax.set_title(f"{model}: which prompts solved the same question", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False); fig.tight_layout(); fig.savefig(out / "fig2_agreement.png", dpi=150); plt.close(fig)

    # fig3: accuracy by question type
    types = list(res["types"])
    fig, ax = plt.subplots(figsize=(9.5, 4.6))
    w = 0.26
    for j, k in enumerate(NAMES):
        v = [res["types"][t][k] * 100 for t in types]
        b = ax.bar(np.arange(len(types)) + (j - 1) * w, v, w, color=COLORS[k], label=k)
        for r, x in zip(b, v): ax.text(r.get_x() + r.get_width() / 2, x + 1, f"{x:.0f}", ha="center", fontsize=8)
    ax.set_xticks(range(len(types)), [f"{t}\n(n={res['types'][t]['n']})" for t in types]); ax.set_ylim(0, 108)
    ax.set_ylabel("accuracy %"); ax.legend(frameon=False, ncol=3, loc="lower left"); ax.set_title(f"{model}: accuracy by question type", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False); fig.tight_layout(); fig.savefig(out / "fig3_question_types.png", dpi=150); plt.close(fig)

    # fig4: error causes
    allc = sorted({c for k in NAMES for c in res["causes"][k]}, key=lambda c: -sum(res["causes"][k].get(c, 0) for k in NAMES))
    cmap = plt.get_cmap("tab20")
    fig, ax = plt.subplots(figsize=(10, 4.4))
    left = np.zeros(3)
    for ci, c in enumerate(allc):
        v = np.array([res["causes"][k].get(c, 0) for k in NAMES])
        ax.barh(NAMES, v, left=left, color=cmap(ci), label=c)
        for yi, (l, x) in enumerate(zip(left, v)):
            if x >= 2: ax.text(l + x / 2, yi, str(x), ha="center", va="center", fontsize=8, color="white", fontweight="bold")
        left += v
    ax.invert_yaxis(); ax.set_xlabel("number of wrong answers"); ax.set_title(f"{model}: why the answers were wrong (automatic classification)", fontweight="bold")
    ax.legend(frameon=False, fontsize=7.5, loc="center left", bbox_to_anchor=(1.0, 0.5)); ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out / "fig4_error_causes.png", dpi=150); plt.close(fig)

    # fig5: time distribution, API vs overhead, accuracy-vs-time
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.6))
    ax[0].boxplot([[r["wall"] for r in rows[k]] for k in NAMES], tick_labels=NAMES, patch_artist=True,
                  boxprops=dict(facecolor="#dde6f0"), medianprops=dict(color="#c0392b"))
    ax[0].set_ylabel("seconds per question"); ax[0].set_title(f"{model}: inference time (wall clock)", fontweight="bold")
    api = [np.mean([r["api"] for r in rows[k]]) for k in NAMES]; ov = [res["overhead_s"][k] for k in NAMES]
    ax[1].bar(NAMES, api, color=[COLORS[k] for k in NAMES], label="API time")
    ax[1].bar(NAMES, ov, bottom=api, color="#bbbbbb", label="CLI overhead (wall - API)")
    for i, (a, o) in enumerate(zip(api, ov)):
        ax[1].text(i, a / 2, f"{a:.2f}", ha="center", color="white", fontweight="bold"); ax[1].text(i, a + o / 2, f"{o:.2f}", ha="center")
    ax[1].legend(frameon=False, fontsize=8); ax[1].set_ylabel("seconds"); ax[1].set_title("Where the time goes (mean)", fontweight="bold")
    for k in NAMES:
        t = np.mean([r["wall"] for r in rows[k]]); a = acc[k].mean() * 100
        c = np.mean([r["cost"] for r in rows[k]])
        ax[2].scatter(t, a, s=c * 12000, color=COLORS[k], alpha=0.85); ax[2].annotate(k, (t, a), xytext=(10, 8), textcoords="offset points")
    ax[2].set_xlabel("mean seconds per question"); ax[2].set_ylabel("accuracy %"); ax[2].margins(0.35)
    ax[2].set_title("Accuracy vs time (bubble size = mean cost)", fontweight="bold")
    for a in ax: a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out / "fig5_time_and_tradeoff.png", dpi=150); plt.close(fig)


# ------------------------------------------------------------------ model factor
MF_METRICS = {"row-F1": "f1", "wall time (s)": "wall", "API time (s)": "api", "output tokens": "out_tok",
              "cost (USD)": "cost"}


def compare_models(by_model, per_model_res, out):
    """Sonnet vs Opus on the same questions and prompts -> out/"""
    out.mkdir(parents=True, exist_ok=True)
    A, B = list(by_model)[:2]
    res = {"models": [A, B], "per_prompt": {}, "interaction": [], "agreement": {}, "conditions": []}

    # six conditions overview
    for m in (A, B):
        for k in NAMES:
            r = by_model[m][k]
            acc = np.array([x["exact"] for x in r], float)
            mean, lo, hi = boot_ci(acc)
            res["conditions"].append(dict(
                model=m, prompt=k, accuracy=mean, ci_lo=lo, ci_hi=hi, correct=int(acc.sum()),
                f1=float(np.mean([x["f1"] for x in r])), wall=float(np.mean([x["wall"] for x in r])),
                api=float(np.mean([x["api"] for x in r])), out_tok=float(np.mean([x["out_tok"] for x in r])),
                cost=float(np.mean([x["cost"] for x in r])),
                cochran_p=per_model_res[m]["cochran_q"]["p"]))

    # model effect within each prompt
    acc_tests = []
    for k in NAMES:
        a = np.array([x["exact"] for x in by_model[A][k]])
        b = np.array([x["exact"] for x in by_model[B][k]])
        n10, n01, pv = mcnemar_exact(b, a)  # B (Opus) first
        d, lo, hi = boot_diff(b, a)
        acc_tests.append(dict(prompt=k, only_B=n10, only_A=n01, diff=d, ci_lo=lo, ci_hi=hi, p=pv))
        res["agreement"][k] = {"both": int(np.sum(a & b)), f"only {A}": int(np.sum(a & ~b)),
                               f"only {B}": int(np.sum(~a & b)), "neither": int(np.sum(~a & ~b))}
    for t, ad in zip(acc_tests, holm([t["p"] for t in acc_tests])):
        t["p_holm"] = float(ad)
    res["accuracy_tests"] = acc_tests
    res["metric_tests"] = {}
    for label, key in MF_METRICS.items():
        tests = []
        for k in NAMES:
            xa = np.array([x[key] for x in by_model[A][k]], float)
            xb = np.array([x[key] for x in by_model[B][k]], float)
            try:
                pv = float(stats.wilcoxon(xb, xa, zero_method="wilcox").pvalue)
            except ValueError:
                pv = 1.0
            md, lo, hi = boot_diff(xb, xa)
            tests.append(dict(prompt=k, mean_A=float(xa.mean()), mean_B=float(xb.mean()), diff=md, ci_lo=lo, ci_hi=hi, p=pv))
        for t, ad in zip(tests, holm([t["p"] for t in tests])):
            t["p_holm"] = float(ad)
        res["metric_tests"][label] = tests

    # prompt x model interaction: does the gap between two prompts change with the model?
    for p1, p2 in itertools.combinations(NAMES, 2):
        xa = np.array([x["exact"] for x in by_model[A][p1]], float) - np.array([x["exact"] for x in by_model[A][p2]], float)
        xb = np.array([x["exact"] for x in by_model[B][p1]], float) - np.array([x["exact"] for x in by_model[B][p2]], float)
        d, lo, hi = boot_diff(xb, xa)
        res["interaction"].append(dict(pair=f"{p1} - {p2}", gap_A=float(xa.mean()), gap_B=float(xb.mean()),
                                       change=d, ci_lo=lo, ci_hi=hi))

    # cochran over all six conditions (same 155 questions)
    M = np.column_stack([[x["exact"] for x in by_model[m][k]] for m in (A, B) for k in NAMES]).astype(int)
    q, p = cochran_q(M)
    res["cochran_6"] = {"Q": q, "df": 5, "p": p}
    res["causes"] = {m: per_model_res[m]["causes"] for m in (A, B)}

    (out / "model_comparison.json").write_text(json.dumps(res, indent=2, default=float), encoding="utf-8")
    write_model_tables(res, out)
    make_model_figs(res, by_model, out)
    print("=" * 30, "model comparison")
    print(json.dumps({k: res[k] for k in ("accuracy_tests", "interaction", "agreement", "cochran_6")}, indent=1, default=float))
    for lab, ts in res["metric_tests"].items():
        print(lab, [(t["prompt"], round(t["mean_A"], 3), round(t["mean_B"], 3), "p_holm=%.3g" % t["p_holm"]) for t in ts])
    return res


def write_model_tables(res, out):
    A, B = res["models"]
    L = [f"# Tables (auto-generated) - {A} vs {B}\n", "## All six conditions\n",
         "| Model | Prompt | Accuracy [95 % CI] | Correct | Row-F1 | Mean wall time | Mean API time | Output tokens | Cost / question |",
         "|---|---|---|---|---|---|---|---|---|"]
    for c in res["conditions"]:
        L.append(f"| {c['model']} | {c['prompt']} | {c['accuracy']*100:.1f} % [{c['ci_lo']*100:.1f}, {c['ci_hi']*100:.1f}] | {c['correct']} | "
                 f"{c['f1']:.3f} | {c['wall']:.2f} s | {c['api']:.2f} s | {c['out_tok']:.0f} | ${c['cost']:.4f} |")
    q = res["cochran_6"]
    L.append(f"\nCochran's Q over all six conditions: Q = {q['Q']:.2f}, df = 5, p = {q['p']:.3g}\n")
    L += [f"## Model effect within each prompt ({B} - {A}), accuracy: exact McNemar, Holm over the 3 prompts\n",
          f"| Prompt | only {B} correct | only {A} correct | difference [95 % CI] | p | p (Holm) |", "|---|---|---|---|---|---|"]
    for t in res["accuracy_tests"]:
        L.append(f"| {t['prompt']} | {t['only_B']} | {t['only_A']} | {t['diff']*100:+.1f} pt [{t['ci_lo']*100:+.1f}, {t['ci_hi']*100:+.1f}] | {t['p']:.3g} | {t['p_holm']:.3g} |")
    L += [f"\n## Model effect on other metrics ({B} - {A}), Wilcoxon signed-rank, Holm over the 3 prompts\n",
          f"| Metric | Prompt | {A} | {B} | difference [95 % CI] | p (Holm) |", "|---|---|---|---|---|---|"]
    for lab, ts in res["metric_tests"].items():
        for t in ts:
            L.append(f"| {lab} | {t['prompt']} | {t['mean_A']:.4g} | {t['mean_B']:.4g} | {t['diff']:+.3g} [{t['ci_lo']:+.3g}, {t['ci_hi']:+.3g}] | {t['p_holm']:.3g} |")
    L += ["\n## Prompt x model interaction (gap between two prompts, in accuracy points)\n",
          f"| Prompt pair | gap with {A} | gap with {B} | change [95 % CI] |", "|---|---|---|---|"]
    for t in res["interaction"]:
        L.append(f"| {t['pair']} | {t['gap_A']*100:+.1f} | {t['gap_B']*100:+.1f} | {t['change']*100:+.1f} [{t['ci_lo']*100:+.1f}, {t['ci_hi']*100:+.1f}] |")
    L += ["\n## Same question, same prompt: agreement between the models\n",
          f"| Prompt | both correct | only {A} | only {B} | neither |", "|---|---|---|---|---|"]
    for k, a in res["agreement"].items():
        L.append(f"| {k} | {a['both']} | {a[f'only {A}']} | {a[f'only {B}']} | {a['neither']} |")
    (out / "tables.md").write_text("\n".join(L), encoding="utf-8")


def make_model_figs(res, by_model, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    A, B = res["models"]
    C = {(c["model"], c["prompt"]): c for c in res["conditions"]}
    x = np.arange(len(NAMES)); w = 0.38
    shade = {A: 1.0, B: 0.55}

    fig, ax = plt.subplots(2, 2, figsize=(13, 9))
    ax = ax.ravel()
    for mi, m in enumerate((A, B)):
        pos = x + (mi - 0.5) * w
        vals = [C[(m, k)]["accuracy"] * 100 for k in NAMES]
        err = [[(C[(m, k)]["accuracy"] - C[(m, k)]["ci_lo"]) * 100 for k in NAMES],
               [(C[(m, k)]["ci_hi"] - C[(m, k)]["accuracy"]) * 100 for k in NAMES]]
        ax[0].bar(pos, vals, w, color=[COLORS[k] for k in NAMES], alpha=shade[m], hatch="" if m == A else "//",
                  edgecolor="white", yerr=err, capsize=4, ecolor="#444")
        for p_, v in zip(pos, vals):
            ax[0].text(p_, 71, f"{v:.1f}", ha="center", color="white", fontweight="bold", fontsize=9)
    ax[0].set_xticks(x, NAMES); ax[0].set_ylim(70, 100); ax[0].set_ylabel("accuracy % (axis starts at 70)")
    ax[0].set_title(f"Accuracy, 95 % CI (solid = {A}, hatched = {B})", fontweight="bold")
    for k in NAMES:
        ax[1].plot([0, 1], [C[(A, k)]["accuracy"] * 100, C[(B, k)]["accuracy"] * 100], "-o", color=COLORS[k], lw=2.5, label=k)
        ax[1].annotate(f"{C[(B, k)]['accuracy']*100:.1f}", (1, C[(B, k)]["accuracy"] * 100), xytext=(8, 0), textcoords="offset points", va="center")
        ax[1].annotate(f"{C[(A, k)]['accuracy']*100:.1f}", (0, C[(A, k)]["accuracy"] * 100), xytext=(-30, 0), textcoords="offset points", va="center")
    ax[1].set_xticks([0, 1], [A, B]); ax[1].set_xlim(-0.3, 1.3); ax[1].set_ylabel("accuracy %"); ax[1].legend(frameon=False)
    ax[1].set_title("Interaction plot: does the prompt ranking change with the model?", fontweight="bold")
    for key, a, title, ylab in [("wall", ax[2], "Mean inference time per question (wall clock)", "seconds"),
                                ("out_tok", ax[3], "Mean output tokens per question", "tokens")]:
        for mi, m in enumerate((A, B)):
            pos = x + (mi - 0.5) * w
            vals = [C[(m, k)][key] for k in NAMES]
            a.bar(pos, vals, w, color=[COLORS[k] for k in NAMES], alpha=shade[m], hatch="" if m == A else "//", edgecolor="white")
            for p_, v in zip(pos, vals):
                a.text(p_, v, f"{v:.2f}" if key == "wall" else f"{v:.0f}", ha="center", va="bottom", fontsize=9)
        a.set_xticks(x, NAMES); a.set_ylabel(ylab); a.set_title(f"{title} (solid = {A}, hatched = {B})", fontweight="bold", fontsize=10)
    for a in ax: a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out / "fig6_model_comparison.png", dpi=150); plt.close(fig)

    # fig7: error causes for all six conditions
    rowsk = [(m, k) for m in (A, B) for k in NAMES]
    allc = sorted({c for m in (A, B) for k in NAMES for c in res["causes"][m][k]},
                  key=lambda c: -sum(res["causes"][m][k].get(c, 0) for m in (A, B) for k in NAMES))
    cmap = plt.get_cmap("tab20")
    fig, ax = plt.subplots(figsize=(11, 5))
    left = np.zeros(len(rowsk))
    ylabels = [f"{m} | {k}" for m, k in rowsk]
    for ci, c in enumerate(allc):
        v = np.array([res["causes"][m][k].get(c, 0) for m, k in rowsk])
        ax.barh(ylabels, v, left=left, color=cmap(ci), label=c)
        for yi, (l, xv) in enumerate(zip(left, v)):
            if xv >= 2: ax.text(l + xv / 2, yi, str(xv), ha="center", va="center", fontsize=8, color="white", fontweight="bold")
        left += v
    for yi, t in enumerate(left): ax.text(t + 0.3, yi, f"{int(t)}", va="center", fontsize=9)
    ax.invert_yaxis(); ax.set_xlabel("number of wrong answers (of 155)")
    ax.set_title("Why the answers were wrong, per model and prompt", fontweight="bold")
    ax.legend(frameon=False, fontsize=7.5, loc="center left", bbox_to_anchor=(1.0, 0.5)); ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out / "fig7_error_causes_by_model.png", dpi=150); plt.close(fig)


def main():
    labels, by_model, conn, regions = load()
    sub = dict(MODELS)
    per_model = {m: analyze_model(m, by_model[m], labels, conn, regions, OUT / sub[m]) for m in by_model}
    if len(by_model) >= 2:
        compare_models(by_model, per_model, OUT / "model_comparison")

if __name__ == "__main__":
    main()
