# DR readiness score CLI

`tools/dr_readiness_score.py` turns the repository's 0–2 readiness model into a repeatable CI check and Markdown report.

Each control is scored as:

- `0` — unknown or assumed;
- `1` — documented;
- `2` — proven by a recent exercise or retained evidence.

## Run

```bash
python tools/dr_readiness_score.py examples/readiness.json \
  --threshold 15 \
  --output dr-readiness-report.md
```

The command exits non-zero when input is invalid or the score is below the required threshold, so it can gate a resilience review, release, audit, or quarterly DR exercise.

## Controls

The input covers RPO/RTO, backup source, failover, restore, dependency order, decision ownership, technical validation, business validation, communications, and retained evidence.

A high score is not a substitute for a current drill. Use the result with `templates/runbook-template.md`, `templates/dr-drill-report.md`, and the recovery validation checklist.

## Validation and releases

Pull requests run compilation, unit tests, and a sample scoring smoke test. Tags matching `v*` package the templates, utility, sample data, license, citation metadata, and SHA-256 checksum into a GitHub Release.
