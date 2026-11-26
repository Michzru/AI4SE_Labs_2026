# Task 6 – Subagenti v Claude Code

**Výsledok:** hlavný agent (Claude Opus 5.5) spustil paralelne **5 subagentov na lacnejšom modeli Haiku**. Každý zhrnul jeden týždeň labov. Všetkých 5 skončilo za 14–19 s, každý použil asi 60 k tokenov a 5–8 volaní nástrojov.

## Konfigurácia

Definícia subagenta v repe: [`.claude/agents/week-summarizer.md`](../../../.claude/agents/week-summarizer.md)

```yaml
---
name: week-summarizer
description: Summarizes one week folder of AI4SE_Labs_2026 (its topic and outputs) in two sentences.
model: haiku
tools: Read, Glob, Grep
---
```

Obmedzenia: lacný model, len nástroje na čítanie, najviac 6 prečítaných súborov, výstup presne 2 vety a 1 agent na 1 týždeň (spolu 5).

## Záznam konverzácie

**Ja:** Poďme na Task 6, čo od nás chce?

**Claude:** Vysvetlil zadanie a navrhol subagenta `week-summarizer` (Haiku, len čítanie). Ten mal paralelne zhrnúť každý týždeň labov.

**Ja:** Áno, urob to.

**Claude:**
1. Vytvoril súbor `.claude/agents/week-summarizer.md`.
2. Skúsil spustiť agenta typu `week-summarizer`. Dostal chybu `Agent type 'week-summarizer' not found`, lebo **nové definície agentov sa načítajú až pri štarte novej session**.
3. Namiesto toho spustil 5× agenta `general-purpose` s parametrom `model: haiku` a rovnakými pravidlami v prompte. Agenti bežali paralelne na pozadí.

Prompt každého subagenta:
> Summarize the week folder `<cesta k týždňu>`. Rules: read only the week's AGENTS.md, README (if any) and Task_N.md files, at most 6 files, use only Read/Glob/Grep, modify nothing. Reply with exactly two sentences in Slovak: (1) the week's topic, (2) what the student produced and where.

### Výstupy subagentov

| Týždeň | Odpoveď subagenta (skrátené) | Tokeny | Čas |
|---|---|---|---|
| 03 Prompting | Text-to-SQL nad databázou reštaurácií (155 otázok), porovnanie ICIO, Few-Shot a CoT na Sonnet 5.5 a Opus 5.5. Výstupy: `prompts.json`, predikcie v `Task_2/output/`, `metrics.py`, analýza v `Task_4/`. | 60 048 | 16,2 s |
| 04 Requirements | Sieť v LangGraph, ktorá z dokumentov vytvorí špecifikáciu požiadaviek s ID, MoSCoW prioritami a blacklistom. Výstupy: `network.py`, 22 testov, `requirements.md` (3 behy: 446, 453 a 421 požiadaviek), `report.md`. | 61 365 | 14,8 s |
| 05 Designing | Architektúra systému Teamify: porovnanie 3 architektúr, ADR a skilly. Výstupy v `Tasks/output/` (konverzácie, ADR, 3 skilly). | 59 953 | 17,6 s |
| 06 Implementation | RAG nad repozitárom AI4SE_Playground, ktorý dopĺňa chýbajúce metódy (10/10 úloh, 481/481 testov). Výstupy: skripty v `output/code/`, `report_task1–6.md`. | 61 786 | 18,7 s |
| 08 Dissecting | Rozbor Claude Code (system prompt, príkazy, AGENTS.md, profily, skilly, subagenti, MCP). Výstupy: screenshoty, AGENTS.md, reporty v `Task_N/`. | 58 755 | 14,2 s |

## Zistenia

- **Paralelizmus funguje:** 5 agentov skončilo približne za čas jedného (do 19 s). Do kontextu hlavného agenta sa vrátili len krátke odpovede, nie obsah prečítaných súborov.
- **Réžia na agenta je vysoká:** asi 60 k tokenov na každého agenta, hoci prečítal len pár súborov. Väčšinu tvorí systémový kontext, ktorý agent dostane pri štarte. Pri dlhodobom autonómnom behu by preto bolo nutné obmedziť počet agentov.
- **Haiku nedodržal všetky pravidlá:** 3 z 5 agentov pridali na začiatok hodnotenie „cítim sa X/10“, lebo zdedili globálny CLAUDE.md. Niektorí napísali viac ako 2 vety. Dvaja tvrdili, že Glob a Grep nemajú k dispozícii, a jeden neprečítal všetky Task súbory. Lacný model sa teda hodí na objemovú prácu, ale jeho výstup treba skontrolovať.
- **Vlastný typ agenta** (`.claude/agents/*.md`) sa dá použiť až v novej session. V tej istej session sa dá to isté dosiahnuť parametrom `model` a pravidlami v prompte.
