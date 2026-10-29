# Teamify – Architecture discussion notes (Task 3)

- **Date:** 2026-10-29
- **Participants:** Michal Zrutta (lead), Claude Code (assistant)
- **Source requirements:** `data/Teamify.txt`
- **Output ADR:** `output/Task3_ADR-001-teamify-architecture.md`
- **Goal:** Understand the Teamify requirements, compare at least three different architectures, choose one and record the decision in an ADR.

---

## 1. Requirements study – what Teamify is

### 1.1 One-line summary
Teamify is a web application for personal task management and small-team collaboration: personal agenda, teams with a shared agenda of events, team group chat, polls and real-time notifications.

### 1.2 Stated main goals
1. **Task management** – create and manage personal and shared tasks.
2. **Team management** – create teams and invite members to join.
3. **Real-time notifications** – users are told about changes as they happen.
4. **Real-time chat** – team members chat with each other live.

The description also mentions shared events and survey creation (polls).

### 1.3 Actors / roles
| Role | Description |
|---|---|
| Visitor | Not signed in. Can register, log in, reset a password. |
| User | Signed-in person. Owns a profile, a personal agenda and personal tasks; can create and join teams. |
| Team member | A user **within one team**. Sees the team agenda, chats, votes in polls, answers event invitations. Role is per team. |
| Team administrator | A team member with admin rights **in that team** (the creator is the first one). Edits/deletes the team, manages admins, creates events and polls. |
| System | Sends notifications and emails (password reset, invitations). |

### 1.4 Functional areas (user stories grouped)
| # | Area | User stories | Notes |
|---|---|---|---|
| A1 | Account & identity | 1–7 | Account deletion (7) erases personal data in **every** other area – the most cross-cutting story. Password reset (6) needs email delivery. |
| A2 | Notifications | 8 (implied by 16, 18, 27–30) | Consumer of changes from all other areas; needs a stored inbox **and** a real-time push. |
| A3 | Personal agenda & tasks | 9, 11–14 | Plain CRUD, owned by one user. |
| A4 | Teams & membership | 15–20, 25, 26 | Rule "a team always has an admin" (19, 20, 26, 18). Description says *invite*, story 16 says *join* – contradiction. Team deletion removes everything below it. |
| A5 | Shared events (team agenda) | 10, 27–31 | Event = shared task. Each invited member answers yes/no (28). Completion set by admin (31). |
| A6 | Team chat | 21 | Real time, ordering, history, offline members. |
| A7 | Polls | 22–24 | One vote per member, concurrent votes, live results. |

### 1.5 Main entities (first-cut domain model)
- **User** – id, email, password hash, name, verified flag.
- **Session** – refresh token (revocable), user id, expiry.
- **PersonalTask** – id, owner id, title, description, start/due, completed at.
- **Team** – id, name, description, invite code, last chat sequence number.
- **Membership** – team id, user id, role (member/admin), joined at.
- **Invitation** – team id, invited user/email, invited by, status.
- **Event** – id, team id, title, start, end, completed at, created by.
- **EventResponse** – event id, user id, status (pending/accepted/declined).
- **ChatMessage** – team id, sequence number, client message id, sender id, text, deleted flag, created at.
- **Poll / PollOption / Vote** – poll: question, single/multi choice, closes at; vote: poll, option, user.
- **Notification** – id, user id, type, payload, created at, read at.

### 1.6 Architectural drivers
Most of Teamify is CRUD. The hard parts are:
1. **Real-time push** of chat messages and notifications to users who are online, without losing anything for users who are offline or briefly disconnected. This needs long-lived connections (WebSockets), a "save first, then push" rule and a catch-up on reconnect.
2. **Team-scoped authorization everywhere.** Almost every read and write is "is this user a member/admin of this team?". A member who leaves or is removed must stop receiving pushes immediately.
3. **Business rules that span several areas:** "a team always has at least one admin", account deletion that touches every area, team deletion that cascades. They push towards one database and short transactions.
4. **Notification fan-out from many triggers** (invitations, events, polls, admin changes) – every area produces notifications.
5. **Small team and budget** (see G13): the design must be cheap to build, run and test.

