# Filled drill report — checkout after PostgreSQL recovery

This is a worked exercise with synthetic orders, timestamps, and evidence IDs. It illustrates what to record in an isolated drill. The RPO and RTO below are example objectives.

## Drill control and recovery contract

| Field | Example |
|---|---|
| Service and environment | Checkout API, isolated recovery environment |
| Simulated incident start | 10:07 UTC |
| Recovery source | Fixture base backup `BASE-01` and archived WAL on the selected exercise timeline |
| Target and fallback | Restore to 10:04 UTC. If the required WAL or timeline cannot be verified, stop and reassess the latest provably usable recovery point. |
| Objectives | At most 5 minutes of data loss (RPO) and verified checkout within 30 minutes (RTO) |
| Critical transaction | Complete a test checkout and match its order, payment, confirmation, and queued event |
| Decision authority | Exercise lead owns reopen or hold. Recovery operator executes restore. Checkout validator signs off the transaction. |
| Isolation | Production routing and workers remain fenced off. Payments and callbacks use a test provider. |

Stop if the restore source is uncertain, a pre-target order is missing, an external payment is unaccounted for, or replay can repeat a charge or shipment.

## Timeline and evidence

| UTC | Milestone | Observation | Evidence |
|---|---|---|---|
| 10:07 | Start the exercise | Checkout is declared unavailable and the clock starts. | TIMELINE-01 |
| 10:12 | Verify the recovery source | Base backup identity, target timeline, and required WAL match the exercise manifest. | RESTORE-01 |
| 10:23 | Complete technical checks | Database and application are healthy. Checkout remains on hold pending order reconciliation. | HEALTH-01 |
| 10:30 | Reconcile affected orders | The post-target payment is matched and a test replay preserves a single charge and a single order. | RECON-01 |
| 10:32 | Complete the business check | A fresh synthetic checkout reaches confirmation and the corresponding payment and queued event agree. The exercise lead approves reopening. | CHECKOUT-01 |

## Reconciliation ledger

The fixture contains two original committed orders in the interval under review. Its independent ledger was retained outside the restored database.

| Order | Original commit | Expected after restore | Observed and disposition |
|---|---|---|---|
| ORDER-A | 10:03:50 UTC | Present | Present, with the original payment state and matching transaction ID. |
| ORDER-B | 10:06:15 UTC | Absent at the selected target | Absent. The test provider retained the captured payment. Replay with the same transaction key restored the order without charging again. |
| ORDER-C | After restore, synthetic validation | New checkout completes once | One new order, one matching test payment and one expected queued event. |

## Decision and objectives

- **Decision:** Reopen in the exercise at 10:32 UTC. Keep production systems isolated.
- **Recovery point:** 10:04 UTC is three minutes before the simulated outage. The fixture ledger accounted for all committed orders in the checked interval. The exercise RPO was met.
- **Recovery time:** 25 minutes elapsed from simulated outage to business validation. The exercise RTO was met. The earlier 10:23 health result represented technical recovery.
- **If the result differs:** Keep checkout restricted, record the unresolved discrepancy, and assign reconciliation before another rerun or reopening decision.

## Follow-up

| Owner | Action | How to verify it |
|---|---|---|
| Checkout validator | Add a duplicate callback to the next fixture. | Both deliveries resolve to one order and one payment. |
| Recovery operator | Record the replay command and approved transaction key in the private runbook. | A second operator can repeat the cleanup on the isolated copy. |

Start your own record with the [blank drill report](../templates/dr-drill-report.md). Use the [checkout validation guide](../docs/verify-orders-after-postgresql-restore.md) to adapt these checks to your workflow.
