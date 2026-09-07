# ADR-0018 — Evidence-Gated Cross-Domain R&D Portfolio

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
UGAS V2 has accumulated many named Candidate Proprietary Technologies across M01–M28. Without a governed lifecycle, names can be mistaken for validated innovation, duplicates can proliferate, negative results can disappear, and engineering effort can be spent on ideas with weak differentiation or poor utility.

## Decision
UGAS V2 SHALL maintain a canonical Candidate Proprietary Technology Registry and SHALL treat every candidate as an R&D hypothesis until it passes evidence gates.

The canonical lifecycle SHALL support at least `CANDIDATE`, `TRIAGED`, `PRIOR_ART_RESEARCH`, `EXPERIMENT_DESIGNED`, `VALIDATING`, `VALIDATED`, `DUPLICATE`, `MERGED`, `REJECTED` and `DEFERRED`.

Promotion to VALIDATED requires predeclared baselines, metrics, thresholds/falsification criteria and reproducible evidence. Prior-art research SHALL record overlap and uncertainty; absence of found prior art SHALL NOT be represented as legal novelty, patentability or freedom-to-operate. Cross-domain compound candidates SHALL preserve provenance to their source primitives.

Portfolio prioritization SHALL be multi-objective and explainable rather than based on a single opaque score.

## Consequences
### Positive
- separates creative invention from technical validation;
- reduces duplicate/overlapping R&D;
- preserves negative evidence;
- encourages falsifiable experiments and ablations;
- enables cross-domain composition;
- creates a defensible internal technical record without unsupported legal claims.

### Costs
- research and benchmark overhead;
- registry maintenance;
- some attractive ideas will be rejected or deferred;
- prior-art work may require external specialist review before IP decisions.

## Rejected alternatives
### Treat named technologies as proprietary by default
Rejected because naming is not evidence of novelty, usefulness or defensibility.

### Validate only by subjective expert review
Rejected because major claims need falsifiable empirical evidence where testable.

### Single weighted innovation score
Rejected because it hides trade-offs and uncertainty; Pareto analysis plus rationale is required.

### Delete failed experiments
Rejected because negative evidence prevents repeated waste and improves future decisions.
