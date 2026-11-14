# Report – Task 2: Chunking repozitára

**Výstupy**
- skript: [`output/code/chunk_repo.py`](output/code/chunk_repo.py)
- chunky: [`output/code/chunks.json`](output/code/chunks.json)

Spustenie: `python chunk_repo.py [REPO_ROOT] [OUTPUT_JSON]` (tokeny cez `tiktoken`, bez neho odhad znaky/4).

---

## 1. Analýza repozitára – findings

Merané `.py` súbory, tokenizer `tiktoken o200k_base` (gpt-4o / 4.1 / 5 modely z Task 5).

| Metrika | Hodnota |
|---|---|
| `.py` súbory | 27 (13 zdroj, 14 testy) |
| Znaky | 159 562 |
| Tokeny | **38 189** (cl100k: 36 915) |
| Zdrojový kód / testy | 10 930 (29 %) / 27 259 (71 %) |
| Znaky na token | ~4.2 |
| Najväčší súbor | `tests/test_models.py` – 4 616 tok |

| Jednotka (AST) | Počet | Medián | p90 | Max |
|---|---|---|---|---|
| Trieda | 99 | 283 tok | 697 tok | 1 420 tok |
| Metóda | 664 | 43 tok | 87 tok | 408 tok |
| Top-level funkcia | 9 | 129 tok | 158 tok | 183 tok |

- 97 % metód ≤ 128 tok, 100 % ≤ 512 tok.
- Celý repozitár (38k tok) sa zmestí do kontextu modelov s 128k+ oknom.
- Chýbajúce metódy (`missing_code.json`) sú v kóde ako `pass` stuby, vždy vo vnútri triedy.
- Task 5 posiela do LLM top 5 chunkov → pri ~500 tok/chunk je prompt ~3k tok (~8 % repozitára).

## 2. Rozhodnutia

| Rozhodnutie | Voľba | Dôvod |
|---|---|---|
| Metóda splittingu | AST (triedy / funkcie / príkazy na top-level) | hranice nerežú metódy; úlohy sú na úrovni „metóda v triede“ |
| Cieľová veľkosť | 500 tok | ~90 % tried sa zmestí celých (p90 = 697) |
| Max veľkosť | 800 tok | väčšie triedy sa delia po metódach |
| Min veľkosť | 100 tok | menšie skupiny (samotné importy, `if __name__`) sa zlúčia so susedom |
| Zlučovanie | susedné malé jednotky do 500 tok | metóda (medián 43 tok) je samostatne príliš malá |
| Overlap | žiadny | hranice sú sémantické; kontext dodáva hlavička |
| Kontext pri delení triedy | každá časť má hlavičku triedy (signatúra, docstring, atribúty) + `# ...` | časť triedy nestratí, kam patrí |
| Hlavička chunku | `# file: <path> (lines a-b)` + `# class: <Name>` | embedding aj LLM vidia umiestnenie |
| Testy | chunkované tiež | testy popisujú očakávané správanie chýbajúcich metód |
| Dátová štruktúra | JSON zoznam objektov | jednoduché, čitateľné, ľahko sa načíta v Task 3 |

Schéma chunku:

```json
{ "id": "playground/playground/orders.py::001", "file": "...", "kind": "module|class|class_part",
  "names": ["Order"], "class_name": "Order", "start_line": 40, "end_line": 120,
  "n_tokens": 685, "header": "# file: ...", "code": "...", "text": "header + code" }
```

## 3. Výsledok – findings

| Metrika | Hodnota |
|---|---|
| Počet chunkov | **95** (28 zdroj, 67 testy) |
| Typy | 39 `class`, 40 `module`, 16 `class_part` |
| Tokeny p10 / medián / p90 / max | 211 / 442 / 637 / 800 |
| Chunky > 800 tok | 0 |
| Chunky < 100 tok | 3 (sused by prekročil 800) |
| Súčet tokenov | 40 085 (+5 % oproti repozitáru kvôli hlavičkám) |

Overenie:
- Každý neprázdny riadok repozitára je v niektorom chunku (0 chýbajúcich).
- Všetky nedelené chunky (79/79) sú validný Python (`ast.parse`).
- Každá z 10 metód z `missing_code.json` je práve v jednom chunku spolu so svojou triedou.

Iterácia: prvá verzia mala 103 chunkov, z toho 9 pod 100 tok (samostatné importy,
`if __name__ == "__main__"` s 27 tok, krátke posledné časti tried) a duplicitné názvy `<imports>`.
Pridaný krok zlučovania malých skupín a deduplikácia → 95 chunkov, 3 malé.
