# Disaster Recovery Runbook Template

A practical disaster recovery runbook template for DevOps, SRE, platform and engineering teams that need clear recovery steps before production incidents happen.

Created by **SteadyOps**:
https://steadyops.best/

Related SteadyOps article:
https://steadyops.best/articles/ha-dr-runbooks/

## Why this exists

Disaster recovery often fails not because teams lack backups, but because nobody has tested the full recovery path under pressure.

This template helps teams document:

* who owns the incident
* what systems are affected
* what recovery objective applies
* what steps must be executed
* how to validate recovery
* how to communicate status
* what evidence should be saved after the incident

The goal is not to create a beautiful document. The goal is to make recovery repeatable.

## When to use this runbook

Use this template when preparing for or responding to:

* database outage
* failed deployment
* region or server failure
* backup restore event
* DNS or load balancer incident
* storage or filesystem issue
* Kubernetes cluster failure
* PostgreSQL failover or restore
* security-related production incident
* customer-impacting service degradation

## Recovery objectives

Before an incident, define the business expectations.

| Term    | Meaning                                                     | Example      |
| ------- | ----------------------------------------------------------- | ------------ |
| RTO     | Recovery Time Objective — how fast service must be restored | 30 minutes   |
| RPO     | Recovery Point Objective — how much data loss is acceptable | 5 minutes    |
| MTTR    | Mean Time To Recovery — how long recovery usually takes     | 20 minutes   |
| SLA/SLO | Service expectation for customers or internal teams         | 99.9% uptime |

## Runbook template

Copy this section into your internal documentation system.

````md
# Disaster Recovery Runbook

## 1. Incident summary

Incident name:

Start time:

Detected by:

Current status:

Affected services:

Customer impact:

Business impact:

Severity:

Incident commander:

Technical owner:

Communication owner:

## 2. Systems involved

| System | Role | Owner | Status | Notes |
|---|---|---|---|---|
| Application | Main service |  | Unknown |  |
| Database | PostgreSQL / MySQL / etc. |  | Unknown |  |
| Load balancer | nginx / HAProxy / cloud LB |  | Unknown |  |
| DNS | Public routing |  | Unknown |  |
| Monitoring | Prometheus / Grafana / Zabbix / etc. |  | Unknown |  |
| CI/CD | GitHub Actions / GitLab CI / etc. |  | Unknown |  |

## 3. Recovery objectives

RTO:

RPO:

Maximum acceptable customer impact:

Data loss tolerance:

Rollback allowed: yes/no

Restore from backup allowed: yes/no

Failover allowed: yes/no

## 4. Detection checklist

- [ ] Confirm alert source
- [ ] Confirm customer impact
- [ ] Check application health endpoint
- [ ] Check error rate
- [ ] Check p95/p99 latency
- [ ] Check database availability
- [ ] Check queue depth / background jobs
- [ ] Check disk space
- [ ] Check CPU and memory pressure
- [ ] Check network / DNS / TLS
- [ ] Check recent deployments
- [ ] Check recent infrastructure changes

## 5. Decision tree

If the latest deployment caused the incident:

- pause the rollout
- roll back the application
- validate health checks
- monitor error rate and latency
- document the bad release

If the database is unavailable:

- confirm primary/replica status
- check disk, CPU, memory and connections
- decide between failover and restore
- validate application connectivity
- confirm data consistency

If DNS or load balancing failed:

- check DNS records
- check nginx / HAProxy / ingress config
- validate upstream health
- test from external network
- confirm TLS certificate status

If data corruption is suspected:

- stop writes if necessary
- preserve evidence
- identify last known good backup
- restore to isolated environment first
- validate data before production restore

## 6. Recovery steps

### Step 1 — Stabilize

Owner:

Commands / actions:

```bash
# Add commands here
````

Expected result:

Validation:

### Step 2 — Restore service

Owner:

Commands / actions:

```bash
# Add commands here
```

Expected result:

Validation:

### Step 3 — Validate recovery

Owner:

Checks:

* [ ] Service returns HTTP 200
* [ ] Error rate is back to baseline
* [ ] p99 latency is acceptable
* [ ] Database connections are stable
* [ ] Queue depth is decreasing
* [ ] Background jobs are processing
* [ ] Customer-facing flows work
* [ ] Monitoring dashboards are normal

### Step 4 — Communicate status

Internal update:

Customer update:

Next update time:

Owner:

## 7. Rollback plan

Rollback target:

Previous version:

Rollback command:

```bash
# Example:
# kubectl rollout undo deployment/my-service
```

Validation:

Rollback risks:

Rollback owner:

## 8. Backup restore plan

Backup source:

Backup timestamp:

Restore target:

Restore command:

```bash
# Add restore command here
```

Validation query:

```sql
-- Add validation SQL here
```

Data consistency checks:

Restore owner:

## 9. Post-recovery checklist

* [ ] Incident timeline completed
* [ ] Root cause documented
* [ ] Customer impact documented
* [ ] Recovery time measured
* [ ] Data loss confirmed or ruled out
* [ ] Monitoring gaps documented
* [ ] Runbook gaps documented
* [ ] Follow-up tasks created
* [ ] Security evidence preserved if needed
* [ ] Customer/internal summary sent

## 10. Post-incident review

What happened?

Why did it happen?

What worked well?

What failed?

What should be automated?

What should be monitored?

What should be tested regularly?

Action items:

| Action | Owner | Priority | Due date |
| ------ | ----- | -------- | -------- |
|        |       |          |          |

```

## Production checklist

Before relying on this runbook, validate:

- [ ] backups exist
- [ ] backups are restorable
- [ ] restore was tested recently
- [ ] recovery owners are known
- [ ] credentials are available securely
- [ ] monitoring covers the affected systems
- [ ] DNS and load balancer changes are documented
- [ ] rollback commands are tested
- [ ] customer communication path is defined
- [ ] RTO and RPO are agreed with the business

## Common mistakes

- Having backups but never testing restore
- Documenting recovery steps that only one engineer understands
- Mixing rollback and disaster recovery decisions
- Restoring directly to production without isolated validation
- Forgetting DNS, TLS, queues and background workers
- Declaring recovery before customer-facing flows are tested
- Not preserving logs and evidence after the incident
- Not updating the runbook after a real failure

## Related SteadyOps resources

- DevOps/SRE articles: https://steadyops.best/articles/
- HA & DR Runbooks: https://steadyops.best/articles/ha-dr-runbooks/
- SteadyOps Platform Story: https://steadyops.best/steadyops-platform-case-study/

## About SteadyOps

SteadyOps provides senior DevOps/SRE support for teams that need reliable production systems, safer deployments, monitoring, incident response and recovery runbooks.

Website: https://steadyops.best/

## License

MIT License. Use, adapt and improve this template for your own production environment.
```
