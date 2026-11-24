# Assessment by laguna-s-2.1

# Week 03 Prompting
- Awarded: 5b out of 5b
- Commentary: All four tasks are complete and well executed. Task 1 delivers three valid, distinct non-prohibited frameworks (ICIO, Few-Shot, CoT) with machine-readable prompts and a clear justification. Tasks 2–4 build coherently on those prompts: predictions with full metadata and timing for two models, a novel metric implementation with a comparison report, and a full statistical analysis (Cochran's Q, exact McNemar, Friedman/Wilcoxon, Holm correction, bootstrap CIs) with tables, figures and a three-factor interpretation (prompt, model, coding agent). The only caveat is that the CoT prompt was reworded into a structured decomposition because the Claude CLI blocked free-form reasoning, but this is documented transparently. The generated outputs (tables.md, stats_results.json, figures, CSVs) match the reports.

## Task 1
- Awarded: 1b   (max 1b)
- Commentary: All required deliverables are present: `prompts.json` (data file with `{{SCHEMA}}`/`{{QUESTION}}` placeholders) and a readable `prompts.md`, plus a human report (`Task_1_human_report.md`) and a detailed report. Three frameworks from frompting.com/frameworks (ICIO, Few-Shot, CoT) were chosen, with ROSES and zero-shot excluded as required, and each is justified (where it was found, why chosen, what expected). The prompts are tailored to the text-to-SQL task and carry the fixed SELECT list and lowercase-literal rules. Complete and correct.

## Task 2
- Awarded: 1b   (max 1b)
- Commentary: `run_task2.py` calls `claude -p` once per (question, prompt) in fresh stateless sessions, measures wall-clock time, API time, TTFT, input/output tokens and cost, executes the predicted SQL against the database and compares the row multiset with the labels. Outputs include `predictions_prompt_a/b/c.csv` (with model, prompt_id, framework, time, tokens, cost, correctness columns), `raw_*.jsonl`, `summary.csv/json`, `comparison.png`, and per-model `report.md`. Runs cover both Sonnet 5.5 and Opus 5.5; inference times and token usage are reported (mean, median, P95). Results are interpreted, including the few-shot example leakage check and an error analysis. Complete and correct.

## Task 3
- Awarded: 1b   (max 1b)
- Commentary: `metrics.py` implements three metrics (B: row-level multiset F1 with partial credit, A: cost/billed-tokens/time per correct answer, C: noise robustness) plus 95% bootstrap confidence intervals. The report argues why each metric is applicable, defends it against the original exact-match metric, and explicitly discusses complement vs. replace (F1 complements and does not replace exact match; cost-per-correct complements accuracy; noise robustness is a diagnostic). Values are computed for the saved Task 2 predictions across both models and prompts, with paired F1 comparisons and a chart. Original and well implemented.

## Task 4
- Awarded: 2b   (max 2b)
- Commentary: `analysis.py` performs the full comparison and writes `tables.md`, `stats_results.json`, `error_causes_per_question.csv`, figures (fig1–fig5 per model, fig6–fig7 for the model comparison), and `model_comparison.json`. Tests are appropriate for paired data: Cochran's Q + exact McNemar for accuracy, Friedman + pairwise Wilcoxon for numeric metrics, Holm correction over the three pairs, and 10,000-resample paired bootstrap CIs as effect sizes. The report interprets significance (e.g. Few-Shot > CoT significant; ICIO vs Few-Shot borderline) and explains the differences via three factors: prompt (information transmission / conventions / region-join mistakes), model (Opus resolves the city column but is slower/more expensive and over-rewrites values), and coding agent (CLI overhead, reasoning_extraction block that reshaped CoT, caching/parallelism, usage limits). Tables and figures reproduce the reported numbers. Complete and correct.