### 1.7 Gaps and ambiguities found
| # | Observation | Why it matters for the architecture |
|---|---|---|
| G1 | No scale given (users, concurrent users). | Decides single server vs. distributed; without it options can't be compared. |
| G2 | No maximum team size. | Decides fan-out per message and size of one transaction. |
| G3 | "Invite members" (goals) vs. "join an existing team" (story 16). How does a user find a team? | Decides whether a team directory/search is needed and which flows create memberships. |
| G4 | Who is invited to an event (story 28)? | Decides how many response rows and notifications one event creates. |
| G5 | Notification triggers and channels (in-app, email, mobile push?) not listed. | External integrations, delivery guarantees. |
| G6 | Last admin leaves the team or deletes the account. | Needs an invariant enforced under concurrency. |
| G7 | Account deletion: what happens to messages, events and polls the user authored? | Scope of the deletion operation across areas; GDPR. |
| G8 | Chat details missing: history for new members, edit/delete, attachments, retention. | Storage, read filters, file storage. |
| G9 | Poll details missing: single/multi choice, anonymity, deadline, changing a vote. | Data model and concurrency of votes. |
| G10 | Personal agenda: only personal tasks, or also team events? | Cross-module read. |
| G11 | Event completion: per event or per member? | Data model. |
| G12 | Client platforms not stated. | API style, push channels. |
| G13 | No non-functional requirements: availability, backups, latency, security/GDPR, dev team size, budget, hosting. | All options are judged on these. |
| G14 | Team deletion: what happens to chat, polls, events. | Size and form of the deletion operation. |
| G15 | Time-based reminders ("event starts in 1 h")? | Would need a scheduler. |
| G16 | Login method not stated (password, SSO?). | Identity component. |

