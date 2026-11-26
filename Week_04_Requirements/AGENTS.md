# AGENTS.md – Week 04 Requirements

LangGraph network that turns a directory of text documents into one Markdown requirements document (ids, tracing, MoSCoW priorities, blacklist). Everything is in `Task_1/`.

- Read first: `Task_1/README.md` (file map), `Task_1/docs/ARCHITECTURE.md` (nodes, state).
- Entry point: `network.py <corpus_dir>`; one module per node (`extraction.py`, `review.py`, `merge.py`, `priority.py`, `context.py`, `elaborate.py`, `render.py`).
- Tests: `python -m unittest test_network` – offline, 22 tests, fake LLM nodes. Run them after any change.
- A full run makes a few hundred OpenAI calls (~6 min). Do not start it without asking. Key: `OPENAI_API_KEY` from `.env` (searched upwards).
