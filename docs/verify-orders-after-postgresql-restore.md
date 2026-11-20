# Verify orders after a PostgreSQL point-in-time restore

During a checkout recovery drill, PostgreSQL can accept connections while some orders, payments, or queued events still need reconciliation. Use this exercise to decide whether checkout can reopen and to document the evidence behind that decision.

## Prepare an expected result

In a test environment, create a few orders through the normal application and keep an independent record of the committed IDs, UTC times, payment states, and resulting events. Include orders on both sides of the recovery target. Keep the record outside the database you will restore so a missing row cannot disappear from the expected results as well.

For an actual incident, use independent sources such as an authorized transaction export from the payment provider and gateway or application records. A request log is evidence that a request arrived. Confirm it against a committed order, an acknowledgement, or another authoritative record before treating it as a completed purchase.

Record the backup identity, selected PostgreSQL timeline, intended recovery target, and the transactions you expect just before and after it. PostgreSQL can replay archived WAL to a chosen recovery point. Use evidence from the restored data to confirm the resulting application state. [PostgreSQL point-in-time recovery documentation](https://www.postgresql.org/docs/current/continuous-archiving.html)

## Match transactions before reopening checkout

Restore to an isolated database and run an application version compatible with its schema and data. Disable outbound email, shipping calls, payment callbacks and production workers, or route them to test substitutes. Start by reading the restored state.

| Check | Evidence to retain | Stop condition |
|---|---|---|
| Orders expected before the target | Order IDs, amounts, states and commit evidence | A known committed order is missing or inconsistent |
| Orders committed after the target | IDs requiring replay or manual reconciliation and a named owner | A charge, order or shipment cannot be reconciled |
| Asynchronous work | Pending event IDs and the worker's duplicate-handling result | A replay can repeat an external side effect |
| Checkout through the app | One synthetic order from creation to confirmation using test integrations | The app reports success while order or payment state disagrees |

Match stable business identifiers, such as an order ID and an external transaction ID. A count of rows alone cannot tell you which orders need attention. Verify the recovery interval separately from the sampled check, and mark it unverified if there is insufficient evidence.

## Example decision from a drill

All IDs, times, and outcomes below are illustrative. The drill models an outage starting at 10:07 UTC. Its exercise goals are a five-minute recovery point objective (RPO) and 30 minutes to restore checkout (RTO).

- The restore targets **10:04 UTC**. An independently recorded order committed at **10:03:50** is present with the expected payment state. An order committed at **10:06:15** is absent, as expected for this target, and its payment is still present at the test provider.
- The target is three minutes before the outage, within the exercise's RPO window. The missing post-target order still needs a reconciliation decision before reopening.
- At **10:23**, the test database and application report healthy. At **10:30**, the operator matches the missing order to the payment and proves a test replay will not charge again. At **10:32**, the business validator confirms a new synthetic checkout and approves reopening. That is 25 minutes from the simulated outage to the verified customer outcome.

If the operator cannot prove the replay result, keep checkout restricted and record the open payment and order discrepancy. The technical health timestamp still helps diagnose delay, but the recovery outcome remains pending.

## Keep a reviewable record

Capture the backup and timeline, verified cutoff, missing orders and their disposition, duplicate-handling result, time of the successful customer flow, and the business decision. Store identifiers and payment evidence in the team's restricted incident record.

Use the [recovery validation checklist](../templates/recovery-validation.md) during the exercise and add the decision to the [drill report](../templates/dr-drill-report.md). For the surrounding procedure, see the [SteadyOps disaster recovery runbook](https://steadyops.best/articles/ha-dr-runbooks/).
