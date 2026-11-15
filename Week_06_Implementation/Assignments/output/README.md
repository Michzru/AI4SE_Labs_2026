# Week 06 – RAG na generovanie kódu

Jednoduchý RAG nad repozitárom `AI4SE_Playground`: chunking → embeddingy → retrieval → LLM doplní chýbajúce metódy → unit testy.
Výsledok: **10/10 úloh, 481/481 testov**.

## Reporty

| Task | Report | Obsah |
|---|---|---|
| 1 | [report_task1.md](../report_task1.md) | klonovanie repozitára |
| 2 | [report_task2.md](../report_task2.md) | veľkosť repozitára, AST chunking, veľkosť chunkov |
| 3 | [report_task3.md](../report_task3.md) | LLM popis chunku + lokálny embedding, porovnanie reprezentácií |
| 4 | [report_task4.md](../report_task4.md) | kosínusová podobnosť, top-n |
| 5 | [report_task5.md](../report_task5.md) | výsledky testov, porovnanie modelov na kód aj na popisy |
| 6 | [report_task6.md](../report_task6.md) | bonus: návrh ideálnej pipeline |

## Štruktúra

```
output/
├── week6/AI4SE_Playground/   naklonovaný repozitár (už s doplneným kódom)
└── code/
    ├── chunk_repo.py         Task 2 – chunking  -> chunks.json
    ├── embed_chunks.py       Task 3 – popis + embedding -> chunk_store.json
    ├── eval_embeddings.py    Task 3 – porovnanie reprezentácií
    ├── retrieve.py           Task 4 – top-n podľa kosínusu
    ├── solve_tasks.py        Task 5 – RAG riešenie úloh + testy
    ├── run_experiments.py    Task 5 – porovnanie modelov
    ├── llm.py                OpenAI klient
    ├── stores/               chunk store pre každý model na popisy
    ├── results/              výsledky behov (summary.json, run_*.json, test_map.json)
    └── backup_original/      pôvodné súbory so stubmi
```

## Spustenie

Do `code/.env` dať `API_KEY=...` (OpenAI), potom v `code/`:

```bash
pip install -r requirements.txt
python chunk_repo.py
python embed_chunks.py --summary-model gpt-5.6-luna
python solve_tasks.py --gen-model gpt-5-mini --summary-model gpt-5.6-luna
```

`python solve_tasks.py --reset` vráti pôvodné stuby. `python run_experiments.py` zopakuje porovnanie modelov.
