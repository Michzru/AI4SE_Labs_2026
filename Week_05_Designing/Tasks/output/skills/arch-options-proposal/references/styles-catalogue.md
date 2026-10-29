# Architectural styles catalogue

Use this to pick options that differ in kind, and as a checklist of the painful parts to mention. Pick styles that match the drivers; don't list all of them.

| Style | In one line | Fits when | Typical painful parts |
|---|---|---|---|
| **Layered / classic monolith** | One deployable, layers (UI / service / data), one DB. | Tiny scope, one developer, short life. | Modules tangle over time; hard to split later. |
| **Modular monolith** | One deployable and one DB, code split by business domain, each module owns its tables and exposes a public API. | Small–medium scale, 1–8 devs, strong consistency needs. Can scale out horizontally. | Boundaries erode unless enforced by tooling (architecture tests). In-memory state (sockets, caches) blocks scaling out → needs Redis pub/sub or a gateway. Single point of failure; deploys disconnect everyone. |
| **Microservices + event bus** | Each capability is its own service with its own DB, talking over HTTP/gRPC and a broker (Kafka/NATS). Usually on Kubernetes. | Many dev teams, very different load/release cadence per capability. | Authorization data in another service (sync call vs. eventually consistent replica). Dual write → transactional outbox + idempotent consumers. Multi-service operations → sagas with compensation. Ordering (partition keys, sequence numbers). Event contract versioning. Ops cost: K8s, tracing, logging, per-service CI/CD. |
| **Event-driven / CQRS / event sourcing** | State changes stored as events; read models built from them. | Audit trails, complex workflows, many read views. | Eventual consistency in the UI, replay and schema evolution of events, debugging. |
| **Serverless / FaaS** (e.g. AWS Lambda + API Gateway + DynamoDB) | Stateless functions run by the provider, paid per invocation. Managed WebSocket API holds connections. | Spiky or low traffic, small team, no ops. | Cold starts, vendor limits (e.g. API GW WebSocket: 2 h max connection, 10 min idle timeout, stale `connectionId` → `GoneException`), NoSQL modelling of relational queries, local testing, observability, per-request / per-connection-minute cost at scale, lock-in. |
| **BaaS** (e.g. Supabase, Firebase) | Ready-made auth, DB, realtime; rules written as DB policies (RLS) plus edge functions. | MVPs, small teams, CRUD + realtime. | Business rules scattered across RLS, triggers and functions (hard to test/review; must be enforced server-side or clients bypass them). Issued JWTs stay valid until expiry. Lock-in, pricing at scale. |
| **Space-based / in-memory grid** | Processing units with replicated in-memory data. | Extreme, spiky load with low latency. | Data consistency, cost, niche skills. |
| **Local-first / offline-first** | Data lives on devices and syncs (CRDTs). | Offline use, collaborative editing. | Conflict resolution, sync protocols, authorization on sync. |
| **Hybrid** | A simple core plus one extracted part (e.g. a real-time gateway fleet, a search engine). | When one concern scales differently from the rest. | Integration between the core and the extracted part; two deployment models. |

## Patterns that come up in almost every real-time discussion

- **Save first, then push.** The DB is the source of truth; a push is only a signal. Clients keep the last seen sequence number and fetch the gap on reconnect.
- **Per-group sequence numbers** for ordering and gap detection; a client-generated message id for idempotent retries.
- **Presence / routing registry** (`userId → node`) with TTLs refreshed by heartbeat.
- **Re-check authorization on every message**, not only at connect — a removed member must stop receiving.
- **Jittered reconnect backoff** to avoid reconnect storms; connection draining on deploys.
- **Row locks** (`SELECT … FOR UPDATE`) for invariants like "a team always has at least one admin" when two people act at the same moment.
- **Keyset pagination** (by sequence number, never `OFFSET`) for long histories.
