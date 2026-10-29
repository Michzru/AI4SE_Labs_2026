# Task 1 – Conversation Notes: Architectural Proposals for Teamify

- **Date:** 2026-10-27
- **Participants:** Michal Zrutta (lead), Claude Code (assistant)
- **Source requirements:** `data/Teamify.txt`
- **Goal of the session:** Understand the Teamify requirements, then discuss at least 3 architectures that could implement it, including their trade-offs and painful low-level implementation details.

The notes are a running record, not a word-for-word transcript. They are updated after each step of the discussion.

---

## 1. Session start

**User request:** Keep notes of the whole discussion in `output/Task1_conversation.md`. Read the requirements of the assigned project (Teamify), summarise what it is about, then move on to architectural design.

**Assistant actions:**
- Read `Task_1.md`, `Task_2.md`, `Task_3.md` to understand the full assignment (Task 2 = ADR from this discussion, Task 3 = turn the process into a Skill). These notes are therefore written to be reusable as input for Task 2 and Task 3.
- Read `data/Teamify.txt` (system description + 31 user stories).
- Created this notes file.

---

## 2. Requirements study – what Teamify is

### 2.1 One-line summary
Teamify is a task-management and team-collaboration app. Individuals keep a personal agenda of tasks. Teams share an agenda of events, a real-time group chat, polls and real-time notifications.

### 2.2 Stated main goals
1. **Task management:** personal and shared tasks.
2. **Team management:** create teams, invite members.
3. **Real-time notifications.**
4. **Real-time chat** with colleagues.

### 2.3 Actors / roles
| Role | Description |
|---|---|
| User | Any registered account. Owns a personal agenda. |
| Team member | A user who belongs to a team. Sees the team agenda, chats, votes in polls. |
| Team administrator | A member with admin rights in that team (the role is per team, and a team can have several admins). Manages events, polls, team info, other admins. |

### 2.4 Functional areas (user stories grouped)
| # | Area | User stories | Notes |
|---|---|---|---|
| A | **Identity & account** | 1 register, 2 login, 3 logout, 4 view profile, 5 edit profile/password, 6 reset password, 7 delete account | Standard auth. US7 implies data erasure (GDPR-style), which spreads into every other area. |
| B | **Notifications** | 8 notification section (inbox) | Plus the "real-time notifications" goal. Triggers are implied, not listed. |
| C | **Personal agenda / tasks** | 9 view agenda, 11 create, 12 edit, 13 delete, 14 mark complete | Simple CRUD scoped to a single user. Tasks occupy "time slots", so they have a date/time. |
| D | **Teams & membership** | 15 create team, 16 join team, 17 list my teams, 18 leave team, 19 promote admin, 20 demote admin, 25 edit team, 26 delete team | Role management per team. |
| E | **Team agenda / events** | 10 view team agenda, 27 create event, 28 accept/refuse invitation, 29 edit event, 30 delete event, 31 mark event complete | An event is a "shared task" with RSVP (accept/refuse). |
| F | **Group chat** | 21 send messages in team group chat | Real-time. One chat per team; no direct messages are mentioned. |
| G | **Polls / surveys** | 22 admin creates poll, 23 view results, 24 vote | Results could update live. |

### 2.5 Main entities (first-cut domain model)
- **User** (credentials, profile)
- **Team**, **Membership** (user–team, role: member/admin)
- **PersonalTask** (owner, title, description, time slot, completed)
- **Event** (team, title, time slot, completed) + **EventInvitation/RSVP** (user, status: pending/accepted/refused)
- **ChatMessage** (team, author, content, timestamp)
- **Poll**, **PollOption**, **Vote** (one vote per member per poll, presumably)
- **Notification** (recipient, type, payload, read/unread)
- Support: **PasswordResetToken**, sessions/refresh tokens

### 2.6 Real-time requirements (main architectural drivers)
- Chat messages delivered live to all online team members.
- Notifications pushed live (event created/changed/deleted, invitation, poll created, role changed, team deleted, …).
- Nice to have: live poll results and live agenda updates.

These push the design towards a persistent connection channel (WebSockets / SSE) and some form of **pub/sub fan-out**. This is the main source of complexity in an otherwise CRUD-heavy app.

