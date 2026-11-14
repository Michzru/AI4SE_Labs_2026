# Report – Task 3: Embeddingy chunkov

**Výstupy**
- skript chunk → embedding: [`output/code/embed_chunks.py`](output/code/embed_chunks.py) (`embed_documents`, `embed_query`)
- storage párov chunk–embedding: [`output/code/chunk_store.json`](output/code/chunk_store.json)
- cache LLM popisov: [`output/code/summaries.json`](output/code/summaries.json)
- overenie výberu: [`output/code/eval_embeddings.py`](output/code/eval_embeddings.py)

Závislosti: `openai`, `python-dotenv`, `numpy`, `fastembed`, `tiktoken` (`requirements.txt`). Kľúč v `code/.env` (`API_KEY`), `.env` je v `.gitignore`.

---

## 1. Overenie API kľúča – findings

| Test | Výsledok |
|---|---|
| Formát `.env` | `API_KEY=sk-svca…`, 167 znakov, bez bodky na konci, bez úvodzoviek a medzier |
| `models.list` | OK – 6 modelov: gpt-4o-mini, gpt-5-mini, gpt-5-nano, gpt-5.4-nano, gpt-5.6-luna, gpt-6-luna |
| `gpt-5-mini`, `gpt-5-nano`, `gpt-5.4-nano` | OK |
| `gpt-4.1-nano` | 404 – deprecated |
| `text-embedding-3-small` | **403 – projekt nemá prístup k embedding modelom** |

→ Embedding sa musí počítať lokálne; OpenAI sa použije len na generovanie popisu chunku.

## 2. Rozhodnutia

| Rozhodnutie | Voľba | Dôvod |
|---|---|---|
| Čo embedovať | LLM popis chunku v angličtine + lokátor (`File`, `Class`, `Defines: <triedy a metódy>`) | otázka (zadanie úlohy) je v prirodzenom jazyku; popis aj kód sú tak v rovnakom „jazyku“ |
| Model na popis | `gpt-5-mini`, `reasoning_effort=low` | presnejší než nano; 95 chunkov za ~40 s, cena zanedbateľná |
| Prompt popisu | 3–6 viet, mená metód, výnimky, návratové hodnoty; `pass` metódy označiť „not implemented yet“ + čo majú robiť; pri testoch čo testujú | chunk s chýbajúcou metódou má byť nájdený podľa popisu toho, čo metóda má robiť |
| Embedding model | `BAAI/bge-small-en-v1.5` cez `fastembed` (lokálne, ONNX, bez torch) | 384 dimenzií, silný na retrieval, limit 512 tokenov stačí na popisy (max 353) |
| Query embedding | `query_embed` (bge inštrukčný prefix pre otázky) | bge je trénovaný asymetricky: query vs. passage |
| Normalizácia | L2 (fastembed) | kosínusová podobnosť = skalárny súčin (Task 4) |
| Storage | jeden JSON: metadáta, `text`, `summary`, `embed_text`, `embedding` | 95 × 384 ≈ 740 KB; vektorová DB je zbytočná; samostatný súbor pre Task 4/5 |
| Cache popisov | `summaries.json` podľa `id` chunku | opakované spustenie nevolá LLM |

Ukážka `embed_text` (chunk so stubom `Customer.can_afford`):

> File: playground/playground/models.py · Class: Customer · Defines: Customer, \_\_init\_\_, …, can_afford, charge
> Defines class Customer(Entity) representing a buyer with a credit limit … can_afford(self, total: Money) is not implemented yet; based on its name and use it should return True if charging total would not exceed the credit limit …

## 3. Porovnanie reprezentácií – findings

Eval: 10 úloh z `missing_code.json`, gold = chunk obsahujúci `class X` + `def method`.
Dva typy otázok: **full** = „Implement method M of class C in F. <docstring>“, **doc_only** = len docstring.

| Reprezentácia | Query | R@1 | R@5 | MRR |
|---|---|---|---|---|
| **LLM popis + lokátor (zvolené)** | full | **1.00** | **1.00** | **1.00** |
| LLM popis + lokátor, bez mien metód | full | 0.90 | 1.00 | 0.95 |
| Surový kód, rovnaký bge model | full | 0.60 | 0.90 | 0.74 |
| TF-IDF nad kódom (bez modelu) | full | 0.30 | 0.90 | 0.58 |
| LLM popis + lokátor | doc_only | 0.30 | 0.80 | 0.50 |
| Surový kód, bge | doc_only | 0.40 | 0.70 | 0.57 |
| TF-IDF nad kódom | doc_only | 0.30 | 0.80 | 0.50 |

- **Nekompatibilný embedding (surový kód do bge-small):** 56 z 95 chunkov má > 512 bge tokenov (max 1 001) → model zvyšok oreže. Najhorší prípad: `OrderStatus.is_terminal` na 74. mieste pri doc_only. Popisy majú max 353 tokenov → nič sa neoreže.
- Pridanie mien metód do `Defines:` posunulo `Money.__bool__` z 2. na 1. miesto (R@1 0.90 → 1.00).
- Pri doc_only (bez mien) sú všetky metódy slabé (R@5 0.7–0.8): krátky docstring („Return a mapping of SKU to available quantity.“) nestačí. → V Task 5 query musí obsahovať triedu, metódu a súbor.
- Eval má len 10 otázok – výsledky sú orientačné.
