# Task 3 – Report: architecture work with and without the skills

## 1. Goal and setup

From the Task 1 and Task 2 conversations I had the assistant build three skills for one workflow – requirements → architecture options → ADR. They are stored in [`output/skills/`](skills/README.md); to use them, copy them to `.claude/skills/`, see the [skills README](skills/README.md).

| Skill | Files | Produces |
|---|---|---|
| [`arch-requirements-analysis`](skills/arch-requirements-analysis/SKILL.md) | `SKILL.md`, `references/notes-template.md` | actors, functional areas, domain model, architectural drivers, gaps and decisions on them, sizing |
| [`arch-options-proposal`](skills/arch-options-proposal/SKILL.md) | `SKILL.md`, `references/styles-catalogue.md` | at least 3 different architectures, painful parts, deep-dive Q&A, scored comparison, choice and growth path |
| [`adr-authoring`](skills/adr-authoring/SKILL.md) | `SKILL.md`, `assets/adr-template.md`, `references/review-checklist.md`, `scripts/mermaid_check.py` | ADR from a template, self-review checklist, Mermaid render check, review log |

Then I repeated Task 1 and Task 2 for Teamify in a new session. The agent was told to read only `data/Teamify.txt` and the skills. It was not allowed to read the previous outputs or the Task 1 and Task 3 assignments; it read the Task 2 assignment text. It produced two files in one turn:
- `output/Task3_architecture_discussion.md` – requirements study, 3 options, comparison, deep-dive Q&A, ADR review log;
- `output/Task3_ADR-001-teamify-architecture.md` – the ADR.

## 2. Tuning the skills – three test runs

The skills needed three runs before the output was usable.

| Run | Output | What was wrong | What I changed in the skill |
|---|---|---|---|
| 1 | one file, 669 lines | Lots of information nobody needs: a "Method" line naming the skills, and a statement that the file was "produced in one pass… deliberately not read" the earlier outputs. | The files describe the system and the decision only; remarks about the process go to the chat. |
| 2 | 2 files (315 + 277 lines) | The agent made assumptions and wrote them into the ADR ("**Assumption.**" next to scale, team size and developer count). I should be the one who says what is correct, not the agent. | Every gap must become a decision: the agent asks, or – if I leave it to it – decides and lists its decisions in chat so I can overturn them. |
| 3 | 2 files (336 + 260 lines) | No process talk and no assumptions in the files. But the agent decided everything itself, including key inputs and product rules (see §4). | Changes after this report (§6). |

In the third run the agent made the decisions itself and listed all of them in the chat so I could overturn them. I see this as a good and quick approach. If it had only asked questions, I would have been left without any files. This way I get the files right away, I can see what is probably the best decision, and I correct only what I disagree with.

## 3. Effort – before and after the skills

| | Without skills (Task 1 + Task 2) | With skills (run 3) |
|---|---|---|
| Sessions / my prompts | 2 sessions, 9 prompts, over 2 days | 1 session, 1 prompt |
| Model working time | ≈ 16 min | ≈ 6 min |
| Active session time (pauses capped at 5 min) | ≈ 59 min | ≈ 6 min |
| Tool calls | 93 | 20 |
| ADR versions until acceptable | 4 (v1 → v4) | 1 (v1, 260 lines, 3 Mermaid diagrams, all render) |

Times are taken from the session logs.

**Caveat:** this does not include the time to build and tune the skills – one authoring session plus three test runs. For this one system the total was not faster. The gain comes with the next system.

## 4. Comparison of the results

### 4.1 What stayed the same
- **The same three options:**
  - #1 modular monolith;
  - #2 microservices + event bus + real-time gateway;
  - #3 serverless/BaaS, with Supabase and AWS variants.
- **The same winner:** a modular monolith on one PostgreSQL database.
- **The same growth path:** Redis pub/sub → separate real-time gateway → read replicas → moving a module out into its own service.
- **The same deep-dive questions:**
  - definitions of the styles;
  - one chat message end-to-end;
  - account deletion of the last admin in every option;
  - "can the monolith reach national scale?".
- **The same growth target:** 1,000,000 users and 100,000 online at peak. The scale today differs: I chose fewer than 50 users, the agent decided 2,000 users with 200 online. That is still reasonable for a first version and close to my choice.

### 4.2 Quality of the first ADR version
All ten weak spots I found in ADR v1 during Task 2 (review round 1) were already avoided in the new v1:
- message rates that contradicted each other;
- notifications defined twice, in two different ways;
- undefined sequence numbers and duplicate messages on retry;
- missing rule that catch-up reads must not use a lagging replica;
- "single point of failure mitigated by backups";
- comparison rows not matching the decision drivers;
- growth path without triggers;
- costs presented as facts;
- `#` cutting off text in Mermaid sequence diagrams;
- no glossary.

I am especially happy about the glossary. In Task 2 I had to complain about jargon before it appeared (v4); now it was there from v1.