### 1.8 Decisions on the gaps
| Gap | Decision | Reason |
|---|---|---|
| G1 | Two target scales. **(a) Launch:** up to 2,000 registered users (one company or faculty), up to 200 online at the same time. **(b) Growth:** 1 million registered users, up to 100,000 online at peak. Only (a) is funded now. | Architectures differ by scale; (a) is realistic for the first year, (b) tests the growth path. |
| G2 | A team has at most **50 members**; a user can be in at most 20 teams. | Collaboration tool for small teams; keeps fan-out and transactions small. |
| G3 | Membership is created only by **invitation** (admin invites a registered user or an email address; the user accepts) or by an **invite code/link** an admin generates and can revoke. Story 16 "join" = accept an invitation or use a code. **No public team directory.** | Teams are private; one membership-creation command for both paths. |
| G4 | An event invites **all current team members**; members who join later are not added to existing events. Each member answers accepted/declined (pending by default). | Max 50 response rows per event; simple and predictable. |
| G5 | **In-app notifications** (real-time push + stored inbox) for: team invitation, role change, member joined/left (to admins), event created/changed/deleted, poll created/closed, removed from team. Chat messages do **not** create inbox entries; they update an unread counter per team. **Email** only for account verification, password reset and invitations to an email address. No mobile push in v1. | Keeps the inbox useful; email only where the user may not be signed in. |
| G6 | A team always has **at least one admin**. The last admin cannot leave or demote themselves while other members exist. If the last admin deletes their account, the longest-standing member becomes admin; if there are no other members, the team is deleted. | Story 26 needs an admin; deletion must never block (GDPR). |
| G7 | Account deletion is immediate. Profile, sessions, personal tasks, notifications, invitations and event responses are deleted. Chat messages, events and polls the user authored stay with the team, shown as **"Deleted user"**. Votes stay as anonymous counts (user link removed). | Team content belongs to the team; personal data is removed. |
| G8 | Chat is **text only** (max 4,000 characters). Members see the **full team history**, including messages sent before they joined. Authors may delete their own message (shown as "message deleted"); no editing. History is kept until the team is deleted. | No file storage in v1; no per-member read filter needed. |
| G9 | Poll is single- or multiple-choice (set at creation), with an optional deadline; the admin can close it early. Members see **counts only**, not who voted. A member can change their vote until the poll closes. Options cannot be edited after the first vote. | Covers stories 22–24 with minimal rules. |
| G10 | The personal agenda shows personal tasks **and** team events the user accepted. | One view of "my time"; a read across two modules via their public interfaces. |
| G11 | Event completion is **per event**, set by an admin. | Story 31 says the admin checks it. |
| G12 | Responsive **web app** first. Server offers a REST API plus one WebSocket per signed-in browser tab, so mobile apps can be added later. | Smallest client effort; API stays reusable. |
| G13 | **Availability 99.5 %/month** (≈ 3.6 h downtime) at launch; short restarts during deploys are acceptable. **RPO ≤ 5 min, RTO ≤ 4 h** (managed database with point-in-time recovery). **Latency:** chat/notification reaches online members p95 < 1 s; API p95 < 300 ms. **Security:** GDPR, EU hosting, HTTPS, password hashing (Argon2id). **Team:** 3 developers, no dedicated ops. **Budget:** ≤ €150/month infrastructure at launch. Managed cloud services are allowed. | Typical for a new product built by a small team. |
| G14 | Team deletion (admin) removes the team with its memberships, events, responses, polls, votes and chat. Members get a notification first. | No orphan data; team content has no owner after deletion. |
| G15 | No time-based reminders in v1. | Not in the user stories. |
| G16 | Email + password with email verification. Short-lived access token (15 min) plus a server-side refresh token that logout, password change and account deletion revoke. | Story 3 needs real logout; no SSO requested. |

### 1.9 Sizing

**Sizing basis:** 30 % of registered users are active on a given day; 10 % of registered users are online at peak; an active user sends 20 chat messages per day; at peak an online user sends one message per 2 minutes and makes one API request per 10 seconds; an average team has 15 members, of whom about one third are online; a stored message with indexes takes ~500 bytes.

| | (a) Launch | (b) Growth |
|---|---|---|
| Registered users | 2,000 | 1,000,000 |
| Open WebSocket connections (peak) | 200 | 100,000 |
| Chat messages per day | 600 × 20 = 12,000 | 300,000 × 20 = 6,000,000 |
| Chat messages/s – **average** | 12,000 / 86,400 ≈ 0.14 | 6,000,000 / 86,400 ≈ 69 |
| Chat messages/s – **peak** | 200 × 0.5/min ≈ 1.7 | 100,000 × 0.5/min ≈ 833 |
| Pushes/s at peak (≈ 5 online recipients per message) | ≈ 8 | ≈ 4,200 |
| API requests/s at peak | 20 | 10,000 |
| Chat storage | 6 MB/day ≈ 2.2 GB/year | 3 GB/day ≈ 1.1 TB/year |

Check: peak is about 12× average in both scales (1.7 / 0.14, 833 / 69), which fits a working-hours usage pattern.

**Key insight:** a team has at most 50 members, so one message fans out to at most 49 people. Teamify is never a broadcast problem. At launch the whole load fits easily on one server and one PostgreSQL database; the real difficulty is **correctness** (team-scoped authorization, the "≥ 1 admin" rule, deletion across all areas) and **reliable delivery** (save first, push second, catch up on reconnect). At growth scale the hard part becomes **holding ~100k open connections on many machines and routing each push to the machine where the recipient is connected**. About 1k writes/s stays within what one PostgreSQL primary handles, so the business data never has to be split across databases.

---

## 2. Architecture options

