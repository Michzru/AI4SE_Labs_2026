# AGENTS.md – Week 06 Implementation

RAG over the cloned `AI4SE_Playground` repo: AST chunking → LLM summaries + embeddings → cosine retrieval → LLM fills missing methods → unit tests. Result: 10/10 tasks, 481/481 tests.

- Read first: `Assignments/output/README.md` (Slovak). Reports: `Assignments/report_task1..6.md`.
- Code: `Assignments/output/code/` (`chunk_repo.py`, `embed_chunks.py`, `retrieve.py`, `solve_tasks.py`, `run_experiments.py`, `llm.py`). Key: `API_KEY` in `code/.env`.
- `output/week6/AI4SE_Playground/` is third-party code already patched by the pipeline; originals with stubs are in `code/backup_original/`.
- Playground tests: from the playground root `python -m unittest discover -s tests -t .`.
- Generated JSON (`chunks.json`, `chunk_store.json`, `stores/`, `results/`) is pipeline output – regenerate, don't hand-edit.