The self-review checklist in the skill still found 7 problems before the agent showed v1, including a new inconsistency (team deletion described in two different ways). The checklist works, but the model does not write a correct ADR without it.

### 4.3 What differed – product decisions
Where I had answered the questions myself in Task 1/2, the agent now decided on its own, and several answers differ:

| Topic | My decision (Task 1/2) | Agent's decision (Task 3) |
|---|---|---|
| Team size | max 20 | max 50 |
| Joining a team | invitation, or code/link → join request that the admin approves | invitation, or code that joins directly |
| Last admin deletes their account | must name a successor first | longest-standing member becomes admin automatically |
| New members and old chat messages | cannot see them | see the full history |
| Chat search, loading in small portions (like WhatsApp) | required | missing |
| Email | password reset only | also account verification and invitations |
| Availability / backups | left as open questions (daily backups, up to 24 h data loss) | 99.5 % availability, at most 5 min data loss |
| Development team | assumption: 1–8 developers | decided: 3 developers, ≤ €150/month |

**Finding:** the skill reproduces the architecture reliably, but it cannot guess product rules. The architecture did not change because of these differences. However, the ADR would have been wrong in details I care about (search, history visibility, admin hand-over).

### 4.4 Costs
The architecture was the same, but the estimated monthly costs differed a lot:

| Option | Task 1/2 | Task 3 | Why |
|---|---|---|---|
| Monolith, today | €5–10 | ≈ €100 | Task 1: one VPS with a daily `pg_dump` for < 50 users. Task 3: a VM + managed PostgreSQL with point-in-time recovery for 2,000 users. |
| Microservices, today | €150–300+ | €1,000–1,500 | Task 3 counted 7 managed databases and tracing. |
| Serverless, growth scale | €10k+ | €3–6k | Task 3 calculated it from pricing units (≈ 4.3 billion connection-minutes and ≈ 1 billion messages per month). Task 1 left it "to be verified". |

The differences come from different inputs, not from chance. All figures are rough and unverified. Without knowing what a cost includes, two estimates of the same option can't be compared.

## 5. My observations

**Positive**
- One prompt in about 6 minutes and 20 tool calls did the same job as Task 1 and Task 2 together, and the first version was already at the quality of the final one from Task 2.
- The output is well structured, mostly pretty, compact and readable: tables, Mermaid diagrams, plain language, a glossary.
- No process talk and no hidden assumptions in the files (after runs 1 and 2).
- Decisions are listed in chat, so I can overturn them quickly.

**Negative**
- **I never chose the option – the agent chose it.** That works for me now, but as I get more experienced I want to make that choice myself. (In Task 1 the agent also picked the winner, but I had a round of questions before it.)
- **Important questions were not asked:**
  - how many people will build and run the app;
  - for whom we build it;
  - what is expected of it (availability, budget).

  The agent decided them reasonably, but they change every later decision.
- **Decisions made by the agent are not marked in the files.** In the files they look like my decisions, so I have to read the chat list carefully.
- **The growth target was not visible enough in the ADR.** It was in the discussion notes (a sizing table for both scales) and in the ADR's growth steps with concrete triggers. In the ADR itself it was only one sentence in the constraints. At first reading the ADR looked like it was designed only for 200 people online. That is not true: the design is checked against 100,000 online, and that was also the framing I asked for in Task 2 ("fewer than 50 users with the option to scale in the future").

## 6. Changes to the skills after this report

| Skill | Change |
|---|---|
| `arch-requirements-analysis` | **Always two scales**, today and the growth target; the growth target is never dropped. **Key questions go first:** who the system is for, scale, number of developers, budget, acceptable downtime and data loss. **Product rules belong to the user** (joining, last admin, history visibility, search); if the agent must decide them, it lists them separately in chat. |
| `arch-options-proposal` | **The user chooses the option.** The agent recommends and asks. When everything is done in one go, the notes say "chosen: #N (recommended)". **Costs** for both scales state what they include and which pricing units they come from. |
| `adr-authoring` | Template has a **"today vs. growth target" sizing table**, C1 names both numbers, and every growth step shows **the size it makes possible**. Checklist: growth target visible; costs state what they include. |

## 7. Summary
- **Faster:** one prompt and about 6 minutes replaced 9 prompts and 4 ADR review rounds. This doesn't count the one-time effort of building and tuning the skills (one authoring session plus three test runs).
- **Better first version:** all ten weak spots from the Task 2 review were avoided in v1, and the glossary was there without asking.
- **Same architecture:** the same options, winner and growth path. The scale was nearly the same: < 50 vs. 2,000 users today, 1,000,000 users at the growth target in both.
- **Weak point:** in the third run the agent decided everything without confirmation, including product rules, and some of them differ from mine (search, history visibility, admin hand-over).
- **Next time:** answer the key questions and product rules first and choose the option myself; let the skills do the rest in one pass