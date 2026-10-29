# Task 2 – Conversation Notes: Architecture Decision Record for Teamify

- **Date:** 2026-10-29
- **Participants:** Michal Zrutta (lead), Claude Code (assistant)
- **Input:** `output/Task1_conversation.md` (architecture discussion from Task 1), `data/Teamify.txt`
- **Output:** `output/ADR-001-teamify-architecture.md`
- **Goal of the session:** Turn the Task 1 architecture discussion into an Architecture Decision Record (ADR), then review and refine it until the user is happy with it.

The notes are a running record, not a word-for-word transcript. They are updated after each step of the discussion.

---

## 1. Session start

**User request:** Keep notes of the discussion in `output/Task2_conversation.md`. Read the Task 1 conversation and write an ADR.

**Assistant actions:**
- Read `Task_1.md`, `Task_2.md` and `Task_3.md`. Task 2 expects several review rounds (is the ADR informative enough, is something missing or extra, is the structure good, is an overview table or a diagram needed). Task 3 will reuse these notes to build a Skill, so the notes record *what was changed and why*.
- Read `output/Task1_conversation.md`. Its section 5 already lists the inputs for the ADR: the decision (modular monolith with a scale-out path), the context (sections 2.4–2.8), the options (section 3) and the consequences (pain points + Q&A in section 4).
- Created this notes file.

---

## 2. ADR v1 – first draft

**File:** `output/ADR-001-teamify-architecture.md`

**Format chosen:** a classic Nygard-style ADR (Context → Decision → Consequences) extended with MADR-style sections (decision drivers, considered options, pros/cons). Reason: the Task 1 discussion compared three options with explicit trade-offs, and a plain Nygard ADR has no place for that comparison.

**Decision recorded:**
- **Scale (a), < 50 users:** #1 Modular monolith on one VPS.
- **Scale (b), national:** #1 scaled out (N stateless instances, Redis pub/sub, PgBouncer, read replicas, partitioned chat, job queue) **plus an extracted Realtime Gateway** borrowed from #2.
- Status set to **Proposed**, because the user has not reviewed it yet.

**Structure of v1:**
| § | Section | Content taken from Task 1 |
|---|---|---|
| Header | Metadata table | Status, date, deciders, sources |
| 1 | Context | System summary, constraints C1–C8 (from clarifications in Task 1 §2.8), derived load at scale (b), key insight (team size ≤ 20 → connections, not fan-out, are the problem) |
| 2 | Decision drivers | Ranked list of 6 drivers (new: made explicit so the matrix can refer to them) |
| 3 | Considered options | One-line summary of #1, #2, #3 (3A Supabase, 3B AWS) |
| 4 | Decision | Per-scale table and a one-sentence rationale |
| 5 | Decision matrix | Task 1 §3.4 comparison table, rows linked to the drivers |
| 6 | Architecture overview | ASCII diagrams for scale (a) and scale (b), chat message flow |
| 7 | Design rules | 7 rules the decision commits to (module boundaries by tooling, invariants in one transaction with row locks, push after commit, catch-up by `seq`, UTC, …) |
| 8 | Consequences | Positive, negative / accepted trade-offs, risks + mitigations table |
| 9 | Rejected options | Why not #2 and #3, and what was kept from them |
| 10 | Revisit triggers | When to re-open the ADR (> 20–30 devs, Chat diverges, large teams, SLAs) |
| 11 | Open questions | Tech stack, team discovery, chat retention, poll anonymity |
| 12 | References | Links to the requirements and Task 1 notes |

**Things the assistant added beyond Task 1** (to check in review):
- The explicit ranking of decision drivers (Task 1 had criteria but no ranking).
- The scale (b) diagram (Task 1 described it only in text).
- Section 7 "Design rules" collected from pain points scattered across Task 1 §3.1 and §4.
- An assumption about a small dev team (1–8 devs), since the requirements give no team size.

**Questions for the user's review** (from the Task 2 assignment):
1. Is the ADR informative enough, or is something missing?
2. Is something extra (e.g. is §7 or §6.3 too detailed for an ADR)?
3. Is the structure good, or should it be shorter (e.g. split into one ADR per scale)?
4. Are the overview table and the ASCII diagrams enough, or is a different visual wanted (e.g. Mermaid / C4 diagram)?

---

## 3. Review rounds

### 3.1 Round 1 – find weak spots, simplify, Mermaid diagrams → ADR v2

**User request:**
- All commits must be made **without any Claude mark** (no co-author trailer). Saved as a standing preference.
- Go through the ADR, find weak spots and inconsistencies, keep it simple and precise.
- Add diagrams where helpful, in **Mermaid**.
- Keep **one ADR for both scales** and explain why.

