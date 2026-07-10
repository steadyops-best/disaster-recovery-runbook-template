# Disaster Recovery Runbook

Version: 1.0.0
Last reviewed: 2026-07-10

Implementation guide: https://steadyops.best/articles/ha-dr-runbooks/

## Document control

- Service:
- Environment:
- Owner:
- Last reviewed:
- Last drill:
- Next drill:
- Evidence location:

## Recovery contract

- Business impact:
- Severity:
- RPO:
- RTO:
- Incident commander:
- Recovery operator:
- Business validator:
- Communications owner:

## Trigger

Describe the measurable condition that activates this runbook.

## Stop conditions

- Recovery source cannot be verified.
- Replica lag or backup age exceeds RPO.
- Target recovery point is unclear.
- More than one writable primary may exist.
- Credentials, routing, DNS, or storage are unavailable.
- A destructive step would remove incident evidence.

## Dependencies and recovery order

1. Identity, secrets, and network access.
2. Primary data store.
3. Queues and object storage.
4. APIs in controlled mode.
5. Workers after data consistency is confirmed.
6. Technical validation.
7. Critical business transaction.
8. Normal traffic and background processing.

## Recovery source

- Source type:
- Backup or snapshot identifier:
- Base-backup timestamp:
- WAL or archive range:
- Integrity evidence:
- Credential owner:

## Recovery procedure

For every step record owner, timestamp, command or action, expected result, actual result, stop condition, and evidence.

### Step 1 — isolate unsafe writes

### Step 2 — verify recovery source

### Step 3 — restore or promote

### Step 4 — update routing

### Step 5 — reconnect dependencies

### Step 6 — validate technical health

### Step 7 — validate the business transaction

### Step 8 — resume traffic and background processing

## Final evidence

- Recovered point:
- Measured data loss:
- Recovery start:
- Technical recovery:
- Business validation:
- Total recovery time:
- RPO met:
- RTO met:
- Remaining risks:
- Follow-up owners and deadlines:
