# Task 1 – Choice of prompting frameworks

## How I did it
I used Sonnet 5.5 (medium effort) in Claude Code. I copied the whole list of frameworks from https://frompting.com/frameworks into the input, gave it Task_1.md and let it look at the data of Task 2 (the restaurants database and the labelled questions). Based on that it proposed three frameworks and wrote one prompt for each of them. The prompts are in `prompts.json` (data) and `prompts.md` (readable). I checked the choice and agreed with it.

**Source of all three frameworks:** https://frompting.com/frameworks (ROSES and Zero-Shot were not used, as required).

**The problem the prompts have to solve (Task 2):** text-to-SQL. For a natural-language question about restaurants the model has to write a SQL query that returns `(house number, restaurant name)`. Many questions contain irrelevant sentences that have to be ignored, and some have an empty result.

## The three frameworks

**a) ICIO (Instruction – Context – Input – Output)**
- Why: on Frompting it is recommended for data-processing tasks where the format matters as much as the content. It keeps the task, the schema and rules, the question and the output format in separate sections.
- What I expected: the prompt should give a clean, correctly formatted answer (only SQL, right columns). Without examples it has to rely only on the written rules, so I expected it to be good but not the best.
- What happened: it was in the middle, 88.4 % accuracy (137/155) and the cheapest of the three.

**b) Few-Shot**
- Why: examples are the clearest way to show the exact SQL conventions (lowercase values, joins, `MAX(RATING)` for "best", region join, a question with irrelevant text). Found in the Communication & Storytelling category on Frompting.
- What I expected: the highest accuracy, because the model can copy the patterns. The price is a longer prompt.
- What happened: it was the best and also the fastest, 92.9 % accuracy (144/155), 3.60 s per question on average.

**c) Chain of Thought (CoT)**
- Why: I wanted to test whether step-by-step reasoning helps on questions with several conditions and noisy text. Found in the Reasoning & Analysis category on Frompting.
- What I expected: the longest inference time, but maybe better results on the harder questions.
- What happened: it was the slowest (4.95 s) and the least accurate (85.2 %, 132/155). The model wrote about twice to three times more output tokens than the others.
- Note: my first version asked the model to write out its reasoning ("Reasoning: ..."). The Claude CLI blocked many of those calls with a `reasoning_extraction` error. I therefore changed prompt C into a step-wise decomposition with a short fixed answer format (IGNORE / FILTERS / TABLES / RATING / SQL). It is the same idea, but the steps are a short structured output and not free-form reasoning, so it is not a "pure" CoT.

## Why these three together
They differ in one thing only: structure only (ICIO), structure + examples (Few-Shot), structure + reasoning steps (CoT). All of them contain the same schema and the same facts about the data, so the differences in Task 2 come from the technique and not from different information.
