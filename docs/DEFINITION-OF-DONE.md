# Definition of Done — UGAS V2

UGAS V2 is complete only when all required gates are objectively satisfied.

## Canon
Current Source Hierarchy; frozen release scope; mapped requirements; ADRs match implementation; checkpoint matches main.

## Functional
All NECESSARY modules have usable E2E paths. Production Graph proves dependency invalidation, execution, quality gating, repair lineage and delivery. Provider-independent intent is demonstrated. Dashboard exposes principal workflows.

## Quality
Each modality has quality gates and representative benchmark fixtures. Regression thresholds exist. No known HIGH/CRITICAL defect is open.

## Reliability
Retry/cancel/recovery tested; canonical state survives expected worker/provider failures; backup/restore or equivalent recovery validated.

## Security/Rights
Threat model current; secrets validated; privileged/destructive actions bounded; consent/rights/provenance tested; no HIGH/CRITICAL security defect.

## Performance/economics
Representative hardware benchmarks; memory/OOM characterized; cost/time metrics; repair/render cascade benefit measured where used.

## Engineering
Lint/type/build/tests pass; migrations validated; deployment current; contracts versioned; release artifacts traceable.

## Documentation
Module docs, APIs/data model, deployment/recovery and known limitations match reality.

## Release
Independent final audit APPROVED; release tag/changelog; rollback/roll-forward; final checkpoint merged.