### 2.7 Gaps, ambiguities and assumptions found
| # | Observation | Impact / assumption to confirm |
|---|---|---|
| G1 | **No non-functional requirements** (users, concurrency, latency, availability, platforms, budget, team size). | We need to assume a scale before comparing architectures. Proposal: small-to-medium SaaS (thousands to tens of thousands of users, teams of 2–50 people). |
| G2 | **Invite vs join conflict:** the goals say "invite members", US16 says "join an existing team". It's unclear how a user finds or joins a team (invite link? code? approval? public search?). | Assumption: admin-generated invite link/code, optionally with an invite notification. |
| G3 | **Notification triggers are not specified.** | Derive from the stories: event CRUD, invitation, poll created, admin promotion/demotion, team edit/delete, chat mention(?). |
| G4 | **Delivery channels not specified** (in-app only? email? mobile push?). | Assume in-app real-time plus email for password reset. Push is optional. |
| G5 | **Client platform not specified** (web, mobile, both). | Assume a web SPA first, with a mobile-ready API. |
| G6 | **Account deletion semantics:** what happens to the user's chat messages, the polls they created, and teams where they are the last admin? | Needs a policy (anonymise messages, transfer or forbid if last admin). |
| G7 | **Last-admin problem:** US20 (demote) and US18 (leave) can leave a team with no admin. | Business rule: a team must always have at least one admin. |
| G8 | **Event invitation scope:** are all team members invited automatically, or a chosen subset? | Assume all members, each with their own RSVP status. |
| G9 | **Event completion:** US31 lets the admin mark completion for the whole team, not per member. | Completion is a team-level flag. |
| G10 | **Poll details missing:** single vs multiple choice, anonymity, deadline, changing a vote. | Assume single choice, editable until closed, results visible to members. |
| G11 | **Chat features missing:** history, edit/delete, attachments, read receipts, typing indicators. | Assume persistent history with pagination, text only. |
| G12 | **Personal vs shared agenda:** should the personal agenda also show accepted team events? | Probably yes (a unified calendar view). To confirm. |
| G13 | **"Survey creation"** appears in the description, but the stories only describe polls. | Treat surveys as polls. |

### 2.8 Clarifications from the user (round 1)
| Gap | User decision |
|---|---|
| G1 scale | Design for **two scales**: **(a) small**, fewer than 50 users in total, and **(b) large, national level**. Architectures can differ by scale. |
| G2 invite/join | **Both** are supported. The team admin ("person in charge") **invites** users, and users can **send a join request** that the admin **accepts or rejects**. |
| new | **Team size is small:** about a dozen members, **max 20**. |
| G4 channels | **In-app notifications only**, with a **notification history** inside the app. (Email is still needed for password reset, US6.) |
| G6/G7 deletion | If the user is an **admin**, they must **appoint a new admin** before they can leave the team or delete their account. A regular user can delete their account freely. Their **chat messages and polls stay** (assistant assumption: shown as "Deleted user" so personal data is still removed). |
| G10 polls | Accepted the assistant's assumption: single choice, the vote can be changed until the poll closes, optional deadline, members see aggregated results. |