**Weak spots and inconsistencies found in v1:**
| # | Problem in v1 | Fix in v2 |
|---|---|---|
| W1 | **Load numbers contradicted each other:** 1.7k msg/s and ~17M msgs/day don't match (1.7k/s for a whole day is ~144M). | 1.7k/s is now labelled as the *peak*. A sizing table says the daily average (~200/s) is assumed to be about 1/8 of the peak. |
| W2 | **Notifications were defined twice, differently:** rule 4 wrote inbox rows in the domain transaction, but scale (b) used a separate job queue. That queue would also be a dual write (DB + queue), which can lose jobs. | One rule (R5) for both scales: a **job table in PostgreSQL**, written in the same transaction. A worker expands it into inbox rows and pushes. The worker is a thread at (a) and separate processes at (b). |
| W3 | **The scale (b) diagram had no inbound path:** it didn't show how a chat message sent over a gateway WebSocket reaches the app. | The Mermaid diagram shows gateway → app (internal HTTP), and a sequence diagram shows the whole flow. |
| W4 | **Read replicas vs. catch-up:** catch-up reads from a lagging replica could miss the newest messages. Not mentioned in v1. | New rule R7: reads that must see recent writes go to the primary. Added to the risks table. |
| W5 | **How `seq` is generated was not defined**, and sender retries could create duplicate messages. | R3: a per-team counter row incremented in the same transaction. R4: a unique `client_msg_id` makes retries idempotent. |
| W6 | **"SPOF mitigated by backups" was wrong:** backups protect data, not availability. | Reworded in 8.2. |
| W7 | **The decision matrix didn't fully match the drivers:** some rows had no driver; "account deletion" duplicated "consistency"; "suits team size" was not a driver. | Every row has a driver column; duplicate rows were merged or removed; a short "reading the matrix" note was added. |
| W8 | **The scale-out path was a single sentence.** It didn't say *when* to add Redis, replicas or the gateway. | New section 5.4: 4 stages, each with an observable trigger, plus a Mermaid diagram. |
| W9 | **No explanation why both scales are in one ADR.** | New section 4.1: (a) and (b) are two deployments of the same codebase, and the design rules must apply from day one. |
| W10 | **Cost numbers looked like facts.** | Marked everywhere as rough, unverified estimates. |
| – | Minor: the empty "Supersedes" field, and the "sticky sessions" from Task 1 (not needed: a WebSocket stays on one node anyway). | Removed. |

**Diagrams added (Mermaid):**
1. **5.1 Modules and allowed dependencies:** makes rule R1 concrete. `teams` is the only owner of membership data.
2. **5.2 Scale (a) deployment.**
3. **5.3 Scale (b) deployment** with the Realtime Gateway, Redis, PgBouncer and replicas.
4. **5.4 Scale-out path:** stages 0 → 3, with triggers, plus the "revisit" exit.
5. **5.5 Chat message flow:** a sequence diagram valid for both scales.

All five diagrams were test-rendered with Mermaid 11.4.1 in the browser: no syntax errors. One subgraph title that was cut off was shortened.

**Simplifications:**
- Design rules and the risks table no longer repeat each other. The rules (R1–R9) are a table with a "protects" column linking to the drivers.
- A per-scale comparison table (4.2) replaces the long prose.
- Status changed to **Proposed (v2)**.

### 3.2 Round 2 – open questions answered → ADR v3

**User question: should we discuss the tech stack now?**
Assistant's recommendation: **not inside ADR-001.** An ADR should record one decision. ADR-001 is about the architectural style and is deliberately stack-agnostic; Task 1 never discussed languages or frameworks. The stack is its own decision, ADR-002, which builds on ADR-001. ADR-001 now lists only what the stack must support: PostgreSQL full-text search and partitioning, Redis, and WebSockets on a long-running server. Whether to write ADR-002 in this session is the user's call.

**User answers to the open questions:**
| Question | Answer | Recorded as |
|---|---|---|
| How does a user find a team? | They get a **code** from someone, or click an **invite link**. | C7 + rule R14 |
| Are poll votes anonymous? | **Yes.** | C8 + rule R13 |
| Chat retention | The **whole chat is kept**, and you must be able to **search words** in it. It **loads in small portions**, like WhatsApp. | C9 + rules R10–R12, new diagram 5.6 |

**Assistant's interpretation and assumptions (to confirm):**
- A code or link creates a **join request** that the admin accepts. It doesn't add the user directly. This keeps it consistent with the join-request flow from Task 1.
- "Anonymous" means anonymous in the product. The voter id is still stored, because it is needed for "one vote per member" and "change your vote", but no API or admin view exposes it.
- "The chat as a whole" means **new members also see history from before they joined.** Listed as an open question.
- Search is scoped to **one team's chat**.