Expected fit: **#1** for launch, and as the growth base. **#2** only for growth scale with a large organisation. **#3** cheapest to start, with vendor limits at scale.

### 2.1 Architecture #1 – Modular monolith + PostgreSQL (fits launch; grows to growth scale)

**Shape:** One deployable application. Its code is split into modules by business area (Identity, Agenda, Teams, Events, Chat, Polls, Notifications, Realtime). Each module owns its tables in **one PostgreSQL database** and other modules call it only through its public interface. The app serves the REST API and holds the WebSocket connections itself. An **outbox table** plus an in-process relay delivers pushes and emails after commit. Managed PostgreSQL with point-in-time recovery; an email provider for transactional mail.
Rough cost: launch ≈ €100/month (one 4 vCPU VM + small managed PostgreSQL + email); growth ≈ €5–8k/month (10–20 app/gateway nodes, Redis, large PostgreSQL primary + replica). *Rough, unverified estimates.*

```
 Browser ──HTTPS/REST──┐
 Browser ──WebSocket───┤
                       ▼
        ┌──────────── Teamify app (1 process) ─────────────┐
        │ Identity │ Agenda │ Teams │ Events │ Chat │ Polls │
        │ Notifications │ Realtime (socket registry) │ Relay│
        └───────────────┬───────────────────────┬──────────┘
                        ▼                       ▼
              PostgreSQL (all modules,      Email provider
              own tables each + outbox)
```

**Hardest flow – one chat message:**
1. Browser sends `{teamId, clientMsgId, text}` over its WebSocket (authenticated at connect with the access token).
2. Chat module asks Teams: is the sender a member? (one indexed query).
3. One transaction: `UPDATE teams SET last_chat_seq = last_chat_seq + 1 … RETURNING` (row lock gives the next per-team sequence number), insert the message (`UNIQUE(team_id, client_msg_id)` makes retries harmless), insert an outbox row. Commit.
4. Sender gets an ack with the sequence number.
5. The relay picks up the outbox row (woken immediately after commit, polling every second as a backup), loads the current members, re-checks membership and pushes to every connected member's sockets.
6. An offline member stores nothing extra; the team's unread counter is `last_chat_seq − member's last_read_seq`.
7. On reconnect the browser sends its `lastSeq` per team and fetches the gap over REST (keyset pagination by seq).

**Pros:** one transaction for every business rule; one deployment, one database, one log; cheapest; easy to test locally (app + PostgreSQL); 3 developers can build it.

**Painful parts (low level):**
- **Module borders erode** (a quick join into another module's table) → architecture tests in CI that fail on cross-module table access or imports of non-public code.
- **Socket registry lives in memory** → fine for one process; with two processes a push must reach the other process → Redis pub/sub (or PostgreSQL `LISTEN/NOTIFY` for a few nodes). Must be planned now: the registry is only a cache, the DB is the truth.
- **Dual write** "commit to DB, then push" → lost push if the process dies between the two. With one process the sockets die too, the clients reconnect and catch up. The outbox row makes the push retryable once there are several processes.
- **Single point of failure** – one VM. Backups protect data, not availability; acceptable within 99.5 % (C6), with an automatic restart and a second instance as growth step 1.
- **Deploys disconnect everyone** → clients reconnect with jittered backoff and catch up; later rolling deploys with connection draining.
- **WebSocket details:** auth token in the first message (not in the URL), heartbeat every 30 s against load-balancer idle timeouts, token expiry while connected → re-auth message or close.
- **Long-running work in the request** (emails, team deletion) → the relay does it, not the request.

**Honest caveat:** it does not give independent deployment per module or isolation of failures: a bug that eats memory takes down chat and agenda together.

### 2.2 Architecture #2 – Microservices + event bus + real-time gateway (fits growth scale with many dev teams)

**Shape:** Services Identity, Agenda, Teams, Events, Chat, Polls, Notifications and a Realtime Gateway, each with its own database, on Kubernetes. Services talk over HTTP/gRPC for queries and publish events to a broker (Kafka or NATS JetStream). The gateway holds all WebSockets and keeps a `userId → gateway node` registry in Redis. An API gateway handles auth.
Rough cost: launch ≈ €1,000–1,500/month (managed Kubernetes, broker, 7 databases, tracing); growth ≈ €12–20k/month. *Rough, unverified estimates.*

```
 Browser ─REST─► API gateway ─► Identity │ Agenda │ Teams │ Events │ Chat │ Polls │ Notifications
 Browser ─WS──► Realtime gateway fleet ◄── Redis (user → node)      │ each with own DB
                    ▲                                                ▼
                    └──────────── Broker (Kafka / NATS) ◄── outbox per service
