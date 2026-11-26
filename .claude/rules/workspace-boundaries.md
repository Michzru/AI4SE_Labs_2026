# Workspace boundaries

These rules apply to every task in this repository.

## Secrets and sensitive files – never read
- Do not open, print, search (grep/cat/head) or copy `.env`, `.env.*`, `*.pem`, `*.key`, `credentials*`, `secrets*`, `~/.ssh/`, `~/.aws/`, `~/.claude.json` or any file that may contain API keys, tokens or passwords.
- If a task seems to need a secret, stop and ask the user. Refer to the variable by name (e.g. `OPENAI_API_KEY`), never by value.
- Do not run `env`, `printenv` or `set` to list environment variables.

## Stay inside the repository
- Work only inside the repository root (the folder containing this `.claude/`). Do not read, list or write anything in its parent folder or elsewhere on the disk, including via `..`, absolute paths or `cd`.
- Exceptions only when the user explicitly asks for a specific path outside the repo in chat.

## Other off-limits content
- Do not read `.git/` internals, `.venv/` or other virtual environments, or personal files unrelated to the task (photos, documents, browser data).
- If you are about to break one of these rules, stop and ask instead.
