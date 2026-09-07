# Repository Governance

## Objective
Keep `main` as a reviewable canonical record suitable for long-running development across chats, executors and reviewers.

## Governed path
Issue/EPIC → Work Order → Context Lock → branch → changes → tests/evidence → PR → audit → verdict → checkpoint delta → merge.

## Main
Direct product changes to `main` are prohibited by project policy even when GitHub settings do not technically block them.

## Preferred merge
Squash for normal Work Orders to keep one logical increment per merge. Preserve merge commits only when history semantics require them.

## Required PR evidence
Base/head; scope; requirement IDs; ADRs; tests; build/static checks; security/rights when applicable; migration/recovery; benchmarks; risks; checkpoint delta.

## Source integrity CI
`.github/workflows/source-pack-integrity.yml` checks that minimum canonical files remain present and that the 23 initial module specifications and ADR baseline are not accidentally removed.

## Administrative controls
Tracked in Issue #26 because the connected GitHub integration cannot write repository-admin settings:
- branch protection;
- required PR/review/status checks;
- label taxonomy;
- milestones;
- merged-branch deletion policy.

## Label taxonomy target
When administrative write becomes available:
- type: feature, bug, docs, r&d, governance
- scope: necessary, important, future
- risk: low, standard, elevated, high-assurance
- verdict: correction-required, blocked
- module: m01..m23
- priority: p0..p3

## Release discipline
No V2 release until release scope is frozen, DoD is satisfied, final audit APPROVED and the release checkpoint is merged.
