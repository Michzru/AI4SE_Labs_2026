# Task 1 Report – Choice of prompting frameworks

**Source of all frameworks:** the Frompting framework library, https://frompting.com/frameworks (ROSES and Zero-Shot were excluded as required).
**Prompts:** [prompts.md](prompts.md) (readable) and [prompts.json](prompts.json) (data file with `{{SCHEMA}}` / `{{QUESTION}}` placeholders).

## The problem the prompts must solve (Task 2)
Text-to-SQL on a small restaurants database (RESTAURANT, LOCATION, GEOGRAPHIC). 155 questions are labelled with the rows the correct query returns, as `(house_number, name)` pairs. Three things make it non-trivial: a join through LOCATION and GEOGRAPHIC, the semantics of "best" (max rating) and "rating above X", and many questions padded with irrelevant sentences, plus questions whose correct answer is an empty set. Scoring is by exact row-set match after executing the SQL, so the prompt must fix the SELECT list and output only executable SQL.

## Why each framework

| | Framework | Category on Frompting | Why chosen | What I expect |
|---|---|---|---|---|
| A | **ICIO** – Instruction, Context, Input, Output | AI & Prompt Engineering | Recommended there for data-processing tasks; it separates the task, the schema and rules, the question, and the output format. | Most reliable *format* compliance (SQL only, right column order). Fixed rules in Context should give correct "best" and "above" semantics. Weakness: no demonstration, so unusual cases (region, ties, noise) rely on the model's reading of the rules. |
| B | **Few-Shot** | Communication & Storytelling | Examples are the strongest way to show exact conventions (lowercase literals, aliases, `MAX(RATING)` subquery, region join, noisy question). | Likely the highest accuracy, since the examples show the target pattern and how to ignore distractors. Cost: longer prompt, so slightly more input tokens and latency; risk of copying an example too closely. |
| C | **CoT** – Chain of Thought | Reasoning & Analysis | Tests whether explicit step-by-step reasoning (strip noise, list filters, map to columns, choose joins) helps on multi-condition questions. | Better at noisy and multi-join questions, but the longest outputs and slowest inference, and a risk that extra text breaks parsing (hence the fixed `SQL:` final line). |

## Why this set
The three differ in the one thing being compared: **structure only** (ICIO), **structure + demonstrations** (Few-Shot), **structure + reasoning** (CoT). All carry the same schema and the same data facts, so differences in Task 2 results can be attributed to the technique rather than to different information. The expected trade-off to measure in Task 2 is accuracy against inference time and tokens.

## Notes for Task 2
- Start a new session per prompt, as required.
- Extract SQL from prompt C's output from the line starting `SQL:`.
- The few-shot SQL examples were executed against the database and reproduce their labelled results; they come from the dataset's own questions, so exclude those 4 questions from scoring or note it in the report if you want a clean comparison.

## Change made while running Task 2
The first CoT wording asked the model to write out its reasoning ("Reasoning:"). The CLI blocked many such calls (`reasoning_extraction` policy error). Prompt C was therefore reformulated as a step-wise decomposition with a compact fixed-format answer (IGNORE / FILTERS / TABLES / RATING / SQL). Same framework idea, but the intermediate steps are a short structured output rather than free-form reasoning.
