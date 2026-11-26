# AGENTS.md – AI4SE_Labs_2026

Lab assignments for the course *AI for Software Engineering* (2026). Each week is an independent folder; nothing is shared between weeks.

## Layout

| Folder | Topic | Agent notes |
|---|---|---|
| `Week_03_Prompting/` | Text-to-SQL prompt frameworks (ICIO, Few-Shot, CoT), model comparison | [AGENTS.md](Week_03_Prompting/AGENTS.md) |
| `Week_04_Requirements/` | LangGraph network that turns documents into a requirements spec | [AGENTS.md](Week_04_Requirements/AGENTS.md) |
| `Week_05_Designing/` | Architecture discussions, ADR, architecture skills | [AGENTS.md](Week_05_Designing/AGENTS.md) |
| `Week_06_Implementation/` | RAG over a code repo that fills in missing methods | [AGENTS.md](Week_06_Implementation/AGENTS.md) |
| `Week_08_Dissecting/` | Dissecting the coding assistant (config, commands, skills, MCP, rules) | [AGENTS.md](Week_08_Dissecting/AGENTS.md) |

Every week has assignment files `Task_N.md` (read-only, written by the lecturer) and the student's outputs next to them or in `output/`.

## Conventions

- Language: Python 3, no shared package; each week has its own `requirements.txt` and its own `.venv` (git-ignored).
- Code and code comments in English. Reports may be in Slovak or English – keep the language of the existing report.
- Reports lead with measured results and tables; no filler.
- Each week's README maps every assignment output to its file. Update it when adding outputs.
- Do not edit `Task_N.md` assignment files.

## Secrets

- API keys live in `.env` files (root `.env` has `OPENAI_API_KEY`; Week 06 uses `output/code/.env`). They are git-ignored – never print, commit or copy them into reports or submitted config.

## Git

- `main` is the only branch; this is a fork that pulls lecturer updates from upstream (`Neltharion59/...`).
- Ask before committing. No AI attribution lines in commits.
- `.DS_Store` files are noise – do not commit them.
