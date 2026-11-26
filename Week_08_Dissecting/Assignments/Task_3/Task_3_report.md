# Task 3 – AGENTS.md

**Assistant:** Claude Code (desktop app, Opus 5.5).

## How Claude Code supports it
- Claude Code's native memory file is `CLAUDE.md`, not `AGENTS.md`. It loads the root `CLAUDE.md` at session start and `CLAUDE.md` files in subfolders when it works with files there.
- The built-in `/init` command scans the repo and writes a `CLAUDE.md`. You can also just ask for the file in a prompt, and that is how I did it here.
- Claude Code does not read `AGENTS.md` by itself. The usual approach is to keep the content in `AGENTS.md`, so other assistants (Codex, Cursor, Copilot …) can use it too, and to put a one-line `CLAUDE.md` next to it with `@AGENTS.md`. This `@` import pulls the file into Claude's context.

## How the files were created
1. I ran my custom `/lab-status 08` command (Task 2). It reported that the repo has no `AGENTS.md`/`CLAUDE.md`.
2. I chose "Task 3 (AGENTS.md)". Claude Code read the root README and `.gitignore`, the directory tree, each week's README, the `requirements.txt` files, the test commands and the names of the `.env` keys (not their values).
3. It wrote these files:

| File | Content |
|---|---|
| `AGENTS.md` | Repo map, conventions (language, venvs, reports), secrets, git rules |
| `Week_0X_*/AGENTS.md` (5×) | Per week: topic, entry points, how to run tests, costly runs to avoid, files not to hand-edit |
| `CLAUDE.md` + `Week_0X_*/CLAUDE.md` | Only `@AGENTS.md` (import for Claude Code) |

4. Check: right after the report was written into `Week_08_Dissecting/`, Claude Code automatically loaded `Week_08_Dissecting/CLAUDE.md` into its context, with the imported `AGENTS.md` content. This shows the nested `@AGENTS.md` import works.
5. Next iteration: when a week changes, re-run `/init` or ask "update AGENTS.md for Week_XX". The per-week split keeps the root file short, so unrelated weeks do not use up context.
