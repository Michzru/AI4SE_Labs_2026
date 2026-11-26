# Task 4 – Profily / módy v Claude Code

**Asistent:** Claude Code (CLI + desktop app) od Anthropicu.

**Výsledok:** Claude Code nemá profily ani módy, ktoré by sa prepínali cez dropdown a mali by vlastný system prompt, model a temperature. Temperature sa v ňom nedá nastaviť vôbec, hoci samotné Anthropic API tento parameter má.

## Prečo to podľa mňa nepodporuje

- Anthropic je etablovaný hráč a chce, aby sa nástroj správal predvídateľne. Keby si používateľ nastavil zlú temperature alebo sampling, dostával by horšie výsledky a pripisoval by ich nástroju, čo by poškodilo reputáciu.
- Namiesto ladenia nízkoúrovňových parametrov Anthropic ponúka niekoľko modelov (Opus, Sonnet, Haiku), ktoré sú doladené na prácu s kódom a s agentmi. Používateľ si vyberá model a úroveň uvažovania (`effort` / extended thinking). Toto nastavenie ovplyvňuje, ako dôkladne model pracuje na cieli, nie či je jeho výstup deterministický.

## Alternatívy v Claude Code

| Funkcia | Čo umožňuje |
|---|---|
| **Output styles** (`~/.claude/output-styles/*.md`) | Vlastný doplnok k system promptu, ktorý sa dá prepínať. Je to najbližšie k „módu“. |
| **Subagenti** (`.claude/agents/*.md`) | Vlastný system prompt, `model`, povolené `tools` a `effort` pre jednotlivých agentov. |
| **Výber modelu a effortu** | Prepínanie modelu a hĺbky uvažovania počas session. |
| **Permission modes** | Režimy default, plan, auto a ďalšie určujú, čo smie agent robiť bez potvrdenia. |
| **Settings / CLAUDE.md** | Konfigurácia na úrovni používateľa, projektu alebo lokálne, plus trvalé inštrukcie. |
