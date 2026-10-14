# Tables (auto-generated) - Opus 5.5

## Accuracy, pairwise (exact McNemar, Holm-adjusted)

| A | B | only A correct | only B correct | acc A - acc B [95 % CI] | p | p (Holm) |
|---|---|---|---|---|---|---|
| ICIO | Few-Shot | 7 | 8 | -0.6 pt [-5.8, +4.5] | 1.0000 | 1.0000 |
| ICIO | CoT | 12 | 3 | +5.8 pt [+1.3, +11.0] | 0.0352 | 0.0927 |
| Few-Shot | CoT | 14 | 4 | +6.5 pt [+1.3, +11.6] | 0.0309 | 0.0927 |

Cochran's Q (all three prompts): Q = 7.58, df = 2, p = 0.0226

## Other metrics (Friedman + pairwise Wilcoxon, Holm-adjusted)

| Metric | Friedman p | ICIO | Few-Shot | CoT | Pair | mean diff [95 % CI] | p (Holm) |
|---|---|---|---|---|---|---|---|
| row-F1 | 0.0257 | 0.932 | 0.959 | 0.88 | ICIO - Few-Shot | -0.0272 [-0.0677, +0.0114] | 0.277 |
| | | | | | ICIO - CoT | +0.0522 [+0.00794, +0.0993] | 0.12 |
| | | | | | Few-Shot - CoT | +0.0794 [+0.0346, +0.127] | 0.00783 |
| wall time (s) | 1.18e-40 | 4.07 | 3.87 | 5.89 | ICIO - Few-Shot | +0.196 [+0.00357, +0.385] | 0.00117 |
| | | | | | ICIO - CoT | -1.83 [-2.09, -1.58] | 2.12e-24 |
| | | | | | Few-Shot - CoT | -2.03 [-2.29, -1.76] | 3.33e-24 |
| API time (s) | 7.08e-47 | 3.73 | 3.44 | 5.66 | ICIO - Few-Shot | +0.283 [+0.121, +0.442] | 7.59e-05 |
| | | | | | ICIO - CoT | -1.93 [-2.18, -1.7] | 1.92e-26 |
| | | | | | Few-Shot - CoT | -2.22 [-2.47, -1.96] | 7.28e-25 |
| output tokens | 6.12e-62 | 198 | 150 | 441 | ICIO - Few-Shot | +47.8 [+35.9, +61.2] | 5.5e-18 |
| | | | | | ICIO - CoT | -243 [-263, -224] | 1.04e-26 |
| | | | | | Few-Shot - CoT | -291 [-312, -271] | 1.04e-26 |
| billed tokens | 2.23e-46 | 3.57e+03 | 4.2e+03 | 2.99e+03 | ICIO - Few-Shot | -623 [-1.71e+03, +450] | 4.3e-14 |
| | | | | | ICIO - CoT | +588 [-483, +1.66e+03] | 1.41e-11 |
| | | | | | Few-Shot - CoT | +1.21e+03 [+146, +2.29e+03] | 2.41e-17 |
| cost (USD) | 4.67e-30 | 0.0191 | 0.0236 | 0.0235 | ICIO - Few-Shot | -0.00457 [-0.00649, -0.00316] | 9.95e-14 |
| | | | | | ICIO - CoT | -0.00446 [-0.00663, -0.00291] | 3.2e-12 |
| | | | | | Few-Shot - CoT | +0.000112 [-0.00233, +0.00239] | 0.514 |