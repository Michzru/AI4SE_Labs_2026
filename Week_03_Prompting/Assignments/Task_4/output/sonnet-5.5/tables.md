# Tables (auto-generated) - Sonnet 5.5

## Accuracy, pairwise (exact McNemar, Holm-adjusted)

| A | B | only A correct | only B correct | acc A - acc B [95 % CI] | p | p (Holm) |
|---|---|---|---|---|---|---|
| ICIO | Few-Shot | 1 | 8 | -4.5 pt [-8.4, -1.3] | 0.0391 | 0.0781 |
| ICIO | CoT | 7 | 2 | +3.2 pt [-0.6, +7.1] | 0.1797 | 0.1797 |
| Few-Shot | CoT | 12 | 0 | +7.7 pt [+3.9, +12.3] | 0.0005 | 0.0015 |

Cochran's Q (all three prompts): Q = 14.53, df = 2, p = 0.0007

## Other metrics (Friedman + pairwise Wilcoxon, Holm-adjusted)

| Metric | Friedman p | ICIO | Few-Shot | CoT | Pair | mean diff [95 % CI] | p (Holm) |
|---|---|---|---|---|---|---|---|
| row-F1 | 0.00111 | 0.921 | 0.966 | 0.895 | ICIO - Few-Shot | -0.0452 [-0.0839, -0.0129] | 0.0393 |
| | | | | | ICIO - CoT | +0.0258 [-0.00651, +0.0645] | 0.177 |
| | | | | | Few-Shot - CoT | +0.071 [+0.0323, +0.116] | 0.00318 |
| wall time (s) | 1.03e-33 | 3.91 | 3.6 | 4.95 | ICIO - Few-Shot | +0.302 [+0.13, +0.47] | 9.77e-08 |
| | | | | | ICIO - CoT | -1.05 [-1.23, -0.845] | 6.14e-17 |
| | | | | | Few-Shot - CoT | -1.35 [-1.55, -1.15] | 6.06e-21 |
| API time (s) | 7.84e-41 | 2.4 | 2.21 | 3.42 | ICIO - Few-Shot | +0.193 [+0.0785, +0.31] | 1.13e-07 |
| | | | | | ICIO - CoT | -1.02 [-1.16, -0.878] | 1.54e-21 |
| | | | | | Few-Shot - CoT | -1.21 [-1.37, -1.07] | 7.03e-24 |
| output tokens | 2.28e-63 | 207 | 145 | 401 | ICIO - Few-Shot | +62.5 [+50.2, +76.3] | 1.19e-24 |
| | | | | | ICIO - CoT | -193 [-211, -176] | 1.19e-24 |
| | | | | | Few-Shot - CoT | -256 [-273, -239] | 1.32e-25 |
| billed tokens | 6.11e-35 | 3.4e+03 | 3.31e+03 | 4.27e+03 | ICIO - Few-Shot | +87.4 [-958, +1.14e+03] | 9.04e-11 |
| | | | | | ICIO - CoT | -870 [-2.17e+03, +422] | 1.47e-09 |
| | | | | | Few-Shot - CoT | -957 [-2.13e+03, +199] | 4.41e-07 |
| cost (USD) | 5.59e-24 | 0.016 | 0.0186 | 0.0207 | ICIO - Few-Shot | -0.00262 [-0.00339, -0.00186] | 1.39e-09 |
| | | | | | ICIO - CoT | -0.0047 [-0.00697, -0.00305] | 1.73e-11 |
| | | | | | Few-Shot - CoT | -0.00208 [-0.00431, -0.000508] | 0.1 |