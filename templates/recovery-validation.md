# Recovery Validation Checklist

## Infrastructure
- [ ] Required network, storage, DNS, certificates, and hosts are healthy.
- [ ] Only the intended data path accepts writes.
- [ ] Monitoring, logging, backup, and archival jobs resumed.

## Data
- [ ] Recovered point is documented.
- [ ] Data loss is measured against RPO.
- [ ] Backup, WAL, snapshot, or archive integrity was checked.
- [ ] Consistency checks completed.
- [ ] Replica recovery is progressing.

## Application
- [ ] Health and readiness succeed.
- [ ] Error rate and p95/p99 latency returned to baseline.
- [ ] Authentication and dependencies work.
- [ ] Queues drain safely.
- [ ] Logs contain no repeated recovery failure.

## Business
- [ ] A real user can authenticate.
- [ ] The critical transaction completes.
- [ ] The business owner accepts the recovered point.
- [ ] Customer impact is falling.

## Evidence
- [ ] Commands and outputs are timestamped.
- [ ] Detection, decision, recovery, and validation times are recorded.
- [ ] RPO/RTO results are recorded.
- [ ] Remaining risks have owners and deadlines.
- [ ] The next drill is scheduled.