```

**Hardest flow – one chat message:**
1. Browser sends over WS to gateway node G1; G1 forwards to the Chat service (HTTP).
2. Chat checks membership in **its own replica** of memberships (built from `MemberJoined/MemberLeft` events) – a sync call to Teams would couple every message to Teams' availability.
3. Chat stores the message with a per-team sequence and an outbox row in its DB; commits; acks.
4. Outbox relay publishes `ChatMessagePosted` to the broker, partition key = teamId (keeps order per team).
5. A dispatcher looks up members' gateway nodes in Redis and sends the push to G1…Gn; each gateway delivers to its sockets.
6. Offline members catch up from Chat over REST using `lastSeq`.

**Pros:** each capability scales and deploys separately; failures isolated (chat down ≠ agenda down); fits many teams working in parallel.

**Painful parts (low level):**
- **Authorization data is owned by Teams** → each service needs an eventually consistent replica; a removed member may still get messages until the `MemberLeft` event arrives (seconds) → gateway also re-checks on push.
- **Dual write DB + broker** → transactional outbox in every service + idempotent consumers (dedupe by event id).
- **Multi-service operations** (account deletion, team deletion, last-admin succession) → sagas with compensation; see §3 Q3.
- **Event contracts** need versioning; one change touches several services and pipelines.
- **Operations:** Kubernetes, broker, 7 databases, distributed tracing, per-service CI/CD – a full-time ops job for a 3-person team.
- **Local testing** needs the whole fleet or contract tests.

**Honest caveat:** microservices mainly solve **organisational** scale (many dev teams). The load at growth scale (≈ 1k writes/s, small fan-out) does not require them.

### 2.3 Architecture #3 – Serverless / Backend-as-a-Service (cheap to start; vendor limits at scale)

Two variants differ enough to name separately.

**3A – Supabase (managed PostgreSQL + Auth + Realtime + Edge Functions).** Client talks to the database through the auto-generated API; access rules are **row-level security (RLS)** policies; business operations that span tables are PostgreSQL functions or edge functions; Realtime pushes row changes or "broadcast" messages to subscribed clients.
Rough cost: launch €0–25/month; growth several €k/month depending on connection and egress pricing. *Rough, unverified.*

**3B – AWS serverless (API Gateway REST + WebSocket, Lambda, DynamoDB, EventBridge, SES).** Each endpoint is a function; API Gateway holds WebSockets and calls a Lambda on connect/message/disconnect; connections are stored in a DynamoDB table.
Rough cost: launch €20–50/month; growth ≈ €3–6k/month (100k connections ≈ 4.3 billion connection-minutes/month plus ~1 billion pushes). *Rough, unverified.*

```
 3A:  Browser ──► Supabase { Auth │ PostgREST + RLS │ Realtime │ Edge Functions } ──► PostgreSQL
 3B:  Browser ──► API GW (REST/WS) ──► Lambdas ──► DynamoDB ──► Streams/EventBridge ──► Lambda ──► API GW @connections
