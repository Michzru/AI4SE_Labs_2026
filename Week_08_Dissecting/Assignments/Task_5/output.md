# Task 5 – Skill v Claude Code

**Skill:** [`.claude/skills/upece-oznamy/SKILL.md`](../../../.claude/skills/upece-oznamy/SKILL.md)

Skill vyrába HTML s týždennými oznamami UPeCe (kalendár omší a akcií, zvonček, oznamy) z textu skopírovaného z Google Docs. Pôvodne som ho používal v Claude appke, teraz je v repe ako projektový skill.

## Umiestnenie (štruktúra podľa Claude Code)

```
<repo>/.claude/skills/<nazov-skillu>/SKILL.md   # projektový skill, verzuje sa v gite
~/.claude/skills/<nazov-skillu>/SKILL.md        # osobný skill, platí pre všetky projekty
```

`SKILL.md` má YAML hlavičku s `name` a `description` a pod ňou inštrukcie v Markdowne. Vedľa môžu byť ďalšie súbory, napr. šablóny alebo skripty.

## Ako ho Claude Code využíva

1. Pri štarte session Claude Code načíta len `name` a `description` všetkých skillov, nie celý obsah.
2. Keď požiadavka zodpovedá popisu (napr. „tu sú nové oznamy, sprav HTML“), model skill zavolá sám. Dá sa spustiť aj ručne cez `/upece-oznamy`.
3. Až potom sa do kontextu načíta celý `SKILL.md`, teda pravidlá formátovania a CSS šablóna. Model podľa nich zostaví HTML a uloží ho ako `oznamy-DD-MM.html`.

Výsledok: [priklad.png](priklad.png).
