---
name: arch-requirements-analysis
description: Phase 1 of 3 of the architecture workflow (requirements → architecture options → ADR). Reads a software requirements document / user stories and turns it into an architecture-ready analysis — actors, functional areas, domain model, the architectural drivers (the "hard part"), gaps and ambiguities, missing non-functional requirements, clarifying questions that resolve every gap into a decision, and back-of-envelope sizing. Use this whenever the user asks to read, study or summarise requirements before designing a system, asks "what is this project about", wants to start an architecture discussion for a project in a data/ or requirements folder, or says they want to propose architectures but the requirements have not been analysed yet — even if they don't say "analysis".
---

# Architecture requirements analysis (phase 1 of 3)

Goal: turn a requirements text into a short, structured analysis that the architecture discussion (phase 2, skill `arch-options-proposal`) and the ADR (phase 3, skill `adr-authoring`) can refer to section by section.

The most valuable output of this phase is not the summary, it is the **gaps and how they get resolved**. In the reference run, the user's answers (two target scales, max team size, invite + join-request flow, deletion rules) changed every later decision. So get to the questions quickly and make them easy to answer.

## Step 0 – Start the notes file first

Before reading anything else, create a running notes file (default `output/Task1_conversation.md`, or the path the user names) and tell the user where it is. Keep it updated after **every** step of the conversation, not only at the end.

- It is a structured record of the *content* of the discussion, not a transcript: findings, options, the user's questions and decisions.
- Number the sections (`## 1. Requirements study`, `### 1.7 Gaps`) so later phases and the ADR can cite them ("context: §1.4–1.9").
- Header: date, participants, source requirements file, goal of the session. Use the template in `references/notes-template.md`.

### What goes into the file, and what stays in chat

The notes (and later the ADR) are read by people who care about the system, not about how the assistant worked. Write about the system and the decision only. Say process remarks to the user in chat, not in the file. That means no:

- "Method" lines, or any mention of skills, prompts, phases or tools used;
- logs of which files the assistant read or deliberately did not read, or claims such as "produced in one pass" / "independently of earlier outputs";
- quoted user prompts that contain working instructions ("use the skills…", "save as a Task 3 file…");
- comments on how the conversation went ("the user did not ask follow-up questions", "the questions were not asked one by one because…");
- instructions for the next review round;
- **unresolved assumptions** — see Step 3. The file contains decisions, not guesses.

## Step 1 – Read

