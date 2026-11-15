# Report – Task 6 (Bonus): Návrh pipeline na generovanie kódu s poznaním repozitára

Návrh vychádza z toho, čo sme namerali v Task 2–5 na repozitári `AI4SE_Playground` (38k tokenov, 10 úloh, 481 testov).

---

## 1. Čo sme zistili v Task 2–5

| Zistenie | Dôkaz |
|---|---|
| Správny chunk (trieda so stubom) nájde aj jednoduchý embedding | R@1 = 1.0 pri 4 zo 6 modelov na popisy, 0.9 pri zvyšných 2 |
| Úspech rozhodujú **ostatné** chunky v top 5, nie poradie toho správneho | `BulkDiscountPricing.price`: 0/3 alebo 3/3 podľa toho, či je 5. chunk `FlatPricing` |
| Embedding hľadá **podobné**, kód potrebuje **súvisiace** | trieda `Money` nebola v top 5 pri žiadnom store → modely hádali `.amount` namiesto `.cents` |
| Surový kód sa do embedding modelu nezmestí | 56/95 chunkov > 512 tokenov → orezané, gold až na 74. mieste |
| Kvalita popisov chunkov mení výsledok viac než voľba generačného modelu | gpt-5.4-nano s luna popismi 10/10, gpt-5-mini s vlastnými 9/10 |
| Pevné k = 5 je náhodné číslo | skóre 1. miesta 0.84 vs. 5. miesta 0.73 – podľa skóre sa relevantné od šumu nedá oddeliť |
| Chyby sú jasné z testov, ale pipeline ich nevidí | `'Money' object has no attribute 'amount'` – pri jednej oprave takmer istý úspech |
| Celý repozitár sa zmestí do kontextu | 38k tokenov vs. 128k–1M kontext dnešných modelov |

## 2. Odpovede na otázky zo zadania

**Je porovnávanie embeddingov najlepšia stratégia?**
Nie ako jediná. Embedding je dobrý na nájdenie miesta, kde sa má niečo zmeniť, keď je úloha zadaná voľným textom. Nevie ale nájsť to, čo kód *potrebuje* (typy, rodičovské triedy, pomocné funkcie), lebo tie sa otázke nepodobajú. V našich úlohách navyše cieľ poznáme presne (súbor, trieda, metóda), takže ho netreba hľadať podľa podobnosti vôbec.

**Fungoval by lepšie iný počet chunkov?**
Lepší ako iné číslo je rozpočet v tokenoch a poradie podľa priority. Jednoduchej úlohe stačí 1 chunk, zložitej nestačí ani 10. Pri repozitári, ktorý sa celý zmestí do kontextu (ako náš), je najjednoduchšie poslať všetko alebo aspoň celé súbory.

**Malo by byť delenie prepracovanejšie?**
Áno, ale nie v tom, *kde* rezať (AST rezanie fungovalo dobre), ale v tom, čo chunk *vie o okolí*. Chunk by si mal pamätať svoje závislosti a kto ho používa. Plus viac úrovní: kostra repozitára → trieda → metóda.

## 3. Navrhovaná pipeline

```
úloha
  │
  ├─ 1. nájdi cieľ ......... presne podľa mena, inak hybrid (BM25 + embedding) + reranker
  ├─ 2. doplň závislosti ... z grafu: typy, rodič, volané triedy, testy
  ├─ 3. poskladaj kontext .. podľa priority do rozpočtu tokenov
  ├─ 4. generuj ............ LLM napíše kód
  └─ 5. over a oprav ....... spusti testy, chybu vráť LLM (max 2–3 pokusy)
```

### 3.1 Index: chunk + jeho závislosti

Chunky ostávajú podľa AST, ale každý si navyše nesie, s čím súvisí. Všetko sa dá vytiahnuť z AST, netreba na to LLM.

