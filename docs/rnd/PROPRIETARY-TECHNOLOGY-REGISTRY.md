# UGAS V2 — Candidate Proprietary Technology Registry

**Status:** GOVERNED R&D REGISTRY  
**Rule:** a named idea is not automatically novel, proprietary, patentable or defensible.

## Purpose
Provide one canonical source for Candidate Proprietary Technologies across UGAS V2 so ideas can be normalized, deduplicated, researched, benchmarked, combined, promoted, rejected or deferred without relying on chat memory.

## Lifecycle
`CANDIDATE → TRIAGED → PRIOR_ART_RESEARCH → EXPERIMENT_DESIGNED → VALIDATING → VALIDATED`

Alternative states: `DUPLICATE`, `MERGED`, `REJECTED`, `DEFERRED`, `OPEN_TECHNIQUE`, `TRADE_SECRET_CANDIDATE`, `PATENT_REVIEW_CANDIDATE`.

## Required fields
Technology ID; canonical name; aliases; source module(s); problem; mechanism; hypothesis; nearest known approaches; prior-art sources/date; overlap class; novelty uncertainty; impact; feasibility; cross-domain leverage; defensibility (non-legal); validation cost; experiment; falsification criterion; ablations; dependencies; security/rights notes; reproducibility requirements; lifecycle state; evidence references.

## Overlap classes
`NONE_FOUND`, `ADJACENT`, `PARTIAL`, `SUBSTANTIAL`, `ESSENTIALLY_KNOWN`.

NONE_FOUND means only that the performed search did not identify substantial overlap. It is not a patentability or freedom-to-operate conclusion.

## Families
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

## Initial cross-domain candidates
| ID | Name | State | Source families |
|---|---|---|---|
| XDT-001 | Universal Decision Evidence Fabric | CANDIDATE | F01/F09/F10/F11/F12/F13 |
| XDT-002 | Production Digital Twin | CANDIDATE | F01/F02/F03/F07/F10/F13 |
| XDT-003 | Cross-Modal Identity Continuity Mesh | CANDIDATE | F04/F05/F06 |
| XDT-004 | Evidence-Guided Adaptive Production Loop | CANDIDATE | F03/F07/F08/F11 |
| XDT-005 | Trust-Preserving Memory Retrieval | CANDIDATE | F08/F09/F10 |
| XDT-006 | Reproducible Creative Build System | CANDIDATE | F01/F04/F10/F13 |
| XDT-007 | Quality-Causal Repair Graph | CANDIDATE | F01/F07/F11 |
| XDT-008 | Predictive Resource-to-Quality Planner | CANDIDATE | F02/F03/F07/F10 |
| XDT-009 | Policy-Carrying Artifact | CANDIDATE | F04/F09/F10/F13 |
| XDT-010 | Autonomous Production Safety Kernel | CANDIDATE | F01/F07/F09/F11/F12/F13 |
| XDT-011 | Cross-Domain Drift Observatory | CANDIDATE | F03/F04/F06/F10/F11/F13 |
| XDT-012 | Creative Lineage Knowledge Graph | CANDIDATE | F01/F04/F07/F08/F09/F13 |

## Scoring dimensions
Impact; Differentiation; Feasibility; Cross-Domain Leverage; Defensibility; Evidence Strength; Validation Cost; Risk.

Do not collapse the portfolio into a single opaque score. Use Pareto analysis plus written rationale.

## Prior-art protocol
1. Define mechanism narrowly.
2. Expand technical synonyms beyond UGAS names.
3. Search academic literature, patents, standards, open-source systems, product documentation and credible technical publications.
4. Record source/date and overlapping mechanism.
5. Classify overlap.
6. Update/reduce the hypothesis when overlap exists.
7. Never translate NONE_FOUND into a legal novelty claim.
8. Require specialist legal review before filing/clearance decisions.

## Experiment protocol
Every validation plan specifies baselines, controlled variables, representative fixtures, metrics, minimum meaningful effect/non-inferiority bound, stochastic trial/seeds where relevant, hardware/model/provider versions, cost/time accounting, failure criteria, ablations and reproducibility evidence.

## Promotion gates
CANDIDATE→TRIAGED: clear mechanism/problem.  
TRIAGED→PRIOR_ART_RESEARCH: plausible impact/feasibility.  
PRIOR_ART_RESEARCH→EXPERIMENT_DESIGNED: differentiated falsifiable hypothesis remains.  
EXPERIMENT_DESIGNED→VALIDATING: baselines/metrics/thresholds/fixtures/evidence plan ready.  
VALIDATING→VALIDATED: predeclared criteria met with reproducible evidence and no unresolved HIGH/CRITICAL defect.

## IP disposition support
After technical validation only: open-source, internal know-how, trade-secret candidate, patent-review candidate, defensive-publication candidate or no-priority. This registry provides technical decision support, not legal advice.
