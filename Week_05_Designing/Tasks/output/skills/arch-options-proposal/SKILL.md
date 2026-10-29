---
name: arch-options-proposal
description: Phase 2 of 3 of the architecture workflow (requirements → architecture options → ADR). Proposes at least three genuinely different architectures for a system described by requirements, explains each one with a diagram, a step-by-step flow of the hardest use case, pros and the painful low-level implementation details, answers deep-dive questions, builds a scored comparison table and picks a winner (per target scale) with runner-up, rejected options and an evolution path. Use this whenever the user wants to discuss, propose, brainstorm or compare architectures / architectural styles / system designs (monolith vs microservices vs serverless, etc.), asks "how would you build this system", wants trade-offs or a recommendation between designs, or wants to choose an architecture before writing an ADR.
---

# Architecture options – propose, discuss, choose (phase 2 of 3)

Goal: give the user a discussion they actually understand — three or more real alternatives, the painful parts of building each, an honest comparison and a clear recommendation — and leave notes the ADR (phase 3, skill `adr-authoring`) can be written from.

## Step 0 – Prerequisites and notes

- Keep (or create) the running notes file — usually the same file as phase 1 (`output/Task1_conversation.md`). Update it after every step. Skeleton: `../arch-requirements-analysis/references/notes-template.md`, sections 2–4.
- The file records the system and the decision, not how the assistant worked. Don't mention skills, phases, the method, which files were or weren't read, "one pass" or "independent of earlier outputs". Don't comment on the conversation either ("the user asked no follow-up questions"). Say such remarks in chat if they matter.
- Don't build on assumptions. If a choice depends on something the requirements and the gap decisions don't settle, ask the user (with your recommendation), or decide it yourself if they leave it to you. Write it into the notes as a decision, never as "assuming…".
- You need the architectural drivers, the target scale(s) and the key insight from phase 1. If the requirements have not been analysed, run the `arch-requirements-analysis` workflow first (at least drivers, gaps and scale questions). Proposing architectures without a scale makes the comparison meaningless.

## Step 1 – Choose the options

Propose **at least three options that differ in kind** — in how the system is deployed, who owns the data, and who runs the infrastructure — not three flavours of one idea. A good default spread:

1. **The simplest thing that works** (usually a modular monolith) — typically the best fit for small scale.
2. **The classic "big scale" answer** (usually microservices + event bus, with a dedicated real-time/connection layer if needed).
3. **A different operating model** (serverless / BaaS, or another style from the catalogue) — often cheap at small scale, with different limits at large scale.

Say up front which option you expect to fit which scale. If concrete products differ a lot inside one style, give named variants (e.g. *3A Supabase/Firebase*, *3B AWS Lambda + API Gateway WebSocket*). For more styles and their typical pain points, read `references/styles-catalogue.md`.

## Step 2 – Describe each option with the same template

Use the same structure for every option so they can be compared side by side:

- **Shape:** components, data stores, deployment, rough monthly cost (marked as a rough estimate) **for both scales, with its basis**: what is included (e.g. "1 VPS with daily `pg_dump`" vs. "VM + managed PostgreSQL with point-in-time recovery") and which pricing units it comes from (per node, per connection-minute, per million messages). Without the basis, two runs give costs that differ 10× for the same option (€5–10 vs. ≈ €100/month for the same monolith) and nobody can tell why.
- **Diagram:** a small ASCII (or Mermaid) diagram showing clients, components, stores and the real-time path.
- **How the hardest driver works:** a numbered step-by-step flow (e.g. one chat message from send to delivery, including what happens when the recipient is offline).
- **Pros.**
- **Painful parts (low level)** — the most important section. Name concrete failure modes and the standard fix for each, e.g.: missed pushes on reconnect → client keeps `lastSeq` and catches up via REST; dual write DB + broker → transactional outbox + idempotent consumers; authorization data owned by another service → sync call vs. eventually consistent replica; multi-service business operation → saga; message ordering → partition key + per-group sequence numbers; WebSocket auth, heartbeats, LB idle timeouts, reconnect storms, connection draining on deploy; vendor limits (max connection time, idle timeout, cold starts, per-message pricing); business rules scattered across DB policies and functions.
- **Honest caveat:** when this option is overkill or which problem it really solves. E.g. microservices mainly solve *organisational* scale (many dev teams), not load — with small groups the load at national scale can be modest.

The user's job here is to understand the options, so explain jargon the first time it appears and keep a running glossary in the notes.

## Step 3 – Deep-dive questions

The user is expected to probe ("do I really understand this?"). Answer briefly in chat and record each Q&A in a short form in notes §3. If the user has no questions, offer these four, which produced the most insight in the reference run. If the user wants everything in one go, answer them directly and title the section "Deep-dive questions", with no remark on who asked or why.

1. **Precise definitions** of the styles involved (monolith, modular monolith, microservices, event-driven, serverless/FaaS, BaaS) plus a mini glossary (WebSocket, pub/sub, outbox, saga, eventual consistency, presence…).
2. **One key request end-to-end** through the most complex option, as numbered steps: auth on connect → validation → persistence with ordering → publish → routing to the recipient's node → offline catch-up → dedupe.
3. **The hardest cross-cutting business operation** (e.g. deleting an admin's account, transferring ownership) in **every** option: one DB transaction with row locks vs. a saga with a pivot step vs. a DB function / step function. This shows the consistency cost of each style very concretely.
4. **"Can the simplest option reach the large scale? What breaks first?"** — an ordered list of bottlenecks with the fix for each (single process / in-memory state → DB connections and table size → synchronous side work → deploys → organisation). This usually reveals that a scaled-out simple option or a hybrid beats the "big" option.

## Step 4 – Compare

Build a comparison table (notes §2.4): rows = criteria, columns = options, scores 1–5 **with a few words of justification in the cell**, best score in bold. Derive the criteria from the drivers so the ADR can later map one row to one driver. Typical rows: fit for each scale, time to MVP, development complexity, operations effort, consistency of business rules, real-time reliability, privacy/deletion complexity, vendor lock-in, local testability, independent scaling / fault isolation, dev-team size it suits, monthly cost per scale. Mark costs as rough, unverified estimates.

## Step 5 – Choose

Give a recommendation, not a survey — but **the choice is the user's**. Present the recommendation and ask the user to confirm it or pick another option before writing notes §4 and before the ADR. If the user asked for the whole job in one go, go with your recommendation, write "chosen: #N (recommended)" in §4, and tell the user in chat that choosing another option means rewriting §4 and the ADR.

For each target scale:

- **Winner** and the 2–4 reasons that decide it (linked to drivers).
- **Runner-up** and the condition under which you would pick it instead.
- **Rejected** options and why.
- **Hybrids:** what is borrowed from a rejected option (e.g. extract only the real-time gateway from the microservices option).
- **Triggers to move on:** observable signals (dev headcount, one module's load or release cadence diverging, SLA changes).
- **Evolution path:** if one option can grow into the large-scale design by *adding infrastructure instead of rewriting*, say so — continuity across scales was the strongest argument in the reference run.

## Step 6 – Close the session

Write notes §4: outcome, and an **"Input for the ADR"** list — decision, which sections hold the context, options, consequences (pain points + Q&A). Then suggest phase 3 (`adr-authoring`).

Don't leave "open items" in the notes. If something is still undecided (e.g. how users find a team, chat retention), ask the user in chat with your recommendation. If they leave it to you, decide it yourself. Either way, record it as a decision with a reason, and tell the user in chat which ones you decided yourself.
