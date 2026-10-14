# Task 2 report - prompt comparison on text-to-SQL (Sonnet 5.5, effort medium)

Each question was sent as an independent, stateless `claude -p` call (new session, no tools, no settings/CLAUDE.md). Time = wall clock of the whole CLI call; API time and time-to-first-token are as reported by the CLI. Correctness = executing the predicted SQL on the database and comparing the row multiset with the label (same rule as `evaluate_retrieval_predictions.py`); SQL that fails to execute counts as wrong.

| Prompt | n | Accuracy | Acc. excl. few-shot ex. | Invalid SQL | Mean time | Median | P95 | Mean API time | Mean out tokens | Mean prompt tokens | Total cost |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ICIO | 155 | 88.4% | 88.1% (n=151) | 0 | 3.91s | 3.44s | 5.52s | 2.40s | 207 | 3189 | $2.48 |
| Few-Shot | 155 | 92.9% | 92.7% (n=151) | 0 | 3.60s | 3.22s | 5.74s | 2.21s | 145 | 3164 | $2.89 |
| CoT | 155 | 85.2% | 84.8% (n=151) | 0 | 4.95s | 4.51s | 6.62s | 3.42s | 401 | 3865 | $3.21 |

![comparison](comparison.png)

## Findings

- Most accurate: **Few-Shot** (92.9%).
- Fastest: **Few-Shot** (3.60s mean per question).

## Where prompts disagree

- Questions solved by all prompts: 130; solved by none: 10.

- row 9: _What is the best delivery in rio del mar ?_ -> ICIO: correct, Few-Shot: correct, CoT: wrong
- row 22: _what is a restaurant in alameda with a rating above 2 (below average or better)?_ -> ICIO: wrong, Few-Shot: wrong, CoT: wrong
- row 25: _A very long menu debate has occupied my afternoon: should a picnic feature warm noodles, cold muffins, or an e_ -> ICIO: wrong, Few-Shot: wrong, CoT: wrong
- row 27: _what are some restaurants in alameda with a rating above 2 (below average or better)?_ -> ICIO: wrong, Few-Shot: wrong, CoT: wrong
- row 29: _what are some restaurants in santa cruz with a rating above 2.5 (average or better)?_ -> ICIO: wrong, Few-Shot: wrong, CoT: wrong
- row 34: _what is a restaurant in lafayette with a rating above 2 (below average or better)?_ -> ICIO: wrong, Few-Shot: wrong, CoT: wrong
- row 36: _where can i eat some vietnamese food on shellmound st # 12 in emeryville with a rating above 1.7 (poorly rated_ -> ICIO: wrong, Few-Shot: wrong, CoT: wrong
- row 51: _give me a restaurant on san pablo ave # a in pinole for deli food with a rating above 2 (below average or bett_ -> ICIO: wrong, Few-Shot: correct, CoT: wrong

_Add your own interpretation here (why a prompt failed, error categories, trade-off accuracy vs. time/tokens)._
