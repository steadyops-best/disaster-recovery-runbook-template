# Contributing

Contributions should make a disaster-recovery procedure more executable, safer under pressure, or easier to validate and audit.

## Good contributions

- Add a missing recovery precondition or stop condition.
- Clarify ownership, escalation, decision authority, or communication responsibility.
- Improve dependency and restart ordering.
- Add validation for infrastructure, data, application, or business recovery.
- Improve evidence fields for RPO, RTO, recovered point, elapsed time, and follow-up work.
- Correct terminology or commands and link to primary documentation.
- Add a failure mode that materially changes restore, failover, fencing, or routing behavior.

## Avoid

- Real credentials, private hostnames, customer data, backup locations, or sensitive topology.
- Destructive commands without explicit warnings, expected results, and stop conditions.
- Example RPO/RTO values presented as universal targets.
- Declaring recovery complete from process health alone.
- Vendor marketing, copied policy text, or unrelated SEO links.
- Procedures that assume a backup is usable without an isolated restore test.

## Change format

A useful change should state:

1. the recovery gap or failure mode;
2. when the change applies;
3. the proposed procedure or template field;
4. the expected result;
5. the stop condition;
6. how technical and business recovery are validated;
7. what evidence should be retained.

Use safe placeholders. Keep environment-specific commands in private derived runbooks rather than in this public template.

## Source and canonical guide

The reusable package lives in this repository. The maintained explanatory guide is:

https://steadyops.best/articles/ha-dr-runbooks/

Material changes to the recovery operating model should keep the repository and canonical guide consistent.