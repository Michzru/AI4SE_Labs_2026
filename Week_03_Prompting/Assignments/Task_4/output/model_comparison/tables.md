# Tables (auto-generated) - Sonnet 5.5 vs Opus 5.5

## All six conditions

| Model | Prompt | Accuracy [95 % CI] | Correct | Row-F1 | Mean wall time | Mean API time | Output tokens | Cost / question |
|---|---|---|---|---|---|---|---|---|
| Sonnet 5.5 | ICIO | 88.4 % [83.2, 93.5] | 137 | 0.921 | 3.91 s | 2.40 s | 207 | $0.0160 |
| Sonnet 5.5 | Few-Shot | 92.9 % [88.4, 96.8] | 144 | 0.966 | 3.60 s | 2.21 s | 145 | $0.0186 |
| Sonnet 5.5 | CoT | 85.2 % [79.4, 90.3] | 132 | 0.895 | 4.95 s | 3.42 s | 401 | $0.0207 |
| Opus 5.5 | ICIO | 92.9 % [88.4, 96.8] | 144 | 0.932 | 4.07 s | 3.73 s | 198 | $0.0191 |
| Opus 5.5 | Few-Shot | 93.5 % [89.7, 97.4] | 145 | 0.959 | 3.87 s | 3.44 s | 150 | $0.0236 |
| Opus 5.5 | CoT | 87.1 % [81.9, 92.3] | 135 | 0.880 | 5.89 s | 5.66 s | 441 | $0.0235 |

Cochran's Q over all six conditions: Q = 20.11, df = 5, p = 0.00119

## Model effect within each prompt (Opus 5.5 - Sonnet 5.5), accuracy: exact McNemar, Holm over the 3 prompts

| Prompt | only Opus 5.5 correct | only Sonnet 5.5 correct | difference [95 % CI] | p | p (Holm) |
|---|---|---|---|---|---|
| ICIO | 12 | 5 | +4.5 pt [-0.6, +9.7] | 0.143 | 0.43 |
| Few-Shot | 5 | 4 | +0.6 pt [-3.2, +4.5] | 1 | 1 |
| CoT | 11 | 8 | +1.9 pt [-3.2, +7.1] | 0.648 | 1 |

## Model effect on other metrics (Opus 5.5 - Sonnet 5.5), Wilcoxon signed-rank, Holm over the 3 prompts

| Metric | Prompt | Sonnet 5.5 | Opus 5.5 | difference [95 % CI] | p (Holm) |
|---|---|---|---|---|---|
| row-F1 | ICIO | 0.9206 | 0.9323 | +0.0116 [-0.0307, +0.0535] | 0.889 |
| row-F1 | Few-Shot | 0.9658 | 0.9595 | -0.00633 [-0.0386, +0.026] | 1 |
| row-F1 | CoT | 0.8948 | 0.8801 | -0.0147 [-0.0581, +0.0291] | 1 |
| wall time (s) | ICIO | 3.907 | 4.065 | +0.158 [-0.0431, +0.35] | 0.000741 |
| wall time (s) | Few-Shot | 3.604 | 3.869 | +0.265 [+0.056, +0.465] | 1.31e-06 |
| wall time (s) | CoT | 4.952 | 5.894 | +0.942 [+0.674, +1.22] | 8.37e-11 |
| API time (s) | ICIO | 2.398 | 3.726 | +1.33 [+1.19, +1.47] | 4.15e-25 |
| API time (s) | Few-Shot | 2.206 | 3.443 | +1.24 [+1.1, +1.39] | 1.05e-23 |
| API time (s) | CoT | 3.42 | 5.659 | +2.24 [+1.99, +2.5] | 1.79e-25 |
| output tokens | ICIO | 207.2 | 198.2 | -9 [-24.7, +5.84] | 0.429 |
| output tokens | Few-Shot | 144.7 | 150.3 | +5.63 [-3.06, +13.2] | 0.0656 |
| output tokens | CoT | 400.6 | 441.2 | +40.6 [+19.7, +62.6] | 0.181 |
| cost (USD) | ICIO | 0.01601 | 0.01907 | +0.00305 [+0.00223, +0.0039] | 1.43e-10 |
| cost (USD) | Few-Shot | 0.01863 | 0.02363 | +0.005 [+0.0037, +0.00679] | 9.28e-17 |
| cost (USD) | CoT | 0.02071 | 0.02352 | +0.00281 [+0.000245, +0.00546] | 1.59e-07 |

## Prompt x model interaction (gap between two prompts, in accuracy points)

| Prompt pair | gap with Sonnet 5.5 | gap with Opus 5.5 | change [95 % CI] |
|---|---|---|---|
| ICIO - Few-Shot | -4.5 | -0.6 | +3.9 [-1.3, +9.0] |
| ICIO - CoT | +3.2 | +5.8 | +2.6 [-3.2, +8.4] |
| Few-Shot - CoT | +7.7 | +6.5 | -1.3 [-7.1, +4.5] |

## Same question, same prompt: agreement between the models

| Prompt | both correct | only Sonnet 5.5 | only Opus 5.5 | neither |
|---|---|---|---|---|
| ICIO | 132 | 5 | 12 | 6 |
| Few-Shot | 140 | 4 | 5 | 6 |
| CoT | 124 | 8 | 11 | 12 |