```json
{
  "id": "pricing.py::001",
  "class": "BulkDiscountPricing",
  "imports":    ["models.Money", "models.LineItem", "base.PricingStrategy"],
  "uses_types": ["Money", "LineItem", "PricingStrategy"],
  "parent":     "PricingStrategy",
  "calls":      ["PricingStrategy.price"],
  "used_by":    ["test_pricing.py::003", "orders.py::001"],
  "summary":    "...",
  "embedding":  [...]
}
```

Externé knižnice sa do kontextu nedávajú (model ich pozná), ukladá sa len názov a verzia, aby model nepoužil neexistujúcu funkciu.

Okrem chunkov sa drží **kostra repozitára**: zoznam súborov, tried a signatúr metód bez tiel. Je malá (rádovo stovky tokenov) a model z nej vidí celkový obraz – napr. že `Money` má property `cents`.

### 3.2 Hľadanie cieľa

- Úloha s menom (ako v `missing_code.json`) → cieľ sa nájde presne, bez embeddingu.
- Úloha voľným textom → **hybrid**: BM25 zachytí presné identifikátory (`can_afford`, `UnknownSKUError`), embedding zachytí význam. Top ~30 kandidátov prejde **reranker** (cross-encoder alebo LLM), ktorý vidí otázku aj chunk naraz a je presnejší ako porovnanie vektorov.

### 3.3 Skladanie kontextu podľa priority

Rozpočet napr. 4–8k tokenov, plní sa v tomto poradí, kým sa neminie:

1. cieľová trieda celá,
2. kostra repozitára,
3. priame závislosti z grafu (typy zo signatúry, rodič, volané triedy),
4. testy, ktoré cieľ volajú,
5. podobné chunky z embeddingu (príklady štýlu a konvencií).

Ak sa celý repozitár zmestí do rozpočtu, pošle sa celý.

### 3.4 Overenie a oprava

Po zápise sa spustia testy. Ak niečo padne, LLM dostane chybu a traceback a opraví kód. Limit 2–3 pokusy, aby sa model nezacyklil. Ak treba, môže si v tomto kroku vypýtať ďalší súbor (agentický prístup – nástroje `read_file`, `grep`, `run_tests`).

### 3.5 Aktualizácia indexu

- Popisy sa cachujú podľa **hashu obsahu** chunku, nie podľa ID (dnes by po zmene kódu ostal starý popis – tichá chyba).
- Prepočet pri každom commite (git hook), len pre zmenené chunky. Embedding je lacný, drahý je LLM popis.
- Ak sa úlohy riešia za sebou a závisia od seba (`charge` volá `can_afford`), index sa aktualizuje po každom zápise.

## 4. Ako by návrh vyriešil naše chyby

| Problém v Task 5 | Čo ho rieši |
|---|---|
| `Money` nebol v kontexte → `.amount` namiesto `.cents` | závislosti z grafu (`-> Money` v signatúre) + kostra repozitára |
| Výsledok závisel od toho, čo padne na 5. miesto | priorita a rozpočet namiesto pevného top 5 |
| Orezanie dlhého kódu v embedding modeli | embeduje sa popis; cieľ a závislosti sa berú cez graf, nie podľa podobnosti |
| `__contains__` vyhadzoval výnimku namiesto `False` | spätná väzba z testov |
| Zastaraný popis po zmene kódu | cache podľa hashu + prepočet pri commite |

## 5. Kompromisy

| Za | Proti |
|---|---|
| Graf je deterministický a lacný | v Pythone bez typových anotácií je neúplný; pre každý jazyk treba parser |
| Spätná väzba z testov výrazne zvyšuje úspešnosť | viac volaní LLM, dlhší čas; bez testov nefunguje |
| Celý repozitár v kontexte je najjednoduchší | pri veľkých repozitároch nemožné a drahé; model sa v dlhom kontexte môže „stratiť“ |
| Reranker zlepší výber | ďalší model a latencia |

**Odporúčanie:** pre malé repozitáre poslať celé relevantné súbory a pridať spätnú väzbu z testov. Pre veľké repozitáre graf závislostí + hybridné hľadanie + rozpočet tokenov + spätná väzba. Embedding ostáva, ale ako jeden zo zdrojov, nie jediný.
