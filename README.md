# Disaster Recovery Runbook Template

A practical disaster recovery runbook template for DevOps, SRE, platform and engineering teams that need clear recovery steps before a production incident happens.

The goal is not to create a beautiful document. The goal is to make recovery repeatable when people are under pressure.

## What this runbook helps clarify

- who owns the incident
- which systems are affected
- what RTO and RPO apply
- which recovery path is allowed
- how to validate service recovery
- how to communicate status
- what evidence and follow-up tasks should be saved

## When to use it

Use this template for:

- database outage
- failed deployment
- server, region or cluster failure
- backup restore event
- DNS, TLS or load balancer incident
- storage or filesystem issue
- Kubernetes control plane or workload failure
- PostgreSQL failover or restore
- customer-impacting service degradation

## Recovery terms

| Term | Meaning | Example |
| --- | --- | --- |
| RTO | Recovery Time Objective: how fast service must be restored | 30 minutes |
| RPO | Recovery Point Objective: how much data loss is acceptable | 5 minutes |
| MTTR | Mean Time To Recovery: how long recovery usually takes | 20 minutes |
| SLO | Service objective for users or internal teams | 99.9% availability |

## Copyable runbook template

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
| --- | --- | --- | --- | --- |
| Application | Main service |  | Unknown |  |
| Database | PostgreSQL / MySQL / etc. |  | Unknown |  |
| Load balancer | Nginx / HAProxy / cloud LB |  | Unknown |  |
| DNS | Public routing |  | Unknown |  |
| Monitoring | Prometheus / Grafana / etc. |  | Unknown |  |
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

- [ ] Confirm alert source.
- [ ] Confirm customer impact.
- [ ] Check application health endpoint.
- [ ] Check error rate.
- [ ] Check p95/p99 latency.
- [ ] Check database availability.
- [ ] Check queue depth and background jobs.
- [ ] Check disk space.
- [ ] Check CPU and memory pressure.
- [ ] Check network, DNS and TLS.
- [ ] Check recent deployments.
- [ ] Check recent infrastructure changes.

## 5. Decision tree

If the latest deployment caused the incident:

- pause the rollout
- roll back the application
- validate health checks
- monitor error rate and latency
- document the bad release

If the database is unavailable:

- confirm primary and replica status
- check disk, CPU, memory and connection pressure
- decide between failover and restore
- validate application connectivity
- confirm data consistency

If DNS or load balancing failed:

- check DNS records
- check Nginx, HAProxy or ingress config
- validate upstream health
- test from an external network
- confirm TLS certificate status

If data corruption is suspected:

- stop writes if necessary
- preserve evidence
- identify last known good backup
- restore to an isolated environment first
- validate data before production restore

## 6. Recovery steps

### Step 1: Stabilize

Owner:
Commands / actions:

```bash
# Add commands here
```

Expected result:
Validation:

### Step 2: Restore service

Owner:
Commands / actions:

```bash
# Add commands here
```

Expected result:
Validation:

### Step 3: Validate recovery

- [ ] Service returns HTTP 200.
- [ ] Error rate is back to baseline.
- [ ] p99 latency is acceptable.
- [ ] Database connections are stable.
- [ ] Queue depth is decreasing.
- [ ] Background jobs are processing.
- [ ] Customer-facing flows work.
- [ ] Monitoring dashboards are normal.

### Step 4: Communicate status

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

- [ ] Incident timeline completed.
- [ ] Root cause documented.
- [ ] Customer impact documented.
- [ ] Recovery time measured.
- [ ] Data loss confirmed or ruled out.
- [ ] Monitoring gaps documented.
- [ ] Runbook gaps documented.
- [ ] Follow-up tasks created.
- [ ] Logs and evidence preserved where useful.
- [ ] Customer or internal summary sent.

## 10. Post-incident review

What happened?
Why did it happen?
What worked well?
What failed?
What should be automated?
What should be monitored?
What should be tested regularly?

| Action | Owner | Priority | Due date |
| --- | --- | --- | --- |
|  |  |  |  |
````

## Production readiness checks

Before relying on this runbook, validate:

- [ ] Backups exist.
- [ ] Backups are restorable.
- [ ] Restore was tested recently.
- [ ] Recovery owners are known.
- [ ] Credentials are available securely.
- [ ] Monitoring covers the affected systems.
- [ ] DNS and load balancer changes are documented.
- [ ] Rollback commands are tested.
- [ ] Customer communication path is defined.
- [ ] RTO and RPO are agreed with the business.

## Common mistakes

- Having backups but never testing restore.
- Documenting recovery steps that only one engineer understands.
- Mixing rollback and disaster recovery decisions.
- Restoring directly to production without isolated validation.
- Forgetting DNS, TLS, queues and background workers.
- Declaring recovery before customer-facing flows are tested.
- Not preserving useful logs after the incident.
- Not updating the runbook after a real failure.

## SteadyOps resources

- Website: https://steadyops.best/
- DevOps/SRE articles: https://steadyops.best/articles/
- LinkedIn: https://www.linkedin.com/in/yuri-osipov-0876b0254
- Related article: https://steadyops.best/articles/ha-dr-runbooks/
- PostgreSQL HA review: https://steadyops.best/postgresql-ha-review/
- SteadyOps platform case study: https://steadyops.best/steadyops-platform-case-study/

## Related public checklists

- Zero-downtime deployment checklist: https://github.com/steadyops-best/zero-downtime-deployment-checklist
- Kubernetes rollback checklist: https://github.com/steadyops-best/kubernetes-rollback-checklist

## License

MIT License. Use, adapt and improve this template for your own production environment.
