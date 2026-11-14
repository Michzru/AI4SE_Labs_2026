# Report – Task 5: Riešenie úloh cez RAG a výsledky testov

**Výstupy**
- RAG riešenie úloh: [`output/code/solve_tasks.py`](output/code/solve_tasks.py) – `solve(task_text)` (top 5 → prompt → LLM), `write_method(...)` (zápis do súboru)
- experimenty: [`output/code/run_experiments.py`](output/code/run_experiments.py), výsledky v [`output/code/results/`](output/code/results/) (`summary.json`, `run_*.json`, `test_map.json`)
- spoločný LLM klient: [`output/code/llm.py`](output/code/llm.py)
- záloha pôvodných stub súborov: `output/code/backup_original/` (`python solve_tasks.py --reset`)

Spustenie finálnej konfigurácie: `python solve_tasks.py --gen-model gpt-5-mini --summary-model gpt-5.6-luna`

---

## 1. Výsledok – finálna konfigurácia

Generovanie `gpt-5-mini`, popisy chunkov `gpt-5.6-luna`, embedding `bge-small`, top 5 kosínus. Kód je zapísaný v repozitári.

| | Pred (stuby `pass`) | Po |
|---|---|---|
| Testy prešli | 429 / 481 | **481 / 481** |
| FAIL + ERROR | 35 + 17 | 0 |
| Úlohy vyriešené | 0 / 10 | **10 / 10** |
| Rozbité testy mimo úloh | – | 0 |

| Úloha | Testy úlohy | Čas LLM |
|---|---|---|
| OrderStatus.is_terminal | 4/4 | 2.4 s |
| InventoryLedger.\_\_contains\_\_ | 5/5 | 7.0 s |
| Warehouse.stock_report | 3/3 | 4.2 s |
| OrderStateMachine.transition | 24/24 | 4.9 s |
| OrderLog.by_status | 2/2 | 4.6 s |
| Customer.can_afford | 8/8 | 2.9 s |
| Order.\_\_len\_\_ | 6/6 | 2.0 s |
| BulkDiscountPricing.price | 10/10 | 4.4 s |
| EventBus.\_\_contains\_\_ | 6/6 | 4.2 s |
| Money.\_\_bool\_\_ | 2/2 | 2.8 s |

Tokeny spolu (10 úloh): 26 620 vstup, 2 745 výstup; prompt priemerne ~10 200 znakov (~2.7k tokenov).

## 2. Rozhodnutia

| Rozhodnutie | Voľba | Dôvod |
|---|---|---|
| Text úlohy | „Implement method M of class C in F. <docstring>“ | v Task 3/4 dal gold chunk na 1. mieste 10/10 |
| Prompt | systém: vráť len `def` + telo v ```python bloku, zachovaj signatúru, nepridávaj importy, rieš podľa testov v kontexte; user: úloha + 5 chunkov so skóre | výstup sa dá spoľahlivo vložiť do súboru |
| Parsovanie | prvý ```python blok, `ast` nájde `def <method>` (aj vnorený v triede), dekorátory sa zahodia | modely občas vrátia celú triedu alebo `@property` |
| Zápis | `ast` nájde `class C` → `def M`, nahradí riadky `def`…koniec, odsadenie podľa stubu, docstring z JSON ak chýba; dekorátory v súbore ostanú | presné nahradenie, nie textové hľadanie |
| Kontrola | `ast.parse` celého súboru pred zápisom | zlá odpoveď nerozbije import balíka |
| Bez spätnej väzby z testov | 1 volanie LLM na úlohu | meria sa čistý RAG |
| Záloha / reset | `backup_original/` + reset pred každým behom | opakovateľné a porovnateľné behy |
| Testy → úloha | každý stub dočasne nahradený `raise NotImplementedError("TASK_i")`, podľa markera v chybe sa test priradí úlohe (`test_map.json`) | výsledky po úlohách, nie len súčet |
| Paralelizmus | LLM volania paralelne, zápis sekvenčne | viac úloh v rovnakom súbore (`orders.py` ×3) |

Mapa testov: 70 testov závisí od 10 stubov, pokrýva všetkých 52 padajúcich; 18 testov prechádza aj so stubom (`pass` vráti `None`, napr. falsy výsledok).

## 3. Experiment A – model na generovanie kódu

Popisy chunkov `gpt-5-mini`, 3 opakovania na model (gpt-5 modely nemajú `temperature` → nedeterministické).

| Model | Úlohy /10 | Testy úloh /70 | Všetky testy /481 | Rozbité mimo | Chyby zápisu | s/úloha | Výstupné tokeny (10 úloh) |
|---|---|---|---|---|---|---|---|
| gpt-6-luna | 9.7 ± 0.6 | 67.3 ± 4.6 | 478.3 ± 4.6 | 0 | 0 | 2.0 | 988 |
| gpt-5.6-luna | 9.3 ± 0.6 | 69.3 ± 0.6 | 480.3 ± 0.6 | 0 | 0 | 2.3 | 1 307 |
| gpt-5.4-nano | 9.0 ± 0.0 | 63.0 ± 0.0 | 474.0 ± 0.0 | 0 | 0 | 2.2 | 2 026 |
| gpt-5-mini | 9.0 ± 0.0 | 63.0 ± 0.0 | 474.0 ± 0.0 | 0 | 0 | 4.1 | 3 097 |
| gpt-5-nano | 8.7 ± 0.6 | 61.7 ± 0.6 | 472.7 ± 0.6 | 0 | 0 | 3.0 | 4 423 |
| gpt-4o-mini | 7.3 ± 0.6 | 59.3 ± 0.6 | 470.3 ± 0.6 | 0 | 0 | 1.3 | 466 |

`gpt-4.1-nano` nebol testovaný – API vracia 404 (deprecated).

Vyriešené behy z 3 (len úlohy, kde aspoň jeden model zlyhal):

| Úloha | 6-luna | 5.6-luna | 5.4-nano | 5-nano | 5-mini | 4o-mini |
|---|---|---|---|---|---|---|
| BulkDiscountPricing.price | 2 | 3 | 0 | 0 | 0 | 0 |
| InventoryLedger.\_\_contains\_\_ | 3 | 1 | 3 | 2 | 3 | 0 |
| EventBus.\_\_contains\_\_ | 3 | 3 | 3 | 3 | 3 | 1 |

- 7 z 10 úloh vyriešili všetky modely vo všetkých behoch.
- **`BulkDiscountPricing.price`** – hlavná chyba: trieda `Money` nie je v top 5, model nevie, že má atribút `.cents`, a háda `.amount` alebo `Money * int // 100` (Money nemá `//`). → chýbajúca závislosť v retrievale.
- `gpt-4o-mini` pri `InventoryLedger.__contains__` volá `_require_sku`, ktorá pre neznámy/chybný SKU vyhodí `UnknownSKUError` namiesto vrátenia `False`.
- Žiadny model nerozbil test mimo svojej úlohy, žiadna odpoveď nebola nesparsovateľná.

## 4. Experiment B – model na popis chunkov (Task 3)

Pre každý model nové popisy všetkých 95 chunkov → vlastný store (`stores/`), rovnaký embedding. Retrieval na 10 úlohách + end-to-end s 2 generačnými modelmi, 3 opakovania.

| Model popisov | Slov/popis | Gold R@1 | MRR | Testy triedy v top 5 | Úlohy (gen gpt-5-mini) | Úlohy (gen gpt-5.4-nano) |
|---|---|---|---|---|---|---|
| gpt-6-luna | 71 | 1.0 | 1.00 | 10/10 | **10.0 ± 0.0** | 9.7 ± 0.6 |
| gpt-5.6-luna | 74 | 0.9 | 0.95 | 10/10 | **10.0 ± 0.0** | **10.0 ± 0.0** |
| gpt-4o-mini | 104 | 0.9 | 0.95 | 9/10 | 9.7 ± 0.6 | 9.7 ± 0.6 |
| gpt-5-mini | 103 | 1.0 | 1.00 | 10/10 | 9.0 ± 0.0 | 8.3 ± 0.6 |
| gpt-5.4-nano | 108 | 1.0 | 1.00 | 10/10 | 9.0 ± 0.0 | 8.7 ± 0.6 |
| gpt-5-nano | 116 | 1.0 | 1.00 | 10/10 | 9.0 ± 0.0 | 8.0 ± 1.0 |

- Gold chunk (trieda so stubom) je pri všetkých modeloch popisov v top 5 (R@5 = 1.0); 2 modely ho majú raz na 2. mieste.
- Rozdiel je v **ostatných 4 chunkoch**: pri popisoch od luna / gpt-4o-mini sa pre `BulkDiscountPricing.price` dostane do top 5 `pricing.py::000` (FlatPricing, obsahuje `Money(subtotal.cents * self._tax_bps // 10000)`); pri gpt-5-mini/nano popisoch je na jeho mieste `tests/test_base.py::002`.
  → s týmto vzorom `price` prejde 3/3, bez neho 0/3 – pri oboch generačných modeloch.
- Trieda `Money` nie je v top 5 pri žiadnom store; úlohu „zachráni“ susedná trieda, ktorá Money používa.
- Luna popisy sú kratšie (71–74 slov vs. 103–116) a sústredenejšie na účel triedy.
- R@1 / MRR gold chunku nepredpovedá výsledok – podstatné je zloženie celého top 5.

## 5. Zhrnutie findings

- RAG s top 5 chunkami (~2.7k tokenov, ~7 % repozitára) stačí na 10/10 úloh a 481/481 testov.
- Najväčší vplyv na výsledok mal **obsah top 5 mimo gold chunku** (závislosti, príklady použitia API), nie poradie gold chunku.
- Model na popisy chunkov ovplyvnil výsledok viac než voľba generačného modelu: gpt-5.4-nano s luna popismi (10/10) > gpt-5-mini s vlastnými popismi (9/10).
- Malé modely (nano) stačia na generovanie, ak dostanú správny kontext; gpt-4o-mini je najrýchlejší, ale najslabší.
- Obmedzenie: 10 úloh × 3 opakovania – rozdiely ±1 úloha sú na hranici šumu.
