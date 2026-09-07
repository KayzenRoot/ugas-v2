# Source Hierarchy

## Order of authority
1. `docs/checkpoint/CURRENT.md`
2. accepted ADRs + `docs/decisions/DECISIONS-LEDGER.md`
3. `docs/SCOPE.md`
4. `docs/DEFINITION-OF-DONE.md`
5. `docs/ARCHITECTURE.md`
6. `docs/REQUIREMENTS.md`
7. module specifications
8. supporting contracts/plans
9. backlog/issues
10. external notes/chat memory

Git history, code, tests, CI, runtime telemetry, benchmarks and reviewed Evidence Bundles prevail for implementation facts.

A change to Checkpoint, Scope, DoD, Architecture or an accepted decision invalidates stale Work Orders and requires a new Context Lock.

Ideas become canonical only after being committed and reviewed.

## Canonical directories
- `docs/checkpoint/` current state/handoff
- `docs/decisions/` ledger
- `docs/adr/` architectural decisions
- `docs/modules/` module specifications
- `docs/contracts/` data/API/integration contracts
- `docs/planning/` backlog/work orders
- `docs/evidence/` reviewed evidence
