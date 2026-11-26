<!-- Created by Claude Code (claude-opus-5-5) on 2026-11-26 -->
# Task 9 – Konfigurácia Claude Code

**Výsledok:** Claude Code nemá jeden konfiguračný súbor. Nastavenia sú rozdelené podľa scope (používateľ, projekt, lokálne). Používateľské súbory z `~/.claude/` som skopíroval do [`config/user/`](config/user/). Lokálne a projektové súbory, ktoré nie sú v gite, sú v [`config/project/`](config/project/). Ani v jednom súbore nebol API kľúč, token ani e-mail. Kópie som robil cez redakčný skript a overil som, že sú zhodné s originálmi.

## Odovzdané súbory

| Kópia | Originál | Úloha | Obsah |
|---|---|---|---|
| [`config/user/CLAUDE.md`](config/user/CLAUDE.md) | `~/.claude/CLAUDE.md` | 1 – system prompt | 4 trvalé inštrukcie (slovenčina, kód po anglicky, pýtať sa pred commitom, „pocit 1–10“). Zhoduje sa s [claude_po_zmene.png](../Task_1/claude_po_zmene.png). |
| [`config/user/commands/lab-status.md`](config/user/commands/lab-status.md) | `~/.claude/commands/lab-status.md` | 2 – slash command | `/lab-status <týždeň>` vypíše tabuľku so stavom úloh týždňa |
| [`config/user/settings.json`](config/user/settings.json) | `~/.claude/settings.json` | 4 – model a effort | `model: opus`, `effortLevel: high`, zapnuté pluginy, `permissions.allow` |
| [`config/project/mcp.json`](config/project/mcp.json) | `<repo>/.mcp.json` | 7 – MCP | registrácia lokálneho stdio servera `underdog-lite` |
| [`config/project/settings.local.json`](config/project/settings.local.json) | `<repo>/.claude/settings.local.json` | 7 – MCP | `enabledMcpjsonServers: ["underdog-lite"]` (schválenie projektového MCP servera) |

Konfigurácia z ostatných úloh je v repe, takže ju nekopírujem:

| Úloha | Súbor |
|---|---|
| 3 – AGENTS.md | [`AGENTS.md`](../../../AGENTS.md), [`CLAUDE.md`](../../../CLAUDE.md) (`@AGENTS.md`) a `AGENTS.md`/`CLAUDE.md` v každom týždni |
| 5 – skill | [`.claude/skills/upece-oznamy/SKILL.md`](../../../.claude/skills/upece-oznamy/SKILL.md) |
| 6 – subagent | [`.claude/agents/week-summarizer.md`](../../../.claude/agents/week-summarizer.md) |
| 8 – rules | [`.claude/rules/file-provenance.md`](../../../.claude/rules/file-provenance.md), [`.claude/rules/workspace-boundaries.md`](../../../.claude/rules/workspace-boundaries.md) |

## Redakcia

- Skript pri kopírovaní nahrádza hodnoty v `env`, kľúče s názvom `key/token/secret/password/auth`, reťazce typu `sk-…`, e-maily a domovskú cestu (za `~`).
- V týchto súboroch nič také nebolo, takže kópie sa zhodujú s originálmi.
- `~/.claude.json` (stav účtu, ID, e-mail, OAuth údaje) som zámerne neotváral ani neodovzdal. Nastavenia z predchádzajúcich úloh v ňom nie sú.
- `OPENAI_API_KEY` je iba v `.env` (gitignore) a do žiadneho configu sa nedostal.

## Hierarchia nastavení v Claude Code

| Scope | Súbor | V gite |
|---|---|---|
| používateľ | `~/.claude/settings.json`, `~/.claude/CLAUDE.md`, `~/.claude/commands/`, `~/.claude/skills/` | nie |
| projekt | `.claude/settings.json`, `.mcp.json`, `.claude/{skills,agents,rules}/`, `CLAUDE.md` | áno |
| lokálne | `.claude/settings.local.json` | nie (gitignore) |

Pri konflikte má prednosť konkrétnejšie nastavenie, teda lokálne pred projektovým a projektové pred používateľským.
