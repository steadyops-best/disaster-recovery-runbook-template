# SteadyOps DR Readiness Scorecard

Version: 1.0.0

| Area | 0 — Unknown | 1 — Documented | 2 — Proven |
|---|---|---|---|
| RPO/RTO | Not agreed | Documented | Measured in a drill |
| Backup source | Freshness unknown | Monitored | Clean restore evidenced |
| Failover path | No tested path | Procedure documented | Controlled failover completed |
| Restore path | No executable procedure | Commands documented | Isolated restore completed |
| Dependency order | Unknown | Listed | Validated in a drill |
| Decision ownership | No owner | Owner documented | Ownership exercised |
| Technical validation | Guessed | Checks documented | Checks executed |
| Business validation | Not defined | Critical transaction identified | Business owner validated recovery |
| Communications | Ad hoc | Template and owner documented | Timeline exercised |
| Evidence | None | Location defined | Drill report and follow-up retained |

## Interpretation

- 0–7: recovery depends on assumptions.
- 8–14: a usable foundation exists, but important controls remain unproven.
- 15–18: recovery is partly exercised; close the remaining evidence gaps.
- 19–20: strong readiness, provided the drill is recent and matches the current architecture.
