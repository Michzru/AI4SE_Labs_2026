# Week 03 – Prompting: where to find the outputs

Problem: text-to-SQL on the restaurants database (`Task_2/data`), 155 labelled questions.
Models: **Sonnet 5.5** and **Opus 5.5** (both effort *medium*), called through the Claude Code CLI, one new session per call. Prompt A = ICIO, B = Few-Shot, C = CoT.

| Task | Required output | File |
|---|---|---|
| **1** | Data file with the formulated prompts | [Task_1/prompts.json](Task_1/prompts.json) (readable copy: [Task_1/prompts.md](Task_1/prompts.md)) |
| | Report: why each framework was chosen and where it was found | [Task_1/Task_1_human_report.md](Task_1/Task_1_human_report.md) (detailed version: [Task_1/Task_1_report.md](Task_1/Task_1_report.md)) |
| **2** | Predictions with model and prompt metadata | [Task_2/output/sonnet-5.5/](Task_2/output/sonnet-5.5/) and [Task_2/output/opus-5.5/](Task_2/output/opus-5.5/): `predictions_prompt_a/b/c.csv` (columns `model`, `prompt_id`, `framework`, time, tokens, cost, correctness); raw model answers in `raw_*.jsonl` |
| | Brief report with visualisation and inference times | [Task_2/Task_2_human_report.md](Task_2/Task_2_human_report.md); per model: `output/<model>/report.md`, `comparison.png`, `summary.csv` |
| | Code | [Task_2/run_task2.py](Task_2/run_task2.py) |
| **3** | Source code of the new metric | [Task_3/metrics.py](Task_3/metrics.py) |
| | Report comparing the prompts with the new metric | [Task_3/Task_3_report.md](Task_3/Task_3_report.md); values in [Task_3/output/](Task_3/output/) |
| **4** | Detailed report with tables, graphs and significance tests | [Task_4/Task_4_report.md](Task_4/Task_4_report.md) |
| | Tables, figures, test results | [Task_4/output/sonnet-5.5/](Task_4/output/sonnet-5.5/) and [Task_4/output/opus-5.5/](Task_4/output/opus-5.5/) (prompt comparison per model: `tables.md`, `stats_results.json`, `fig1`–`fig5`, `error_causes_per_question.csv`); [Task_4/output/model_comparison/](Task_4/output/model_comparison/) (Sonnet vs Opus: `tables.md`, `fig6`, `fig7`) |
| | Code | [Task_4/analysis.py](Task_4/analysis.py) |

## How to reproduce
```bash
cd Task_2
python3 -m venv .venv && .venv/bin/pip install matplotlib scipy numpy
.venv/bin/python run_task2.py                  # Sonnet 5.5 -> output/sonnet-5.5/  (needs the `claude` CLI)
.venv/bin/python run_task2.py --model opus     # Opus 5.5   -> output/opus-5.5/
cd ../Task_3 && ../Task_2/.venv/bin/python metrics.py     # no model calls
cd ../Task_4 && ../Task_2/.venv/bin/python analysis.py    # no model calls
```
