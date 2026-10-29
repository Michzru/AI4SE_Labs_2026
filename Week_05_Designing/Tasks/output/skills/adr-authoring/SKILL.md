---
name: adr-authoring
description: Phase 3 of 3 of the architecture workflow (requirements → architecture options → ADR). Writes an Architecture Decision Record (ADR) from an architecture discussion, self-reviews it for inconsistencies, adds Mermaid diagrams that are render-checked, and refines it with the user over several review rounds while logging what changed and why. Use this whenever the user asks to create, write, draft, review, shorten or improve an ADR / architecture decision record / design decision document, wants to "record the decision" after comparing architectures, or asks whether something belongs in an ADR.
---

# ADR authoring (phase 3 of 3)

Goal: an ADR that a non-expert reader understands, that records **one** decision with its reasons, and that a developer can build from. The reference run needed four versions to get there; the user's final preferences are baked into the template below, so start from them instead of rediscovering them.

## Step 0 – Notes and inputs

- Create a review log (default `output/Task2_conversation.md`) before writing the ADR, and update it after every round. Header: date, participants, input files, output file, goal. Per round record **user request → problems found → what changed and why** (a `# | Problem | Fix` table works well). The log is what makes the process reusable, so record the *why*.
- Read the architecture discussion notes (phase 2, usually `output/Task1_conversation.md`) — especially its "Input for the ADR" section — and the requirements file. If there was no discussion yet, run `arch-options-proposal` first; an ADR without considered options is just an announcement.
- Read the assignment if there is one: it tells you what review questions the user will ask.
- **The ADR records the system and the decision, not how it was made.** Write for a developer or reviewer who will never see this conversation. Keep out: skills, method, prompts, which files the assistant read or skipped, "produced in one pass", remarks about the conversation, and to-dos for the next review round. *Sources* and *References* list project documents only (requirements, discussion notes, review log). Process remarks go to the user in chat. The review log may say what changed and why, but it too names project documents, not skills or tools.

## Step 1 – Settle the framing (ask only if unclear)

These choices shaped the final ADR in the reference run. Use the defaults unless the user or the notes say otherwise:

| Question | Default |
|---|---|
| How many decisions? | **One decision per ADR.** The tech stack (language/framework) is a separate ADR — keep it out entirely. |
| Several target scales in the discussion? | **One decision for today's scale, with the growth target always visible.** Don't present two co-equal per-scale decisions; that made v3 confusing ("why is the small-scale decision made because of the large scale?"). But don't hide the growth target either: C1 states both numbers, the context has a small sizing table (today vs. growth target), and every growth step says what size it makes possible. A reader must see that the design was checked against the large scale. |
| Audience | Plain language. Explain every technical term where it first appears and in a glossary. Avoid unexplained jargon ("fleet", "cross-node delivery"). |
| Length | Aim for ~200–270 lines. Cut repetition before cutting content. |
| Format | Nygard core (Context → Decision → Consequences) extended with MADR parts (drivers, options, pros/cons), because the discussion compared options and plain Nygard has no place for that. |
| File | `output/ADR-NNN-<system>-<topic>.md`, status **Proposed (v1)**. |

## Step 2 – Write the draft from the template

Copy `assets/adr-template.md` and fill it. Section guidance:

- **Context:** what the system is, the hard part in plain words, a **sizing table** (today vs. growth target: users, concurrent connections, peak load, storage per year) and a **constraints table C1…** built from the decisions on the gaps. Every constraint is stated as a fact or a decision, never as an assumption.
- **Decision drivers D1…:** ranked, each linked to constraints. Users liked this section most; everything else refers to it.
- **Options considered:** one plain-words row per option, with a pointer to the discussion for details.
- **Decision:** one quoted sentence, then *why* (bullets citing drivers), then **"How we keep the option to grow"** — a concrete example of what would go wrong without the rule (e.g. "if messages lived only in the app's memory, a second app copy could never see them, so growth would mean a rewrite"), and growth steps with *what we add / why, in plain words* and observable triggers.
- **How it works today:** Mermaid diagrams — the deployment, the module borders, and one sequence diagram for the hardest flow. 3–4 diagrams total; more is noise.
- **Design rules R1…:** table `Rule (plain words) | Technical detail | Why (driver/constraint)`. These are the commitments that keep the decision valid (module boundaries enforced by tests, invariants in one transaction with row locks, save-then-push, idempotency keys, nothing important in memory, …).
- **Comparison:** exactly **one row per driver**, scores 1–5 with a few words each; costs marked as rough estimates, with what they include (e.g. "VM + managed database with point-in-time recovery").
- **Consequences:** good, and accepted downsides (honest — single point of failure, release disconnects users, …).
- **Rejected options:** why, and **what was kept** from each.
- **Glossary, When to revisit (observable triggers), References** (requirements, discussion notes, review log).

**Resolve questions instead of listing them.** Writing the ADR often raises questions about this decision, e.g. "is downtime of the single server acceptable?" or "is losing up to 24 h of data with daily backups acceptable?". Don't park them in an "Open questions" section and don't paper over them with assumptions. Ask the user in one batch, with your recommended answer and a one-line reason. If the user leaves it to you, or asked for the ADR without stopping, decide yourself: pick what best fits the drivers. Then write the answer into the ADR as a constraint (C#) and, if it changes the design, as a design rule (R#). Tell the user in chat which of these you decided yourself.

**Product rules:** include a product rule only if it has an architectural consequence, and then record *where* it is enforced, not the UI. Example: "new members don't see old messages" became "membership stores the sequence number at join; every chat read path filters by it in one place" — otherwise one endpoint will eventually leak.

## Step 3 – Self-review before showing it

Run through `references/review-checklist.md` (numbers, duplicate definitions, diagram completeness, hidden interactions, risks vs mitigations, matrix ↔ drivers, jargon). Then render-check every Mermaid block:

```bash
python3 <this skill's folder>/scripts/mermaid_check.py output/ADR-001-....md --out <scratch-dir>/adr_check.html
```

The page loads Mermaid 11.4.1 from a CDN, renders each block and fills the `#summary` element with one line per diagram: `OK`, or `ERROR` with the source line and the Mermaid parse error. Browser automation usually can't script `file://` pages, so serve the folder first (`python3 -m http.server 8765 --bind 127.0.0.1` in `<scratch-dir>`, in the background), open `http://127.0.0.1:8765/adr_check.html`, wait ~3 s and read `#summary` (page text or JS). Also take one screenshot — a diagram can render but be too wide or have clipped titles. Fix and re-run until all are OK, then stop the server.

## Step 4 – Review rounds with the user

Present the ADR. In chat, list the decisions you made yourself and anything you added beyond the discussion, so the user can overturn them. Then ask the standard review questions:

1. Is it informative enough — is something missing?
2. Is something extra or too detailed?
3. Do you like the structure?
4. Do you need an extra overview table or a visual (diagram) somewhere?

For each round: apply the changes, bump the status version (`Proposed (v2)` …), re-run the self-review and the Mermaid check, and log the round in the notes with a before/after table. When the user answers a question or overturns one of your decisions, update the constraint (C#) and, if it affects the design, the design rule (R#), then check what else depends on it.

When the user is satisfied, offer to set the status to **Accepted** and commit (follow the user's commit conventions).
