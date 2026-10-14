# Task 2 report - prompt comparison on text-to-SQL (Opus 5.5, effort medium)

Each question was sent as an independent, stateless `claude -p` call (new session, no tools, no settings/CLAUDE.md). Time = wall clock of the whole CLI call; API time and time-to-first-token are as reported by the CLI. Correctness = executing the predicted SQL on the database and comparing the row multiset with the label (same rule as `evaluate_retrieval_predictions.py`); SQL that fails to execute counts as wrong.

| Prompt | n | Accuracy | Acc. excl. few-shot ex. | Invalid SQL | Mean time | Median | P95 | Mean API time | Mean out tokens | Mean prompt tokens | Total cost |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ICIO | 155 | 92.9% | 92.7% (n=151) | 0 | 4.07s | 3.60s | 6.18s | 3.73s | 198 | 3375 | $2.96 |
| Few-Shot | 155 | 93.5% | 93.4% (n=151) | 0 | 3.87s | 3.40s | 6.01s | 3.44s | 150 | 4045 | $3.66 |
| CoT | 155 | 87.1% | 86.8% (n=151) | 0 | 5.89s | 5.48s | 9.14s | 5.66s | 441 | 2544 | $3.65 |

![comparison](comparison.png)

## Findings

- Most accurate: **Few-Shot** (93.5%).
- Fastest: **Few-Shot** (3.87s mean per question).

## Where prompts disagree

- Questions solved by all prompts: 128; solved by none: 3.

- row 9: _What is the best delivery in rio del mar ?_ -> ICIO: wrong, Few-Shot: correct, CoT: wrong
- row 12: _give me a restaurant on avenue near the alameda in belmont with a rating above 2.3 (below average or better)?_ -> ICIO: wrong, Few-Shot: correct, CoT: wrong
- row 27: _what are some restaurants in alameda with a rating above 2 (below average or better)?_ -> ICIO: correct, Few-Shot: wrong, CoT: correct
- row 29: _what are some restaurants in santa cruz with a rating above 2.5 (average or better)?_ -> ICIO: correct, Few-Shot: wrong, CoT: wrong
- row 34: _what is a restaurant in lafayette with a rating above 2 (below average or better)?_ -> ICIO: correct, Few-Shot: wrong, CoT: correct
- row 35: _where can i eat some mexican food on noriega in san francisco with a rating above 2 (below average or better)?_ -> ICIO: correct, Few-Shot: wrong, CoT: correct
- row 36: _where can i eat some vietnamese food on shellmound st # 12 in emeryville with a rating above 1.7 (poorly rated_ -> ICIO: wrong, Few-Shot: correct, CoT: wrong
- row 44: _where is a restaurant on n.shoreline blvd. in mountain view for sandwiches food with a rating above 2 (below a_ -> ICIO: wrong, Few-Shot: correct, CoT: correct

_Add your own interpretation here (why a prompt failed, error categories, trade-off accuracy vs. time/tokens)._
