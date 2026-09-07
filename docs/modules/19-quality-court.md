# M19 — Quality Court

**Round:** 19  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Make acceptance an evidence-based decision using specialized judges, calibrated confidence and human-review escape hatches.

## Responsibilities
- judge registry
- modality/constraint-specific evaluation
- score/confidence/verdict
- court aggregation
- defect localization
- human review
- quality regression

## Planned capabilities
- Identity/Anatomy/Composition/Temporal/LipSync/Voice/Audio/Music/3D/Brand/Narrative/Policy/Provenance/Artifact judges
- threshold profiles
- evidence retention
- judge disagreement
- quality regression comparisons
- human override with rationale

## Candidate proprietary technologies
- **Quality Court** — multi-judge evaluation framework
- **Quality Evidence Bundle** — evidence attached to acceptance
- **Defect Localization Engine** — locates failed region/segment/constraint
- **Partial Repair Planner** — turns defect into bounded correction scope
- **Confidence Arbitration** — handles judge disagreement
- **Quality Regression Memory** — detects historical degradation

## Inputs
- generated artifact
- DNA/IR/canon/brand/rights constraints
- judge profile/version
- reference/gold data

## Outputs
- per-judge evaluations
- aggregate verdict
- confidence
- defect set/location
- repair recommendation
- human-review request

## How it works
1. Select judges required by artifact modality and governing constraints.
2. Each judge evaluates against explicit criteria/version and emits score, confidence, verdict and evidence.
3. Court aggregates with policy-defined hard gates and weighted/advisory signals.
4. Disagreement or low confidence may require human review rather than false certainty.
5. Rejected outputs send defect locations and reasons to Repair.
6. Accepted decisions reference the exact Court profile and evidence.

## Canonical data / contracts
- JudgeDefinition
- Evaluation
- CourtProfile
- CourtDecision
- Defect
- HumanReview

## Dependencies
- all creative modules
- M20 Repair
- M22 Memory
- M23 Provenance

## Failure modes and safeguards
- judge unavailable → policy determines block/degraded review
- uncalibrated confidence → cannot act as hard gate
- judge disagreement → arbitration/human review
- systematic false accept → regression incident

## Observability
- false accept/reject on gold sets
- judge disagreement
- acceptance rate
- confidence calibration
- quality regression

## Security / rights
- policy/rights judges cannot be bypassed by creative model output
- human override is audited

## Tests and benchmarks
- gold labeled datasets
- calibration curves
- hard-gate tests
- disagreement fixtures
- version regression

## Acceptance criteria for first usable V2 path
- [ ] artifact cannot become accepted without configured court decision
- [ ] rejection includes actionable reason/evidence
- [ ] judge version and criteria are reproducible

## Deliberately out of this module
- claiming subjective artistic truth
- replacing required legal/human review

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
