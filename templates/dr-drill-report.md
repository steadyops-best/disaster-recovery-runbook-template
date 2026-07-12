# Disaster Recovery Drill Report

Version: 1.0.0  
Canonical guide: https://steadyops.best/articles/ha-dr-runbooks/

Complete this report after a restore, failover, or full disaster-recovery exercise. Store the completed copy with the runbook and evidence.

## Drill control

- Service/system:
- Environment:
- Drill date:
- Scenario:
- Exercise type: tabletop / isolated restore / failover / full recovery
- Incident commander:
- Recovery operator:
- Business validator:
- Communications owner:
- Observers:
- Evidence location:

## Recovery contract

- Customer/business impact represented by the scenario:
- RPO target:
- RTO target:
- Critical business transaction:
- Recovery source:
- Target recovery point:
- Expected recovery path:
- Approved fallback:
- Stop conditions:

## Preconditions

- [ ] Recovery source identity and freshness were verified.
- [ ] Credentials and break-glass access were available.
- [ ] Isolated target environment was ready.
- [ ] Required DNS, routing, storage, and network access were available.
- [ ] Monitoring and logging were available for the exercise.
- [ ] Production data and secrets were handled according to policy.
- [ ] Participants understood decision authority and stop conditions.

## Timeline

| UTC time | Owner | Event or action | Expected result | Actual result | Evidence |
|---|---|---|---|---|---|
| | | Drill started | | | |
| | | Recovery source verified | | | |
| | | Restore or promotion started | | | |
| | | Routing updated | | | |
| | | Technical validation passed | | | |
| | | Business validation passed | | | |
| | | Drill closed | | | |

## Recovered state

- Recovered timestamp/LSN/version:
- Measured data loss:
- Data consistency result:
- Only intended primary accepted writes: yes/no/not applicable
- Replication or replica rebuild status:
- Backup/archive jobs resumed:
- Monitoring and alert delivery resumed:

## Validation results

| Area | Check | Result | Evidence | Owner |
|---|---|---|---|---|
| Infrastructure | Network, DNS, TLS, storage, routing | | | |
| Data | Recovered point and consistency | | | |
| Application | Health, readiness, dependencies | | | |
| Queues/workers | Backlog and processing safety | | | |
| Business | Critical transaction | | | |
| Operations | Monitoring, logs, backups, archive | | | |

## Objectives

- Recovery start time:
- Technical recovery time:
- Business validation time:
- Total elapsed recovery time:
- RPO met: yes/no
- RTO met: yes/no
- Difference from target:

## What worked

- 

## Gaps and unexpected behavior

- 

## Decision review

- Were stop conditions clear?
- Was authority to fail over or restore clear?
- Did the runbook contain exact commands and expected results?
- Did dependency order match reality?
- Could a second engineer follow the procedure safely?
- Did technical health and business validation agree?

## Follow-up actions

| Action | Risk | Priority | Owner | Deadline | Verification |
|---|---|---|---|---|---|
| | | | | | |

## Runbook maintenance

- Runbook sections to update:
- Architecture/dependency records to update:
- Monitoring or alert changes:
- Access or credential changes:
- Automation opportunities:
- Next drill date:

## Approval

- Technical reviewer:
- Business reviewer:
- Review date:
- Final readiness status: