# AGENTS.md – Week 03 Prompting

Text-to-SQL on the restaurants database (`Assignments/Task_2/data`, 155 labelled questions). Three prompts: A = ICIO, B = Few-Shot, C = CoT. Models: Sonnet 5.5 and Opus 5.5, called through the `claude` CLI (one new session per call).

- Output map: `Assignments/README.md`.
- Entry points: `Task_2/run_task2.py` (model calls, needs `claude` CLI), `Task_3/metrics.py` and `Task_4/analysis.py` (offline, no model calls).
- Venv: `Assignments/Task_2/.venv` (`matplotlib scipy numpy`), reused by Tasks 3 and 4.
- Results are per model in `output/<model>/`; do not overwrite them unless re-running on purpose (calls cost money).
