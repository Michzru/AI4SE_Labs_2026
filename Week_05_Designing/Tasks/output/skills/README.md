# Architecture design skills

Three skills that turn a requirements document into a chosen architecture and an Architecture Decision Record (ADR). They were distilled from the Week 05 Task 1 and Task 2 sessions on Teamify (`output/Task1_conversation.md`, `output/Task2_conversation.md`, `output/ADR-001-teamify-architecture.md`).

| Phase | Skill | Produces |
|---|---|---|
| 1 | `arch-requirements-analysis` | Notes file; actors, functional areas, domain model, architectural drivers, gaps table, every gap resolved (asked, or decided by the model when left to it), sizing + key insight |
| 2 | `arch-options-proposal` | ≥3 different architectures (diagram, hardest flow, pros, painful low-level parts), deep-dive Q&A, scored comparison, winner/runner-up/rejected, evolution path, "Input for the ADR" |
| 3 | `adr-authoring` | ADR from the template (user's final v4 preferences built in), self-review checklist, Mermaid render check, review rounds logged |

Typical prompts:
- "Read the requirements for EFarmers in data/ and let's discuss architectures. Keep notes in output/Task1_conversation.md."
- "Based on the Task 1 notes, write an ADR and keep notes in output/Task2_conversation.md."

Each skill also works on its own; a later phase runs the earlier one first if its input is missing.

## Files

```
skills/
├── README.md
├── arch-requirements-analysis/
│   ├── SKILL.md
│   └── references/notes-template.md
├── arch-options-proposal/
│   ├── SKILL.md
│   └── references/styles-catalogue.md
└── adr-authoring/
    ├── SKILL.md
    ├── assets/adr-template.md
    ├── references/review-checklist.md
    └── scripts/mermaid_check.py
```

## Installing

Claude Code loads project skills from `.claude/skills/`. To use them, copy the three skill folders there:

```bash
mkdir -p .claude/skills && cp -R output/skills/arch-* output/skills/adr-authoring .claude/skills/
```