**Derived national-scale numbers** (assistant's assumption, for sizing only):
- About 1M registered users and about 100k concurrent WebSocket connections at peak.
- Teams of 20 or fewer, so roughly 50k–100k teams.
- 1 chat msg/min per active user gives about 1.7k msg/s inbound, and fan-out ×20 gives about 35k deliveries/s.

**Key insight:** because teams have **at most 20 members**, fan-out per message is tiny. At national scale the hard problem is **holding many concurrent connections and routing each message to the gateway node that holds the recipient's socket**, not wide broadcast.

---

## 3. Architectural design discussion

The user asked for designs for scale (a) and scale (b). The assistant proposed three architectures:
- **#1 Modular monolith**, the best fit for (a).
- **#2 Microservices + event bus + real-time gateway**, the classic answer for (b).
- **#3 Serverless / BaaS**, a different style that can serve both (a) and (b) with managed scaling.

### 3.1 Architecture #1 – Modular monolith (scale a, < 50 users)

**Shape:** one deployable process serves the SPA, a REST API and a WebSocket endpoint. Inside it, modules have clear boundaries: `identity`, `teams`, `agenda` (personal tasks + events + RSVP), `chat`, `polls`, `notifications`. There is one PostgreSQL database (a schema/table prefix per module). It runs on one VPS with Docker Compose (app + Postgres + reverse proxy with TLS), at roughly €5–10/month.

```
Browser SPA ──HTTPS/REST──┐
            ──WebSocket───┤
                    ┌─────▼──────────────────────────────┐
                    │  App process                        │
                    │  identity │ teams │ agenda          │
                    │  chat │ polls │ notifications       │
                    │  in-memory ConnectionRegistry       │
                    │  (userId -> sockets)                │
                    └─────┬───────────────────┬──────────┘
                          │                   │ SMTP (password reset only)
                    PostgreSQL           Mail provider
```

**How real-time works:**
1. The client sends a chat message over the WebSocket.
2. The `chat` module checks membership and INSERTs the message.
3. After the commit, it looks up the team's member ids, then their open sockets in the in-memory registry, and pushes the message.
4. Notifications work the same way: the domain action writes `Notification` rows in the same DB transaction, then pushes to the socket after the commit.
5. If a user is offline, the rows wait in the inbox (US8 history).

**Pros:** simplest to build, test and debug. A single DB transaction keeps business rules consistent (last-admin rule, max 20 members, one vote per poll). Very cheap, and one developer can run it.

**Painful parts (low level):**
- **Missed messages on reconnect.** A socket drops, and the push happened between commit and reconnect. The client must keep `lastMessageId` / `lastNotificationId` and fetch the gap via REST on reconnect. Pushes are best effort; the DB is the source of truth.
- **Crash between commit and push.** Same mitigation: the client catches up via history.
- **WebSocket auth.** Validate the session cookie or JWT on the handshake. Re-check team membership on every message, not only at connect, because a user removed from a team must stop receiving messages.
- **Deploys restart the process**, so every client reconnects at once. That's fine at 50 users.
- **The in-memory registry blocks horizontal scaling.** A second instance needs sticky sessions plus Redis pub/sub. That is exactly the evolution path towards (b).
- Time zones for agenda/time slots: store UTC and render in the user's zone.
- The server is a single point of failure, which is acceptable at this scale. Daily `pg_dump` backups.

### 3.2 Architecture #2 – Microservices + event bus + real-time gateway (scale b, national)

**Shape:**
- An API gateway / ingress routes requests to independent services, each with its own database:
  - **Identity** (Keycloak or a custom service: register, login, reset, deletion)
  - **Profile**
  - **Teams & Membership** (invites, join requests, roles, last-admin rule, max 20)
  - **Agenda** (personal tasks, events, RSVP)
  - **Chat** (message store partitioned by `teamId`)
  - **Polls**
  - **Notifications** (inbox store)
  - **Realtime Gateway** (a horizontally scaled WebSocket fleet)
- **Kafka/NATS** carries domain events: `MemberJoined`, `MemberRemoved`, `AdminChanged`, `EventCreated`, `PollCreated`, `UserDeleted`, …
- **Redis** stores presence/routing (`userId -> gateway node`).
- Everything runs on Kubernetes.

```
Clients ─► API Gateway ─► Identity │ Teams │ Agenda │ Polls │ Chat │ Notifications
   │                          │ (each service: own DB, publishes via outbox)
   │                          ▼
   │                    Kafka / NATS  (domain events, partitioned by teamId)
   │                          │
   └──WebSocket──► Realtime Gateway fleet ◄── Redis (presence: userId -> node)
```

**Flow, chat message:**
1. The client sends the message via its gateway node.
2. The Chat service persists it.
3. It publishes `ChatMessageSent(teamId)`.
4. The gateway layer resolves the members, looks up which node holds each member's socket in Redis, and routes the message there.

**Flow, notification:**
1. The Notifications service consumes the domain events.
2. It writes inbox rows.
3. It publishes them to the online users through the gateway.

**Pros:**
- Independent scaling: the gateway fleet scales with connections and Chat scales with writes.
- Fault isolation: polls going down doesn't kill chat.
- Separate teams can own separate services.

**Painful parts (low level):**
- **Authorization data lives in another service.** Chat, Polls and Agenda all need "is user X a member/admin of team Y?". They either make a synchronous call to Teams (latency, coupling, cascading failure) or keep a **local replica of memberships built from events**. The replica is eventually consistent, so a removed member may still receive a message for a short window.
- **Dual-write problem.** "Save to DB and publish to Kafka" must use the **transactional outbox** pattern plus **idempotent consumers** (at-least-once delivery).
- **Account deletion becomes a saga.** The steps are: check the last-admin rule in Teams, then anonymise the author in Chat and Polls, delete the inbox, remove memberships, and finally delete the credentials. Every step needs retries and compensation.
- **Ordering.** Chat order per team needs a Kafka partition key of `teamId`, plus server-side sequence numbers.
- **Gateway operations:**
  - Connection draining on deploys.
  - A **reconnect storm** (thundering herd) when a node dies; use jittered backoff.
  - Load balancer idle timeouts; heartbeats/pings.
  - Presence entries go stale when a node crashes; use TTLs.
- **Operational cost:** Kubernetes, tracing, centralised logging, per-service CI/CD, and contract versioning of events. It needs a real DevOps capability.
- **Honest caveat:** with teams of 20 or fewer, a national-scale load (about 1.7k msg/s) is **modest**. A horizontally scaled modular monolith (#1 + Redis pub/sub + sticky sessions + Postgres read replicas) could probably handle it. Microservices are justified more by organisational scale (many dev teams) than by load.

### 3.3 Architecture #3 – Serverless / BaaS (scales a → b with managed infrastructure)

There are two concrete variants:
- **3A – Supabase / Firebase (BaaS):**
  - Postgres + built-in Auth (register/login/reset emails).
  - **Row Level Security** policies enforce membership and admin rules in the DB.
  - **Realtime** channels per team for chat and notifications (Postgres changes or broadcast).
  - Edge Functions for multi-step rules (e.g. account deletion with admin hand-over).
  - The SPA talks almost directly to the DB API.
- **3B – AWS serverless:**
  - Cognito for auth.
  - API Gateway REST + Lambda for CRUD.
  - **API Gateway WebSocket API** for real-time: `$connect` stores `connectionId,userId` in DynamoDB. Sending a message runs a Lambda that writes the message, queries the team's connections and calls `PostToConnection` for each.
  - DynamoDB (or Aurora Serverless) for data.
  - DynamoDB Streams → Lambda to generate notifications.

**Pros:** no servers to run. Scales from 0 to national without re-architecting. Auth, password reset and real-time are mostly built in. At scale (a) it is often free tier.

**Painful parts (low level):**
- **Vendor lock-in.** RLS/Realtime or API Gateway semantics don't port.
- **Business rules are scattered** across RLS policies, DB functions and edge functions, which makes them hard to test and review. Example: the last-admin and max-20 rules must be enforced in SQL/policies, otherwise a client can bypass them.
- **AWS WebSocket limits:** a 2-hour max connection, a 10-minute idle timeout (needs client pings), and `GoneException` cleanup of stale `connectionId`s.
- **DynamoDB modelling** for relational queries (my teams, members of a team, agenda by date range, polls with votes) needs careful single-table design and GSIs.
- **Cold starts**, harder local development/testing, and observability spread across many functions.
- **Cost model flips at scale.** You pay per request, per message and per connection-minute. With 100k always-connected users, connection-minutes plus messages can cost more than running servers.

### 3.4 Comparison & conclusions
*(Filled in at the end of the session after the Q&A in section 4, on 2026-10-29.)*

#### Comparison table
Scores: 1 = poor, 5 = excellent, from the point of view of Teamify.

| Criterion | #1 Modular monolith | #2 Microservices + event bus | #3 Serverless / BaaS |
|---|---|---|---|
| Fit for scale (a), < 50 users | **5** | 1 (massive overkill) | 4 |
| Fit for scale (b), national | **4** (scaled out: Redis pub/sub, PgBouncer, replicas, partitioning) | **5** | 3 (works, but cost and limits) |
| Time to MVP | **5** | 1 | 4 |
| Development complexity | **5** (low) | 1 (high) | 3 (logic spread across RLS, functions and triggers) |
| Operations effort | 4 at (a), 3 at (b) | 1 (K8s, Kafka, tracing, per-service CI/CD) | **5** (managed) |
| Consistency of business rules (last admin, max 20, one vote) | **5** (one DB transaction) | 2 (sagas, eventual consistency) | 4 (Supabase: one Postgres; AWS: conditional writes) |
| Real-time reliability | 4 (DB as source of truth + catch-up by `seq`) | 4 (same pattern, more moving parts) | 3 (WS connection limits, stale connection ids) |
| GDPR / account deletion complexity | **5** (one transaction) | 2 (saga across 6 services) | 4 |
| Vendor lock-in | **5** (none) | 4 (portable, but Kafka/K8s know-how) | 1 |
| Testability (local dev) | **5** | 2 | 2 |
| Independent scaling / fault isolation | 2 | **5** | 4 |
| Team size it suits | 1–8 devs | 20+ devs / several teams | 1–5 devs |
| **Monthly cost (a)**, rough | **€5–10** (1 VPS) | €150–300+ (min. cluster + Kafka) | **€0–25** (free/pro tier) |
| **Monthly cost (b)**, rough order of magnitude | **€2–5k** (10–20 app nodes, Redis, Postgres primary + replicas) | €6–15k (more nodes, Kafka cluster, per-service DBs, ops tooling) | €10k+, mostly per-message and per-connection-minute charges for ~100k always-on sockets (pricing to be verified) |

*Costs are rough estimates for comparing the options only. They exclude developer salaries, which favour #1 and #3 even more.*

#### Winner for scale (a): fewer than 50 users → **#1 Modular monolith**
- One VPS, one Postgres, one deploy. All business rules (last admin, max 20, admin hand-over before deletion, one vote) are enforced in one DB transaction with row locks.
- Real-time is an in-memory socket registry. Clients catch up by `seq` after a reconnect.
- **Runner-up: #3 Supabase.** Choose it when nobody wants to run a server or write auth. It costs a trickier rule implementation in RLS and triggers, plus vendor lock-in.
- **Rejected: #2.** Distributed-system cost with zero benefit at this scale.

#### Winner for scale (b): national → **#1 scaled out, with the Realtime Gateway extracted (hybrid #1 + #2)**
- **Core:** the same modular-monolith codebase run as N stateless instances behind a load balancer, with:
  - Redis pub/sub for cross-instance delivery
  - PgBouncer
  - Postgres read replicas (read-your-writes routing)
  - the chat table partitioned by time with an index on `(team_id, seq)`
  - a job queue for notification fan-out and email
- **Borrowed from #2:** a separate **Realtime Gateway** fleet holds the ~100k WebSockets, with presence in Redis. Deploys of business logic then don't disconnect users, and connections scale independently.
- **Why not pure #2:** teams of 20 or fewer keep the load modest (~1.7k msg/s, ~35k deliveries/s). Microservices would pay for sagas, outbox, eventual consistency and K8s/Kafka operations mainly to solve an *organisational* problem (many dev teams) that the requirements don't mention.
- **Trigger to move further towards #2:** more than ~20–30 developers, or one module (e.g. Chat) whose load or release cadence diverges strongly. Then extract it with the strangler pattern. The module boundaries from #1 make this possible.
- **Why not #3:** per-message and per-connection pricing grows badly with always-on chat. It also has hard WS limits (2 h max connection, 10 min idle) and vendor lock-in at a scale where migrating is painful.

#### One evolution path covers both scales
Start at (a) with #1 and keep module boundaries enforced by tooling. Growing towards (b) means adding infrastructure (Redis, PgBouncer, replicas, a job queue, then the gateway), not rewriting. This continuity is the main argument for the decision.

---

## 4. Q&A round 2 – user's clarifying questions (short record)

**Q1: Explain the architectural styles precisely.**
- **Monolith:** one deployable process and one DB. Modules call each other with in-process function calls.
- **Modular monolith:** still one deployable, but the code is split by business domain. Each module has a public API, private internals and owns its own tables. Its weak point is that boundaries erode unless a tool enforces them.
- **Microservices:** each business capability is a separately deployed process with its own DB. They talk over the network (HTTP/gRPC or messaging). They can be deployed and scaled independently, at the cost of distributed-system problems.
- **Event-driven / event bus:** producers publish facts (`MemberJoined`) to a broker. Consumers react without the producer knowing them. This decouples services but makes data eventually consistent.
- **Serverless (FaaS):** short-lived, stateless functions run and scale by the provider, paid per invocation. They cannot hold sockets, so API Gateway holds the WebSocket.
- **BaaS:** ready-made backend building blocks (auth, DB, realtime), with rules written as DB policies (Supabase/Firebase).
- Glossary given: WebSocket, pub/sub, transactional outbox, saga, eventual consistency, presence.

**Q2: One chat message end-to-end in #2.**
1. The WS handshake validates the JWT. The gateway node registers presence in Redis (`user -> node`, refreshed by heartbeat with a TTL).
2. The client sends `chat.send {teamId, clientMsgId, text}`.
3. The gateway forwards it to the Chat service. The gateway holds no business logic.
4. Chat checks membership against its local replica.
5. In one transaction, Chat inserts the message (per-team `seq`) and an outbox row, then acks the sender.
6. The outbox relay publishes to Kafka with `key = teamId`, which preserves order within the team.
7. The delivery consumer gets the team members (≤ 20), looks up their presence and publishes to each target gateway node's channel. The nodes push to the sockets.
8. Offline members fetch the missed messages by `seq` on reconnect.
9. Delivery is at least once, so clients dedupe by message id and detect gaps by `seq`.

**Q3: Deleting an admin's account.**
- **Common rule:** if the user is the *last* admin of a team, they must first appoint a successor. If they are the only member, the team is deleted.
- **Data handling:**
  - Messages and polls stay, shown as "Deleted user".
  - Votes stay anonymised.
  - Tasks, RSVPs, notifications, memberships, invites and sessions are deleted.
- **#1:** one DB transaction.
  - It locks the user's admin memberships (`SELECT … FOR UPDATE`) so that two co-admins deleting at the same moment cannot leave a team with zero admins.
  - It applies the successors (passed in the same request), anonymises, deletes and commits, then closes the user's sockets.
- **#2:** a saga orchestrated by Identity/Account.
  1. Teams performs the only business check that can fail, plus "remove from all teams" (the pivot step).
  2. The user is marked `DELETING`: login blocked, tokens revoked or denylisted (short JWT lifetimes matter).
  3. `UserDeletionRequested` is published. Chat, Polls, Agenda, Notifications and Gateway each erase or anonymise and reply.
  4. Credentials are hard-deleted, then `UserDeleted` is published.
  - Irreversible steps come after the pivot, so no compensation is needed.
  - Anonymisation trick: keep `author_id` on messages and let the Profile service return a "Deleted user" tombstone, which avoids rewriting millions of rows.
- **#3:**
  - **Supabase:** a single `SECURITY DEFINER` Postgres function, transactional like #1, plus an auth admin API call. A trigger or RLS must stop the last admin demoting themselves, and an already issued JWT stays valid until it expires.
  - **AWS:** Step Functions + DynamoDB `TransactWriteItems` with condition expressions for the last-admin check, then Cognito `AdminDeleteUser`.

**Q4: Can #1 reach national scale? What breaks first?**
Yes, as a **horizontally scaled modular monolith**. Things break in this order:
1. **The single process and the in-memory connection registry.** About 100k sockets is feasible on one box (FD limits, roughly 3 GB RAM), but one server is a single point of failure and a deploy causes a reconnect storm. With N instances, a message on instance 1 cannot reach a socket on instance 2. Fix: an LB with WS support plus Redis pub/sub.
2. **The DB.** Symptoms are connection pool exhaustion and a huge chat table (about 17M rows/day). Each notification also fans out into about 20 inbox writes. Fixes: PgBouncer, partitioning chat by time, an index on `(team_id, seq)`, and read replicas (watch replication lag and read-your-writes).
3. **Synchronous side-work.** Fix: move notification fan-out and email to a job queue.
4. **Deploys.** Need rolling deploys with connection draining.
5. **Organisation.** A single codebase gets crowded with many developers. Enforce module boundaries with tooling.
- **Conclusion:** load alone doesn't force microservices. A possible hybrid is to extract only the Realtime Gateway (and later Chat) using the strangler pattern.

---

## 5. Session close (2026-10-29)

**User request:** Fill in the final comparison, pick a winner for each scale, and finish Task 1.

**Outcome:**
- The comparison table and both winners are in section 3.4.
- **Scale (a):** #1 Modular monolith.
- **Scale (b):** #1 scaled out, with the Realtime Gateway extracted (hybrid #1 + #2).

**Input for Task 2 (ADR):**
- **Decision:** modular monolith with a defined scale-out path.
- **Context:** sections 2.4–2.8.
- **Options considered:** #1, #2, #3 (section 3).
- **Consequences:** the painful parts listed under each option, plus the answers in section 4.

**Open items not yet decided:**
- Concrete tech stack (language/framework).
- How users discover a team in order to send a join request (search vs. code/link).
- Chat history retention.
- Poll anonymity towards admins.