- Read the whole requirements file. If the folder holds several projects, ask which one is assigned (don't guess).
- If assignment/task files exist next to it (e.g. `Task_*.md`), read them too — they tell you what the later phases expect, so the notes can be written to be reused.

## Step 2 – Write the requirements study (notes §1)

Produce these subsections, in this order:

1. **One-line summary** of the system.
2. **Stated main goals** (numbered, as the document states them).
3. **Actors / roles** table (`Role | Description`). Note when a role is scoped (e.g. admin *per team*).
4. **Functional areas** table: group user stories into areas, keep their IDs (`# | Area | User stories | Notes`). In *Notes*, flag cross-cutting consequences — e.g. "account deletion implies data erasure, which spreads into every other area".
5. **Main entities** – a first-cut domain model (bullet list, key fields only).
6. **Architectural drivers** – what makes this system hard. Most systems are CRUD plus one or two hard things (real-time push, high write volume, offline sync, payments, search, heavy media, strict consistency, multi-tenancy, integrations). Name them explicitly and say what they push the design towards. This is what the options in phase 2 will be judged on.
7. **Gaps and ambiguities** table: `# (G1…) | Observation | Why it matters for the architecture`. Look especially for:
   - contradictions between the description and the user stories (e.g. "invite" vs "join"),
   - implied but unlisted behaviour (notification triggers, who gets invited),
   - lifecycle edge cases (deleting an account / the last admin / an owner leaving),
   - missing details of features (polls: single/multi choice, anonymity, deadline; chat: history, search, edits),
   - **missing non-functional requirements** – see the checklist below. Almost every student-style requirements doc lacks them, and without a scale you cannot compare architectures.

### NFR checklist (ask about whatever is missing)
Scale (total users, concurrent users, peak vs average), group/tenant sizes, latency expectations, availability / acceptable downtime, data loss tolerance (backups), data retention, client platforms (web / mobile / both), delivery channels (in-app / email / push), security & privacy (GDPR, deletion), budget, **size of the development team**, deployment constraints (cloud/on-prem), integrations.

## Step 3 – Resolve every gap before building on it

Don't carry assumptions forward. A guess written into the notes quietly becomes a "fact" in the architecture and the ADR, and nobody remembers it was never agreed. Every gap must end up as a **decision** before phase 2 uses it.

**Ask first.** Put all the questions in chat in **one batch**, numbered by gap ID. For each, give your **recommended answer and a one-line reason**, so the user can reply "ok", override it, or say "you decide". Keep it short, and group small related gaps.

- **Always work with two scales: today and the growth target.** If the scale is unknown, propose both (e.g. *(a) today, < 50 users* and *(b) growth target, national level*). Never drop the growth target, even when only today's scale is funded: the architecture must be judged on whether it can reach (b) without a rewrite.
- Wait for the answers before continuing to sizing and phase 2.

**Key questions.** These change every later decision, so they always go **first** in the batch, marked as key questions:

| Key question | Why it matters |
|---|---|
| Who is the system for (one company, a school, the public, paying customers)? | Sets the scale today, privacy rules and expectations. |
| Scale today and the growth target (users, concurrent users). | Decides single server vs. distributed. |
| How many developers build and run it; is there an ops person? | Microservices or Kubernetes need a team that can run them. |
| Budget per month for infrastructure. | Rules options in or out. |
| Acceptable downtime and data loss (availability, backups). | Changes cost and the deployment (e.g. one server vs. two). |

**Product rules are the user's.** Gaps about behaviour the user sees (who can join a team, what happens when the last admin leaves, whether new members see old messages, poll anonymity, search) are product decisions, not technical ones. The reference run showed that a model's choices here differ from the user's (it picked "longest-standing member becomes admin" where the user wanted "admin must name a successor", and it missed chat search entirely). Ask them; if you must decide, list them in chat separately as product decisions.

**Decide yourself when the user leaves it to you.** That applies if the user says "you decide", skips a question, or asked for the whole job in one go without stopping. Then resolve the gap as well as you can: choose the option that fits the stated goals and drivers best, preferring the simpler option that doesn't close off later growth. Be as definite as a user decision would be.

**Write only the result into the file.** Use the table `1.8 Decisions on the gaps`, with columns `Gap | Decision | Reason`. A decision made by the user and one made by you look the same in the file. Don't write "assumption", "assistant assumption", "to be confirmed", "TBD", "presumably" or "probably". New facts the user volunteers get a `new` row.

**Report your own decisions in chat.** After writing them, list in chat the decisions *you* made (gap → decision), so the user can overturn any of them. Order the list: key questions first, then product decisions, then the rest, and for each key question say in one line what would change if the user answered differently. If they overturn something, update the notes and everything built on that decision.

## Step 4 – Derive sizing and the key insight

For **both** scales (today and growth target), do back-of-envelope numbers (users → concurrent connections → requests or messages per second → fan-out → storage per day/year), in one table with a column per scale.

- The inputs (share of users online at peak, messages per active user per minute, …) are decisions too. Ask for them together with the Step 3 questions, or choose sensible values yourself. Write them in the file as the **sizing basis**, not as "assumed".
- **Check the arithmetic and label peak vs average.** A real mistake in the reference run: "1.7k msg/s" and "17M msgs/day" were both written down, but 1.7k/s for a whole day is ~144M. Say which number is the peak and what the daily average is.

Then state the **key insight** in one or two sentences: what the hard problem *actually* is once the numbers are known. Example from the reference run: teams have at most 20 members, so the fan-out per message is tiny; at national scale the hard part is holding ~100k open connections and routing each message to the right node, not broadcasting. Insights like this decide the architecture later, so make them explicit.

## Step 5 – Hand off

Update the notes, give the user a short summary (drivers, key insight, the decisions you made yourself), and suggest moving on to phase 2 (`arch-options-proposal`).
