# Report – Task 4: Matching embeddingov

**Výstup:** [`output/code/retrieve.py`](output/code/retrieve.py)
- `top_n(query_embedding, n=5)` → zoznam `(chunk, score)` zoradený od najrelevantnejšieho
- `search(task_text, n=5)` → embedne text úlohy (`embed_query` z Task 3) a zavolá `top_n` (použije Task 5)
- CLI: `python retrieve.py "<text úlohy>" [n]`

---

## 1. Rozhodnutia

| Rozhodnutie | Voľba | Dôvod |
|---|---|---|
| Metrika | **kosínusová podobnosť** | pozri nižšie |
| Výpočet | `matrix @ q` nad L2-normalizovanými vektormi | pri jednotkových vektoroch je kosínus = skalárny súčin → jeden maticový súčin |
| Vyhľadávanie | presné, brute force (všetkých 95 chunkov) | 95 × 384 floatov; ANN index (FAISS, HNSW) by pridal závislosť a aproximáciu bez prínosu |
| Výber top n | `argpartition` (O(N)) + zoradenie len n víťazov | netreba triediť celé pole |
| Načítanie úložiska | raz, `lru_cache` | Task 5 robí 10 dopytov, JSON sa nečíta opakovane |
| Normalizácia | aj uložené vektory, aj query | ochrana pred zaokrúhlením na 6 desatinných miest v JSON |
| Prah skóre | žiadny | skóre sú stlačené (top-5 priemer 0.73, top-1 0.84) – prah by nič neoddelil, Task 5 aj tak chce pevne 5 |
| Vyváženie zdroj/testy | žiadne | prirodzene vychádza 25 zdroj / 25 testy (viď findings) |

**Prečo kosínusová podobnosť:**
- `bge-small-en-v1.5` je trénovaný kontrastívne práve s kosínusovou podobnosťou – smer vektora nesie význam, dĺžka nie.
- Je nezávislá od dĺžky vektora → dlhší popis chunku nemá výhodu len preto, že je dlhší (pri čistom skalárnom súčine bez normalizácie by mal).
- Euklidovská vzdialenosť na normalizovaných vektoroch dá rovnaké poradie (‖a−b‖² = 2 − 2·cos), takže iná metrika nič nezlepší, len je drahšia.
- Výsledok je v rozsahu [−1, 1] → čitateľné a porovnateľné skóre.

## 2. Overenie – findings

10 úloh z `missing_code.json`, query = „Implement method M of class C in F. <docstring>“.

| Metrika | Hodnota |
|---|---|
| Gold chunk (trieda s metódou) na 1. mieste | **10/10** |
| Testy danej triedy v top 5 | **10/10** |
| Zloženie top 5 (všetky úlohy spolu) | 25 zdrojových / 25 testovacích chunkov |
| Skóre top-1 (priemer) | 0.844 |
| Skóre top-5 (priemer) | 0.730 |
| Rozdiel 1. a 2. miesta | priemer 0.044, min 0.013 |
| Latencia `top_n` | 0.006 ms / dopyt |
| `argpartition` vs. úplné zoradenie | rovnaké poradie (overené na všetkých 95) |

Príklad – `Customer.can_afford`:

| Skóre | Chunk |
|---|---|
| 0.864 | `models.py` – Customer (obsahuje stub) |
| 0.807 | `test_models.py` – CustomerTests |
| 0.718 | `test_models.py` – CustomerTests (2. časť) |
| 0.703 | `orders.py` – OrderBuilder |
| 0.683 | `test_orders.py` – pomocné `_customer`, `_order` |

- Top 5 typicky = trieda so stubom + jej testy + súvisiace triedy (napr. `OrderStatus.is_terminal` → `OrderStateMachine`, ktorý statusy používa).
- Malý rozdiel medzi 1. a 2. miestom (min 0.013) – poradie je správne, ale pri väčšom repozitári by mohlo byť krehké.
