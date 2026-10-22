Pokračujeme v Task 1 (Week_04_Requirements/Task_1): agentic network v LangGraph, ktorá z priečinka s textami
vyrobí jeden Markdown dokument s požiadavkami. Zadanie je v Task_1.md, dizajn v ARCHITECTURE.md (prečítaj len tieto dva
súbory a network.py, extraction.py; korpus v data/corpus nečítaj celý, má 145 kB).

Pracujeme spolu: ja píšem vlastný report, ty píšeš kód a vysvetľuješ každý krok (som v LangGraphe nový, vysvetli
pojmy stručne). Odpovedaj po slovensky, stručne.

Pravidlá:
- Pred každou novou časťou kódu urob git commit aktuálneho stavu. Commity bez značky Claude (žiadne
  Co-Authored-By, žiadne "Generated with"), autor je môj git user.
- API kľúč je v ../../.env (v koreni repozitára, gitignorovaný) ako OPENAI_API_KEY; načítaj ho cez
  python-dotenv (find_dotenv). Kľúč nikdy nevypisuj, necommituj ani nekopíruj.
- Python: ./.venv/bin/python (balíky v requirements.txt). Cesta ku korpusu je vždy argument, nič natvrdo.

Hotovo (commitnuté):
- network.py: State, uzly load_corpus a chunk_documents (lossless split, max 4000 znakov), graf START->load->chunk->END.
- extraction.py: Pydantic schéma Requirement (title, description, evidence, type, date), ExtractionResult, prompt extraktora.
- benchmark_extract.py: porovnanie modelov na extrakcii.

Výsledok benchmarku (3 vzorky, 1 beh): gpt-6-luna a gpt-5.6-luna majú najvyšší recall (v dense SRS chunku 43/41
požiadaviek), gpt-5.6-luna a gpt-5.4-nano majú 100 % doslovných citátov, gpt-5.4-nano je najrýchlejší ale v SRS
nájde len ~22, gpt-5-mini/gpt-5-nano sú pomalé (reasoning, až 13k tokenov), gpt-4.1-nano a gpt-4o-mini majú nízky recall.
Šum (Costco, knihy) nepreniká.

Rozhodnuté priradenie: extract=gpt-5.6-luna, review_completeness a merge_and_resolve=gpt-6-luna, prioritize=gpt-5.4-nano.

Ďalšie kroky (podľa ARCHITECTURE.md), po jednom, každý otestuj a vysvetli:
1. uzol extract (paralelne cez chunky cez LangGraph Send) + verify_evidence (kód, normalizovaná kontrola citátu, doplní source_doc)
2. review_completeness + feedback loop späť na extract (max 2 iterácie)
3. merge_and_resolve (dedup, konflikty -> blacklist s dôvodom, jednotná slovná zásoba)
4. prioritize (MoSCoW so škálou)
5. assign_ids + render_doc (Markdown, vrátane sekcie Blacklist a vysvetlenia priorít; kontrola špecifikácie)
6. spustenie na celom data/corpus, kontrola výstupu proti OS1-OS9, výstup uložiť do output/

Začni krokom 1. Najprv mi povedz stručný plán uzla, potom commit a kód.
