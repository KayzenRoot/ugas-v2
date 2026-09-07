# M29 — Cross-Domain Proprietary R&D

**Round:** 29  
**Scope class:** PROGRAM R&D / PLANNING NECESSITY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Convert the large set of UGAS V2 Candidate Proprietary Technologies into a governed, evidence-driven R&D portfolio. M29 does not assume novelty. It defines how candidates are inventoried, normalized, researched, compared, experimentally validated, combined, promoted, rejected or deferred.

## Core principles
1. A name is not evidence of novelty.
2. Prior-art research precedes novelty/defensibility claims.
3. Hypotheses must be falsifiable.
4. Validation requires baselines, metrics, thresholds and reproducible evidence.
5. Negative results are first-class evidence.
6. Overlap is recorded, not hidden.
7. Cross-domain combinations may create more value than isolated inventions.
8. Technical IP disposition is not legal advice.
9. Portfolio priority is multi-objective, not one opaque score.
10. Validated technology still does not automatically mean patentable.

## Candidate lifecycle
`CANDIDATE → TRIAGED → PRIOR_ART_RESEARCH → EXPERIMENT_DESIGNED → VALIDATING → VALIDATED`

Other states: `DUPLICATE`, `MERGED`, `REJECTED`, `DEFERRED`, `OPEN_TECHNIQUE`, `TRADE_SECRET_CANDIDATE`, `PATENT_REVIEW_CANDIDATE`.

## Technology record contract
Each record SHALL include stable ID, canonical name, aliases, originating modules, problem, proposed mechanism, hypothesis, nearest known approaches, prior-art sources/date, overlap classification, novelty uncertainty, impact, feasibility, cross-domain leverage, defensibility score (non-legal), validation cost, dependencies, experiment design, falsification criterion, ablations, security/rights implications, reproducibility requirements, lifecycle state and evidence references.

## Technology families
F01 Graph/planning/orchestration
F02 Hardware/compute intelligence
F03 Model intelligence/routing
F04 Multimodal IR/identity
F05 Generative media production
F06 Narrative/content/ads/brand/localization
F07 Quality/repair/economics
F08 Memory/RAG/context
F09 Provenance/rights/security
F10 Storage/cache/recovery
F11 Observability/operator intelligence
F12 Automation/agents
F13 Export/delivery/reproducibility

## Prior-art protocol
Search mechanism synonyms across academic literature, patents, standards, open-source systems, product documentation and credible technical publications. Classify overlap as `NONE_FOUND`, `ADJACENT`, `PARTIAL`, `SUBSTANTIAL`, or `ESSENTIALLY_KNOWN`. NONE_FOUND is not a legal novelty or freedom-to-operate conclusion.

## Experiment protocol
Every validation plan defines baseline(s), controlled variables, representative fixtures, metrics, minimum meaningful effect/non-inferiority bound, stochastic trials/seeds, hardware/model/provider versions, cost/time accounting, failure criteria, ablation plan and reproducibility bundle.

## Portfolio evaluation
Dimensions include Impact, Differentiation, Feasibility, Cross-Domain Leverage, Defensibility, Evidence Strength, Validation Cost and Risk. Portfolio ranking uses Pareto analysis and written rationale rather than a single magic score.

## Initial cross-domain compound hypotheses
### XDT-001 Universal Decision Evidence Fabric
Unifies decision-ledger patterns from compute/model/security/storage/automation/delivery under one typed evidence envelope.

### XDT-002 Production Digital Twin
Combines Production Graph, compute, model fitness, storage locality, quality history, cost and delivery constraints to simulate execution plans before expensive work.

### XDT-003 Cross-Modal Identity Continuity Mesh
Links Asset DNA, digital human, voice, canon, brand and localization invariants in one continuity graph.

### XDT-004 Evidence-Guided Adaptive Production Loop
Combines Model Director, Quality Court, Self-Correction, Render Cascade, memory and cost telemetry into a closed optimization loop.

### XDT-005 Trust-Preserving Memory Retrieval
Makes trust, rights and data classification hard dimensions of multimodal retrieval.

### XDT-006 Reproducible Creative Build System
Combines Production Graph invalidation, Cache Truth Key, content identity, IR/DNA fingerprints and release reproducibility into software-build-like reproducibility classes for media.

### XDT-007 Quality-Causal Repair Graph
Models defects as causal hypotheses linked to judges, lineage and minimal repair actions.

### XDT-008 Predictive Resource-to-Quality Planner
Jointly optimizes compute, model, fidelity stages, storage locality and cost for accepted-output yield.

### XDT-009 Policy-Carrying Artifact
Carries referenced rights/security/retention/destination policy consistently across lineage and derivatives.

### XDT-010 Autonomous Production Safety Kernel
Shared safety kernel for bounded agents using capabilities, budgets, quality gates, stop conditions, idempotency, delivery reconciliation and human control.

### XDT-011 Cross-Domain Drift Observatory
Correlates model, identity, brand, canon, storage, destination and telemetry drift.

### XDT-012 Creative Lineage Knowledge Graph
Unifies Production Graph, DNA, derivation, quality evidence, memory, provenance, rights and release history for traceability/reuse.

## Promotion gates
CANDIDATE→TRIAGED requires clear mechanism/problem.
TRIAGED→PRIOR_ART_RESEARCH requires plausible value.
PRIOR_ART_RESEARCH→EXPERIMENT_DESIGNED requires an explicit differentiated testable hypothesis after overlap review.
EXPERIMENT_DESIGNED→VALIDATING requires baseline/metrics/thresholds/fixtures/evidence plan.
VALIDATING→VALIDATED requires predeclared criteria met with reproducible evidence and no unresolved HIGH/CRITICAL defect.

## Rejection/defer rules
Reject when falsified, essentially known without useful differentiation, unsafe, architecturally harmful or economically irrational. Defer when useful but blocked by cost, dependencies or priorities.

## IP-disposition support
After technical validation, candidates may be flagged for later specialist review as open-source, internal know-how, trade-secret candidate, patent-review candidate, defensive-publication candidate or no-priority. M29 does not determine patentability or freedom-to-operate.

## Observability and governance
All R&D decisions should be auditable through M26-compatible evidence. M24 applies to restricted research inputs. M23 tracks provenance of research evidence where applicable. M25 stores datasets/results; M27 may automate experiments but cannot promote a technology without governed evidence.

## Acceptance criteria
1. One canonical technology registry exists.
2. Every candidate has a lifecycle state and evidence links.
3. Cross-module duplicates/aliases can be merged without losing provenance.
4. Prior-art protocol is explicit and non-legal in its conclusions.
5. Every validation candidate has falsifiable success criteria.
6. Baselines/ablations/reproducibility are mandatory for VALIDATED.
7. Negative results are retained.
8. Cross-domain compound technologies are represented separately from source primitives.
9. Portfolio priority is explainable and multi-objective.
10. No unsupported proprietary/novel/patentable claim is made.
11. No product implementation is introduced in this round.

## Out of scope
Patent filing, legal opinions, freedom-to-operate clearance, production implementation of candidates, guaranteed novelty, and public claims of proprietary status before evidence/review.