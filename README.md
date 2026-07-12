# Disaster Recovery Runbook Template

A reusable disaster-recovery package for engineering teams that need an executable recovery path, named ownership, measurable RPO/RTO, technical and business validation, and retained drill evidence.

- Canonical implementation guide: https://steadyops.best/articles/ha-dr-runbooks/
- PostgreSQL HA review: https://steadyops.best/postgresql-ha-review/
- SteadyOps resource library: https://steadyops.best/resources/
- License: MIT
- Artifact version: 1.0.0
- Repository reviewed: 2026-07-12

## Why this repository exists

A backup-success message is not recovery evidence. A production recovery process also needs:

- an agreed service scope and business impact;
- explicit RPO and RTO;
- an incident commander, recovery operator, business validator, and communications owner;
- a verified recovery source;
- stop conditions that prevent destructive improvisation;
- dependency and restart order;
- exact actions with expected and actual results;
- technical health plus a critical business transaction;
- a timestamped timeline, measured outcome, and owned follow-up work.

The repository keeps the reusable operational files separate from the longer explanatory guide so teams can fork the templates, adapt them to their own topology, and retain versioned recovery evidence.

## Start here

1. Copy [`templates/runbook-template.md`](templates/runbook-template.md) into the repository that owns the service or infrastructure.
2. Complete the recovery contract, owners, dependencies, stop conditions, and evidence location before an incident.
3. Replace placeholders with environment-specific commands and expected outputs.
4. Run the procedure in a clean, isolated, production-like environment.
5. Validate recovery with [`templates/recovery-validation.md`](templates/recovery-validation.md).
6. Record the exercise in [`templates/incident-timeline.md`](templates/incident-timeline.md).
7. Score readiness with [`templates/dr-readiness-scorecard.md`](templates/dr-readiness-scorecard.md) and convert every gap into an owned action.

## Repository contents

| File | Purpose |
|---|---|
| [`templates/runbook-template.md`](templates/runbook-template.md) | Recovery contract, trigger, stop conditions, dependency order, procedure, and final evidence. |
| [`templates/recovery-validation.md`](templates/recovery-validation.md) | Infrastructure, data, application, business, and evidence checks after restore or failover. |
| [`templates/incident-timeline.md`](templates/incident-timeline.md) | Detection, decision, recovery, communication, and validation timeline. |
| [`templates/dr-readiness-scorecard.md`](templates/dr-readiness-scorecard.md) | Maturity score from unknown assumptions to proven recovery controls. |
| [`CITATION.cff`](CITATION.cff) | Citation metadata for derived runbooks and internal standards. |
| [`LICENSE`](LICENSE) | MIT license for reuse and adaptation. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Rules for safe and practical improvements. |

## Recovery operating model

### 1. Define the recovery contract

Document the customer or business impact, severity, RPO, RTO, authority to fail over or restore, and the evidence required to declare recovery complete.

### 2. Verify the source before changing production

Confirm backup age, snapshot identity, WAL or archive continuity, integrity evidence, credentials, storage, and the target recovery point. Stop when the source cannot be proven.

### 3. Recover dependencies in a controlled order

Identity, secrets, network, primary data, queues, object storage, APIs, workers, routing, and business flows often have different recovery dependencies. Document the order instead of discovering it during an outage.

### 4. Validate beyond infrastructure health

A healthy VM, pod, process, or database connection does not prove that the service is usable. Validate authentication and the critical customer transaction, then confirm that the recovered point is acceptable to the business owner.

### 5. Retain evidence and schedule the next drill

Store commands, outputs, recovered timestamp, measured data loss, elapsed time, communications, unresolved risks, owners, deadlines, and the next exercise date.

## Minimum drill evidence

- scenario and initiating failure;
- participants and decision owners;
- source backup, snapshot, replica, or archive identifiers;
- target and actual recovered point;
- start, decision, technical recovery, and business validation times;
- measured RPO and RTO result;
- commands and outputs;
- routing and write-safety state;
- technical checks and customer transaction result;
- gaps, owners, deadlines, and next drill date.

## Safety boundaries

These templates are not a substitute for an environment-specific recovery design.

- Do not restore directly over the only usable production copy without isolated validation.
- Stop when the recovery source, target point, write authority, or primary identity is unclear.
- Preserve logs and incident evidence before destructive cleanup.
- Verify fencing and routing so more than one writable primary cannot exist.
- Protect credentials, customer data, private hostnames, and topology when publishing derived files.
- Use RPO/RTO agreed with the business, not copied example values.
- Test the current procedure after material architecture, database, identity, storage, or routing changes.

## Related SteadyOps resources

- Kubernetes rollback checklist: https://github.com/steadyops-best/kubernetes-rollback-checklist
- Zero-downtime deployment checklist: https://github.com/steadyops-best/zero-downtime-deployment-checklist
- PostgreSQL production and failover guide: https://steadyops.best/articles/postgresql-at-scale/
- Production reliability cases: https://steadyops.best/reliability-cases/
- SteadyOps platform case study: https://steadyops.best/steadyops-platform-case-study/

## Citation

GitHub can render citation metadata from [`CITATION.cff`](CITATION.cff). Retain the source repository and canonical implementation guide when adapting these templates into an internal standard or customer-specific runbook.

## Contributing

Corrections and practical additions are welcome when they make ownership, stop conditions, execution, validation, or evidence clearer. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT. Use, adapt, and improve the templates for your own environment. The team executing a recovery remains responsible for testing, approvals, data safety, and production impact.