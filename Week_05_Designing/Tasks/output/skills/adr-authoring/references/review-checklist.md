# ADR self-review checklist

Every item comes from a real problem found while reviewing an ADR (v1 → v4 in the reference run). Check each one before showing a version to the user, and mention what you fixed.

## Consistency
- [ ] **Numbers add up.** Recompute derived numbers (per second ↔ per day ↔ per year). Label peak vs average. *(v1 had 1.7k msg/s and 17M msgs/day, which contradict each other.)*
- [ ] **Each mechanism is defined once.** Search for the same concept described two ways in different sections. *(v1 wrote notifications inside the DB transaction in one place and through a separate job queue in another — and that queue was itself a lossy dual write.)*
- [ ] **Identifiers and keys are defined:** how sequence numbers are generated, what makes retries idempotent.
- [ ] **Mitigations actually mitigate the risk named.** *(v1: "single point of failure mitigated by backups" — backups protect data, not availability.)*
- [ ] **Hidden interactions between rules:** e.g. catch-up reads from a lagging read replica can miss the newest messages → reads that must see recent writes go to the primary.

## Structure
- [ ] **Comparison rows map 1:1 to the decision drivers.** No row without a driver, no duplicate rows, no criterion that is not a driver.
- [ ] **Design rules and risks don't repeat each other.** Rules carry a "why" column pointing to drivers/constraints.
- [ ] **Growth / evolution path has steps with observable triggers**, not a single sentence.
- [ ] **One decision, one target scale.** Future scale appears as an option with growth steps, not as a second decision. Tech stack is out.
- [ ] **The growth target is visible:** the sizing table shows today and the growth target, C1 names both, and the last growth step reaches the growth target. *(A reviewer read a v1 as "designed only for 200 people online" because the growth numbers were only in the discussion notes.)*
- [ ] **Costs say what they include** (server type, managed vs. self-run database, backup level), so costs from different documents can be compared.
- [ ] **No assumptions and no open questions left in the document.** Search for `assum`, `to be confirmed`, `TBD`, `presumably`, `probably`, `open question`. Each hit gets resolved: ask the user, or decide yourself if they left it to you, then write it as a constraint or decision.
- [ ] **No process talk in the document:** no mention of skills, method, prompts, files read/not read, "one pass", what the user did or didn't ask, or next-round instructions. Search for `skill`, `pass`, `the user`, `assistant actions`. Process remarks go to chat.
- [ ] No empty metadata fields (e.g. "Supersedes: –"); no leftovers that are no longer true (e.g. sticky sessions when a WebSocket stays on one node anyway).

## Readability
- [ ] Every technical term is explained at first use and in the glossary.
- [ ] Abstract statements have a concrete example ("if X lived only in memory, then …").
- [ ] Costs and other estimates are marked as rough / unverified.
- [ ] Length is reasonable (~200–270 lines); cut repetition first.

## Diagrams (Mermaid)
- [ ] Every block renders (run `scripts/mermaid_check.py`).
- [ ] Diagrams show **all** paths, including the inbound one (how a message sent over a gateway WebSocket reaches the app), not only outbound.
- [ ] In `sequenceDiagram` text, **`#` cuts off the rest of the line** — write `no. 101`, not `#101`.
- [ ] Long flowcharts use `flowchart TB`; `LR` gets too wide to read.
- [ ] Subgraph titles are short (long ones get clipped); use `<br/>` for line breaks inside node labels; quote labels containing `()`, `:` or `/`.
- [ ] 3–4 diagrams are usually enough: deployment, module borders, the hardest flow, growth path.