```

**Hardest flow – one chat message (3B):**
1. Browser sends over the API Gateway WebSocket; `$default` route invokes the `sendMessage` Lambda (cold start possible).
2. Lambda reads the membership item, writes the message with a conditional put (sequence from an atomic counter item).
3. DynamoDB stream triggers a fan-out Lambda: queries members' connection ids, calls `PostToConnection` for each; `GoneException` → delete the stale connection id.
4. Offline members query messages by `teamId` + seq on reconnect.
(3A: insert via API → RLS checks membership → Realtime sends the row to subscribers, RLS re-evaluated per subscriber; catch-up via a select by seq.)

**Pros:** no servers to run; near-zero cost at launch; built-in auth (3A) and auto-scaling (3B); fastest MVP for 3A.

**Painful parts (low level):**
- **Business rules scattered** across RLS policies, triggers, SQL functions and edge functions (3A) or across many Lambdas (3B) – harder to review and test; any rule not enforced server-side can be bypassed by a modified client.
- **3B vendor limits:** WebSocket connection max 2 h, idle timeout 10 min → forced reconnects and heartbeats; stale connection ids; per-connection-minute and per-message pricing.
- **3B data model:** DynamoDB has no joins and limited transactions (`TransactWriteItems` up to 100 items) – "≥ 1 admin" and account deletion need careful conditional writes and step functions.
- **3A Realtime:** RLS is evaluated for every subscriber on every change, which limits throughput; issued JWTs stay valid until expiry, so a removed member can keep reading until the token expires unless the policy checks membership on every read.
- **Local testing and observability** are weaker; **lock-in** is high (3B) to medium (3A – open-source, self-hostable).

**Honest caveat:** excellent for a prototype; the cost is that the domain logic ends up in the vendor's shape, and moving away later is a rewrite.

### 2.4 Comparison & choice

Scores 1 = poor, 5 = excellent. Rows follow the drivers in §1.6 and the constraints in §1.8. Costs are rough, unverified estimates.

| Criterion | #1 Modular monolith | #2 Microservices | #3A Supabase | #3B AWS serverless |
|---|---|---|---|---|
| Correct team rules (≥ 1 admin, membership checks) | **5** one transaction, row locks | 2 replicas + sagas | 3 one DB, rules split over RLS/functions | 2 conditional writes, no joins |
| Reliable real-time delivery | **4** save-then-push, catch-up; one node at launch | **4** dedicated gateway; more moving parts | 3 Realtime + own catch-up; RLS cost per subscriber | 3 2 h / 10 min limits, stale ids |
| Fit for 3 devs and ≤ €150/month | **5** one deploy, ≈ €100 | 1 K8s + broker, ≈ €1k+ | 4 fast MVP, ≈ €25 | 3 cheap, steep learning curve |
| Account deletion (GDPR) | **5** one transaction | 2 saga across 7 DBs | 4 one SQL function + Auth admin call | 2 batched writes, step function |
| Growth to 100k connections without rewrite | 4 add Redis + gateway | **5** built for it | 3 pricing/limits, self-host possible | 4 auto-scales, cost grows |
| Local testing, low lock-in | **5** app + PostgreSQL | 2 whole fleet / contracts | 3 CLI exists; logic in SQL | 1 emulators only |
| Monthly cost: launch / growth | ≈ €100 / ≈ €5–8k | ≈ €1–1.5k / ≈ €12–20k | ≈ €25 / several €k | ≈ €20–50 / ≈ €3–6k |

**Choice for (a) launch:** **#1 Modular monolith.**
- Every business rule is one PostgreSQL transaction (D: correctness, deletion).
- One deployable and ≈ €100/month fit 3 developers and the budget.
- Real-time delivery is reliable because the DB is the truth and clients catch up.

**Choice for (b) growth:** **#1 grown into a hybrid** – the same modular monolith core, plus Redis pub/sub, then an extracted real-time gateway fleet (borrowed from #2), read replicas and chat-table partitioning. Growth is done **by adding infrastructure, not by rewriting**, because the rules in §4 are followed from day one.

**Runner-up:** #2 Microservices – pick it when there are more than ~4 development teams (25+ developers) or when one module's load or release cadence diverges strongly from the rest. #3A Supabase is the runner-up for launch only if a working prototype in ~4 weeks matters more than everything else.

**Rejected:** #3B AWS serverless – the relational rules (admins, memberships, deletion) fit DynamoDB poorly and the WebSocket limits fight a chat product; highest lock-in.

**Hybrid parts kept:** from #2 the real-time gateway, the outbox and idempotent consumers; from #3 the idea of a managed database and a managed email service instead of self-hosting.

**Triggers to move on:** > 5,000 concurrent connections or a need for > 99.5 % availability (→ second instance + Redis); > 30,000 connections or deploys disconnecting too many users (→ gateway fleet); DB CPU > 60 % at peak or chat table > 500 M rows (→ replicas, partitioning); > 3 dev teams or a module with its own release cadence (→ extract that module as a service).

---

## 3. Deep-dive questions

**Q1: What exactly are the styles, and what do the terms mean?**
- *Monolith* – one deployable unit. *Modular monolith* – one deployable unit, code split by business area, each module owns its data and exposes a public interface; borders are enforced by tests.
- *Microservices* – each capability is a separately deployed service with its own database, talking over the network.
- *Event-driven* – components react to published facts ("MemberLeft") instead of calling each other.
- *Serverless / FaaS* – code runs as functions the provider starts on demand; you pay per call. *BaaS* – a provider gives you ready auth, database and realtime; you write rules and small functions.
- Glossary: *WebSocket* – a connection that stays open so the server can send data at any time. *Push* – a message the server sends without being asked. *Pub/sub* – publish once, all subscribers receive it. *Outbox* – a table written in the same transaction as the business change; a relay later delivers its rows, so "saved" and "will be delivered" can't diverge. *Saga* – a business operation split into local steps across services, with compensating steps on failure. *Eventual consistency* – copies of data agree after a short delay, not instantly. *Presence/registry* – which user is connected to which machine. *Row lock* – `SELECT … FOR UPDATE`, which makes concurrent transactions on the same rows wait. *Idempotent* – doing it twice has the same effect as once.

**Q2: One chat message end-to-end through the most complex option (#2).**
1. WS connect to gateway G1: access token validated, user→G1 written to Redis with a 60 s TTL refreshed by heartbeat.
2. Message `{teamId, clientMsgId, text}` → G1 → Chat service.
3. Chat validates length and membership (local replica).
4. Transaction: next per-team seq, insert message (unique `clientMsgId`), insert outbox row; commit; ack to sender with seq.
5. Relay publishes to the broker, partition key teamId.
6. Dispatcher consumes, reads member list (replica) and `user → node` from Redis, sends to each gateway node involved.
7. Gateway re-checks membership, delivers to sockets; client dedupes by seq.
8. Recipient offline or the push lost: on reconnect, client sends `lastSeq` per team and fetches the gap from Chat over REST.

**Q3: The hardest cross-cutting operation – a user who is the last admin of two teams deletes their account. How in each option?**
- **#1:** one transaction in the Identity module: lock the user's memberships and the admin memberships of their teams (`FOR UPDATE`); per team either promote the longest-standing member or delete the team; anonymise authored messages/events/polls and votes; delete tasks, responses, notifications, sessions, the user; insert outbox rows ("you are now admin", "team deleted"). Commit, then close the user's sockets. All or nothing; a concurrent "leave team" by the other member waits on the lock.
- **#2:** saga. Step 1 (pivot): Identity marks the user `deleting` and revokes sessions – from here only forward. Publishes `UserDeletionRequested`. Teams does the succession per team in its own transaction and publishes `AdminChanged`/`TeamDeleted`; Chat, Events, Polls, Agenda, Notifications anonymise/delete and reply. Identity hard-deletes when all replies arrive; missing replies are retried. In between, other services can show the user for seconds; a concurrent "leave team" must be handled by Teams' own lock.
- **#3A:** one SQL function `delete_account()` (security definer) does the DB part in one transaction, like #1; deleting the Auth user is a separate admin API call in an edge function – two steps, retried on failure.
- **#3B:** a step function iterates over DynamoDB items in batches of ≤ 100 (`TransactWriteItems`); not atomic overall; the last-admin check is a conditional write on a team counter item.

**Q4: Can the simplest option reach growth scale? What breaks first?**
1. **One process, in-memory socket registry** → second instance behind a load balancer + Redis pub/sub so a push reaches the other instance.
2. **Connections per process** (~20–50k per tuned node) → extract the real-time gateway as its own fleet; the core stays a monolith.
3. **DB connections** (N instances × pool) → PgBouncer connection pooler.
4. **Read load** (agenda, history) → read replicas; catch-up reads stay on the primary so the newest messages are never missed.
5. **Chat table size** (~1 TB/year) → partition by month.
6. **Relay throughput** (pushes, email) → run the relay as a separate worker process.
7. **Deploys disconnect users** → rolling deploys, connection draining, jittered reconnect.
8. **Organisation** (> 3 teams) → extract the module with the most independent change rate.
Conclusion: yes. Points 1–7 add infrastructure; only 8 changes code structure, and the module borders make it a cut, not a rewrite.

---

## 4. Outcome and input for the ADR

**Outcome:** Teamify is built as a **modular monolith on one PostgreSQL database** for launch scale, with a defined growth path (Redis pub/sub → real-time gateway fleet → replicas/partitioning → service extraction) to growth scale.

**Input for the ADR:**
- **Decision:** modular monolith + PostgreSQL, outbox-based delivery, WebSockets in the app; growth by adding infrastructure.
- **Context:** §1.6 drivers, §1.8 decisions on the gaps, §1.9 sizing and key insight.
- **Options considered:** §2.1–2.3, comparison §2.4.
- **Consequences:** painful parts in §2.1 (border erosion, single point of failure, deploy disconnects), answers in §3 Q3–Q4.

---

## 5. ADR review log

**Output:** `output/Task3_ADR-001-teamify-architecture.md`

### Round 1 – draft v1 (2026-10-29)
**Request:** write an ADR from §4, using one target scale (launch) with growth as a future option; the tech stack (language/framework) is left to a separate ADR.

**Problems found in self-review and fixed before showing v1:**
| # | Problem | Fix |
|---|---|---|
| 1 | Notification delivery was described twice (written in the request transaction vs. sent by the relay). | One mechanism: notification rows and an outbox row in the same transaction; only the relay pushes and emails (R4). |
| 2 | "Single point of failure – mitigated by backups" – backups protect data, not availability. | Availability handled by automatic restart + 99.5 % target (C6); second instance is growth step 1. |
| 3 | Comparison rows did not match drivers (extra "cost" row). | One row per driver D1–D6; costs moved under the table as rough estimates. |
| 4 | Catch-up reads would miss the newest messages once read replicas exist. | Rule R9: reads that must see recent writes go to the primary. |
| 5 | `#` in sequence-diagram text cuts the line. | Wrote "no." instead of `#`. |
| 6 | Sequence numbers and retry handling not defined. | R3: per-team counter row locked in the insert transaction; `UNIQUE(team_id, client_msg_id)`. |
| 7 | R11 moved team-deletion purges into the relay, while G14 and §3 Q3 delete a team in one transaction. | Team deletion stays one transaction (≤ 50 members, small history at launch); R11 now covers only emails. |

**Diagrams:** 3 Mermaid diagrams (growth path, deployment, chat sequence) rendered with Mermaid 11.4.1, 0 errors; module borders are a table instead of a fourth diagram.

**Result:** `Proposed (v1)`, 260 lines.