**Design changes in the ADR:**
- **Partitioning changed from time to `hash(team_id)`.** Task 1 proposed time partitioning, mainly so old data can be dropped. With no retention limit, nothing is ever dropped, and every chat query (page, catch-up, search) names one team. Hashing by team means each query touches one partition.
- **Paging (R10):** keyset pagination by `seq` (`beforeSeq` / `afterSeq` / `aroundSeq`), never `OFFSET`, so page 1 and page 10,000 are equally fast. `aroundSeq` lets a search hit open in the middle of the history.
- **Search (R11):** PostgreSQL full-text search with a team-scoped GIN index (`btree_gin` on `(team_id, tsvector)`), using the `simple` configuration plus `unaccent` because messages mix languages and diacritics. A separate search engine (OpenSearch) is only a **revisit trigger**, not part of the decision. That avoids another system to run.
- **Sizing:** added storage growth of ~2–3 TB/year at scale (b). The key insight now also names "history that only grows" as a hard problem.
- **New diagram 5.6:** a sequence diagram for opening the chat, scrolling up, searching and jumping to a hit.
- Two new risks: slow paging/search on large history, and a leaked team code.
- Open questions reduced to: the tech stack (→ ADR-002) and whether new members see older history.
- Status changed to **Proposed (v3)**. All 6 Mermaid diagrams render without errors (Mermaid 11.4.1).

### 3.3 Round 3 – chat history visibility

**User answer:** new members **cannot** see messages sent before they joined. The user wasn't sure whether this belongs in an ADR.

**Assistant's view:** the rule itself is a product rule, but it has an architectural consequence, so one line belongs in the ADR. Every chat read path (pages, reconnect catch-up, search) must apply it. If each endpoint filters on its own, one of them will eventually leak old messages. The ADR fixes *where* the rule is enforced, not the UI.

**Changes:**
- C9 extended: "New members see only messages sent after they joined."
- New rule **R15:** the membership stores `history_from_seq` (the team's chat `seq` at join or re-join). The chat module applies `seq > history_from_seq` in one place for every read.
- Diagram 5.6: the first page query now shows the filter.
- Open questions: only the tech stack (→ ADR-002) remains.

**User question: is anything more needed for Task 2?**
The assignment asks for (1) a record of the conversation, (2) the final ADR, and (3) several review rounds. All three are done: v1 → v2 (weak spots, Mermaid) → v3 (open questions) → v3 + R15. Remaining optional steps: a final read-through by the user, setting the status to **Accepted**, and committing. ADR-002 (tech stack) is optional and not required by the assignment.

### 3.4 Round 4 – shorter, one target scale, plain language → ADR v4

**User feedback:**
- New members don't see old messages (confirmed; already in the ADR).
- The ADR is **too long**.
- Change the framing: design for **fewer than 50 users, with the option to scale in the future**. Choose **one** model and explain why the others were rejected (that part is fine as it is).
- **Decision drivers are good** and should stay.
- The decision section **mixes scale (a) and (b)** and is **too technical**. The user didn't understand why "the scale (a) decision is made because of scale (b)", and wants technical details explained.
- Unknown terms: "Realtime Gateway fleet", "cross-node delivery".
- **Keep the tech stack out of the ADR completely.** Open questions may stay, but only those related to this ADR. References are good.

**What changed in v4:**
| Area | v3 | v4 |
|---|---|---|
| Framing | Two equal scales, (a) and (b), everywhere | **One target: < 50 users today**; growth is a *future option* (C1) |
| Length | ~350 lines, 6 diagrams, 15 rules | **~265 lines, 4 diagrams, 12 rules** |
| Decision | Per-scale table full of infrastructure terms | One-sentence decision, a plain "why" list, then **4.2 "How we keep the option to grow"** |
| "(a) because of (b)" | Abstract statement | A concrete example: if messages were kept only in the app's memory, a second app copy could not see them and growth would need a rewrite. "Save first, then send" avoids that at no cost today. |
| Growth path | Stages with technical triggers | 3 steps, each with "what we add" and "why, in plain words". Cross-node delivery is explained with the Redis "message board" example. |
| Jargon | Used without explanation | Explained where it first appears, plus a **glossary** (§10) |
| Design rules | Technical only | Table with **plain rule + technical detail + why** |
| Scale (b) material | Sizing table, scale (b) deployment diagram, partitioning and replica rules | Removed or reduced to growth steps 1–3 |
| Comparison | 11 rows incl. costs at both scales | **One row per decision driver (D1–D6)** |
| Chat diagrams | Two sequence diagrams (send; load/search) | One combined diagram |
| Open questions | Tech stack, history visibility | **Tech stack removed.** Two ADR-related questions: is downtime of the single server acceptable, and is up to 24 h of data loss with daily backups acceptable? |

**Verification:** all 4 Mermaid diagrams render (Mermaid 11.4.1). One problem was found and fixed: in sequence diagrams Mermaid cuts text after `#`, so message numbers like `#101` disappeared. They are now written as `no. 101`. The growth diagram was switched from left-to-right to top-to-bottom, because it was too wide to read.
