# Task 1 – Prompts for Task 2 (natural-language question → SQL, restaurants database)

Placeholders: `{{SCHEMA}}` = restaurants-schema.csv, `{{QUESTION}}` = one dataset question. Machine-readable copy: prompts.json.

## Prompt A – ICIO (Instruction – Context – Input – Output)

```
### INSTRUCTION
Translate the natural-language question in the INPUT section into one SQLite SELECT query that retrieves matching restaurants. Ignore any part of the question that is unrelated to restaurants (jokes, food comparisons, small talk).

### CONTEXT
Database schema (table, field, primary key, foreign key, type):
{{SCHEMA}}

Rules about the data:
- RESTAURANT.ID = LOCATION.RESTAURANT_ID. RESTAURANT.CITY_NAME and LOCATION.CITY_NAME join to GEOGRAPHIC.CITY_NAME.
- All stored text is lowercase, so write string literals in lowercase.
- REGION (e.g. 'bay area') and COUNTY live in GEOGRAPHIC; the street is LOCATION.STREET_NAME.
- "best" means the highest RATING among the restaurants that fit the other conditions (return all ties).
- "rating above X" means RATING > X; the parenthesised words after the number are only a description.
- If nothing in the database can match (e.g. a food type that does not exist), the query should still be valid and simply return no rows.

### INPUT
Question: {{QUESTION}}

### OUTPUT
Return ONLY the SQL query, on a single statement, with no explanation, comments or markdown fences.
The SELECT list must be exactly: LOCATION.HOUSE_NUMBER, RESTAURANT.NAME (in this order).
```

## Prompt B – Few-Shot (Few-Shot Learning)

```
You convert questions about restaurants into SQLite queries. Study the examples, then answer the last question in the same way.

Schema:
{{SCHEMA}}

Conventions: RESTAURANT.ID = LOCATION.RESTAURANT_ID; city links to GEOGRAPHIC.CITY_NAME; all text is lowercase; the SELECT list is always LOCATION.HOUSE_NUMBER, RESTAURANT.NAME; irrelevant sentences in the question are ignored. Output only the SQL.

Question: What is the best californian in portola valley ?
SQL: SELECT L.HOUSE_NUMBER, R.NAME FROM RESTAURANT R JOIN LOCATION L ON L.RESTAURANT_ID = R.ID WHERE R.FOOD_TYPE = 'californian' AND R.CITY_NAME = 'portola valley' AND R.RATING = (SELECT MAX(RATING) FROM RESTAURANT WHERE FOOD_TYPE = 'californian' AND CITY_NAME = 'portola valley');

Question: While comparing dumplings with pancakes for an imaginary picnic, give me a restaurant on timber creek dr in san jose with a rating above 1.7 (poorly rated or better)?
SQL: SELECT L.HOUSE_NUMBER, R.NAME FROM RESTAURANT R JOIN LOCATION L ON L.RESTAURANT_ID = R.ID WHERE L.STREET_NAME = 'timber creek dr' AND L.CITY_NAME = 'san jose' AND R.RATING > 1.7;

Question: what is the best basque in the bay area ?
SQL: SELECT L.HOUSE_NUMBER, R.NAME FROM RESTAURANT R JOIN LOCATION L ON L.RESTAURANT_ID = R.ID JOIN GEOGRAPHIC G ON G.CITY_NAME = R.CITY_NAME WHERE R.FOOD_TYPE = 'basque' AND G.REGION = 'bay area' AND R.RATING = (SELECT MAX(R2.RATING) FROM RESTAURANT R2 JOIN GEOGRAPHIC G2 ON G2.CITY_NAME = R2.CITY_NAME WHERE R2.FOOD_TYPE = 'basque' AND G2.REGION = 'bay area');

Question: What is the best place in winters for tea food ?
SQL: SELECT L.HOUSE_NUMBER, R.NAME FROM RESTAURANT R JOIN LOCATION L ON L.RESTAURANT_ID = R.ID WHERE R.FOOD_TYPE = 'tea' AND R.CITY_NAME = 'winters' AND R.RATING = (SELECT MAX(RATING) FROM RESTAURANT WHERE FOOD_TYPE = 'tea' AND CITY_NAME = 'winters');

Question: {{QUESTION}}
SQL:
```

## Prompt C – CoT (Chain of Thought, as step-wise decomposition)

```
You are translating a question about restaurants into a SQLite query, decomposing the problem into sub-steps before writing the final SQL.

Schema:
{{SCHEMA}}

Facts: RESTAURANT.ID = LOCATION.RESTAURANT_ID; RESTAURANT.CITY_NAME / LOCATION.CITY_NAME join to GEOGRAPHIC.CITY_NAME; all stored text is lowercase; "best" = highest RATING among matching restaurants (keep ties); "rating above X" = RATING > X; the SELECT list must be LOCATION.HOUSE_NUMBER, RESTAURANT.NAME.

Question: {{QUESTION}}

Solve it in sub-steps and report the result of each sub-step in exactly this compact format (one short line each, no long explanations):
IGNORE: <words of the question that are irrelevant to restaurants, or "none">
FILTERS: <food type / city / street / region / county / rating condition / best, as column = value>
TABLES: <tables that must be joined and the join conditions>
RATING: <how "best" or the rating threshold is expressed>
SQL: <the finished single-statement SQLite query>

The SQL: line must be last, and nothing may follow the query.
```
