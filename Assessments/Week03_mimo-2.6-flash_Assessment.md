# Assessment by mimo-2.6-flash

# Week 03 Prompting
- Awarded: 5b out of 5b
- Commentary: All four tasks are delivered completely and mutually consistent: three justified prompting frameworks, a scripted comparison over 155 questions with per-call metadata and timings on two models, an implemented and defended new metric (row-F1 plus efficiency), and a rigorous statistical analysis with correct paired tests, correction for multiplicity, figures and mechanistic explanations across prompt, model and agent factors. The reports are honest about limitations (single run, CLI-imposed CoT adaptation, cache-dependent cost, questionable labels).

## Task 1
- Awarded: 1b   (max 1b)
- Commentary: Three frameworks (ICIO, Few-Shot, CoT) are chosen from frompting.com/frameworks, excluding ROSES and zero-shot as required. The prompts are stored as a data file (prompts.json with a readable prompts.md copy) with {{SCHEMA}}/{{QUESTION}} placeholders, and the report explains where each framework was found, why it was chosen, and what was expected from it (including the expected accuracy/time/token trade-off), plus an honest note on adapting the CoT wording after the CLI blocked free-form reasoning output.

## Task 2
- Awarded: 1b   (max 1b)
- Commentary: The three Task 1 prompts are executed on all 155 questions (465 calls per model) with a fresh, stateless session per call, for two models (Sonnet 5.5 and Opus 5.5). Predictions are saved per prompt/model as CSV with rich metadata (model, effort, prompt_id, framework, wall/API/first-token times, tokens, cost, correctness, leakage flag) plus raw answers, and reports include accuracy tables, a comparison figure, inference-time statistics (mean/median/P95), a disagreement/error analysis, and an exclusion check for the four few-shot example questions.

## Task 3
- Awarded: 1b   (max 1b)
- Commentary: metrics.py implements genuinely new metrics — multiset row-level F1 (with precision/recall and mean F1 on errors), efficiency (cost/tokens/time per correct answer) and a noise-robustness diagnostic, plus bootstrap confidence intervals — and computes them for the saved Task 2 predictions of both models. The report argues why F1 fits a retrieval task, explicitly discusses complement-vs-replace against exact match (F1 complements, does not replace), and compares metric values per prompt with paired win/loss counts and a figure.

## Task 4
- Awarded: 2b   (max 2b)
- Commentary: Task_4_report.md is a detailed analysis backed by analysis.py and generated artefacts (tables.md, stats_results.json, error-cause CSVs, fig1–fig7 for each model plus a cross-model folder). It uses appropriate paired tests (Cochran's Q with exact McNemar for accuracy; Friedman with pairwise Wilcoxon for numeric metrics), Holm correction, 95 % paired bootstrap CIs, and reports effect sizes — with numerically correct values (verified e.g. the exact McNemar p = 0.000488 for 12/0 discordants, chi-square p for Q = 14.53). It determines which differences are and are not significant after correction, attributes causes by question type and classified error categories, and explicitly treats the prompt, the model (incl. the interesting Few-Shot example overriding Opus's better default) and the coding agent (CLI overhead, neutralised settings, platform safeguard, usage limits, caching) as factors, ending with limitations and conclusions.