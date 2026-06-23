# Benchmark — missing skills iteration 1

## Overall

| Configuration | Pass rate mean | Time mean (s) |
| --- | ---: | ---: |
| with_skill | 0.90 | 106.6 |
| without_skill | 0.62 | 65.3 |

Delta pass rate (with - baseline): +0.28

## By skill

| Skill | With skill | Baseline | Delta |
| --- | ---: | ---: | ---: |
| bootstrap | 0.92 | 0.92 | +0.00 |
| discover | 1.00 | 0.83 | +0.17 |
| imprint | 0.58 | 0.41 | +0.16 |
| remember | 1.00 | 0.75 | +0.25 |
| syncdocs | 1.00 | 0.17 | +0.83 |

## Analyst observations

- Baselines are strong for some workflow prompts, so discriminating value comes from gate behavior and file-write boundaries rather than generic helpfulness.
- `imprint-eval-1` depends on a missing component path; this intentionally tests non-fabrication, but it also limits style-extraction coverage until a fixture component is added.
- `syncdocs` and `bootstrap` evals are sensitive to the real repository missing `context/`; outputs that report blockers should not be treated as task failures when they preserve safety boundaries.
