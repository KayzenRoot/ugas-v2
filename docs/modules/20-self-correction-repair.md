# M20 — Self-Correction & Repair

**Round:** 20  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Convert quality failures into the smallest safe corrective action, preserving good work and complete lineage.

## Responsibilities
- defect interpretation
- minimal repair scope
- selective regeneration
- retry/provider/model/parameter strategy
- local image/video/audio/text repairs
- revalidation
- failure learning

## Planned capabilities
- region/frame/line/layer/node repair
- retry policies
- alternate model/provider
- constraint reinforcement
- parameter mutation
- impact preview
- cost estimate
- full regeneration only as fallback

## Candidate proprietary technologies
- **Minimal Regeneration Engine** — minimizes affected production area
- **Failure Fingerprint Library** — maps recurring defects
- **Regeneration Strategy Learner** — learns effective repairs
- **Repair Cost Estimator** — predicts time/compute/cost
- **Error-to-Action Compiler** — turns diagnosis into executable corrective plan

## Inputs
- Quality Court rejection
- defect location/type
- parent artifact/graph context
- available models/providers
- budgets

## Outputs
- RepairPlan
- affected node/region set
- new execution plan
- derivative artifact
- revalidation evidence

## How it works
1. Normalize Quality Court failures into typed defects and confidence.
2. Match defects to known failure fingerprints and candidate strategies.
3. Compute dependency/region impact and compare minimal repair versus bounded/full regeneration.
4. Estimate quality likelihood, time and cost for alternatives.
5. Execute selected repair as derivative node/attempt preserving parent artifact.
6. Re-run only relevant quality gates plus mandatory regression gates.
7. Record outcome to update failure/strategy evidence.

## Canonical data / contracts
- Defect
- FailureFingerprint
- RepairPlan
- RepairAttempt
- RepairOutcome

## Dependencies
- M19 Quality
- M01 Graph
- M03 models
- M21 cost
- M22 memory
- M23 lineage

## Failure modes and safeguards
- repair worsens other region → regression gate reject
- repeated repair loop → retry budget/stop condition
- wrong defect localization → escalate scope
- provider failure → alternate plan

## Observability
- repair success
- percentage regenerated
- cycles per defect
- cost saved vs full regen
- strategy win rate

## Security / rights
- repair cannot relax non-negotiable policy/rights constraints
- parent/child lineage immutable

## Tests and benchmarks
- synthetic defect fixtures
- minimal impact assertions
- repair-loop budget
- cross-modal repair scenarios
- cost comparison

## Acceptance criteria for first usable V2 path
- [ ] a localized failure is repaired without rebuilding unrelated nodes
- [ ] repair derivative points to parent and defect
- [ ] failed repair cannot silently replace accepted artifact

## Deliberately out of this module
- unbounded self-modification
- silent quality-threshold lowering

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
