# Notes template – architecture discussion (phases 1 and 2)

Copy this skeleton into the notes file at the start of the session and fill it as the conversation goes. Sections that are not reached yet stay as a one-line placeholder, so the user can see what is still to come.

The file is about the system and the decision. It has no "method", "session start" or "assistant actions" section and does not mention skills, prompts, or which files were read. Tell the user such things in chat.

```markdown
# <System> – Architecture discussion notes

- **Date:** <YYYY-MM-DD>
- **Participants:** <user name> (lead), Claude Code (assistant)
- **Source requirements:** `<path>`
- **Goal:** <one sentence about the system, e.g. "Understand the requirements, compare at least three architectures and choose one.">

---

## 1. Requirements study – what <System> is
### 1.1 One-line summary
### 1.2 Stated main goals
### 1.3 Actors / roles
| Role | Description |
|---|---|
### 1.4 Functional areas (user stories grouped)
| # | Area | User stories | Notes |
|---|---|---|---|
### 1.5 Main entities (first-cut domain model)
### 1.6 Architectural drivers
### 1.7 Gaps and ambiguities found
| # | Observation | Why it matters for the architecture |
|---|---|---|
### 1.8 Decisions on the gaps
| Gap | Decision | Reason |
|---|---|---|
### 1.9 Sizing
**Sizing basis:** …
**Derived numbers** (peak and average labelled):
| | (a) Today | (b) Growth target |
|---|---|---|
| Registered users | | |
| Concurrent connections (peak) | | |
| Writes or messages/s (average / peak) | | |
| Storage per year | | |

**Key insight:** …

---

## 2. Architecture options
### 2.1 Architecture #1 – <name> (<scale it fits>)
### 2.2 Architecture #2 – …
### 2.3 Architecture #3 – …
### 2.4 Comparison & choice

---

## 3. Deep-dive questions
**Q1: …**

---

## 4. Outcome and input for the ADR
**Outcome:** …
**Input for the ADR:**
- **Decision:** …
- **Context:** §…
- **Options considered:** §2
- **Consequences:** pain points in §2 + answers in §3
```

There is no "open items" list. Anything still open is asked in chat and written here only once it is decided.
