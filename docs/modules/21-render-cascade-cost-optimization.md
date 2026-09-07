# M21 — Render Cascade & Cost Optimization

**Round:** 21  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Allocate compute progressively so expensive fidelity is spent only on candidates and regions likely to become accepted outputs.

## Responsibilities
- draft/preview/final stages
- candidate tournaments
- quality-cost prediction
- selective enhancement
- waste tracking
- quality/compute budgets
- approved-output economics

## Planned capabilities
- cheap candidate generation
- early quality screen
- candidate ranking
- progressive upscale/refine
- cost/time prediction
- budget enforcement
- wasted render analysis
- compute ROI metrics

## Candidate proprietary technologies
- **Render Cascade Engine** — orchestrates fidelity stages
- **Progressive Fidelity Pipeline** — raises fidelity only when justified
- **Candidate Tournament** — compares candidate set
- **Cost-to-Quality Predictor** — estimates quality gain per extra resource
- **Selective Enhancement Engine** — refines only needed regions
- **Waste Render Detector** — identifies compute with no useful result
- **Quality Budget Allocator** — distributes compute budget
- **Compute ROI Score** — quality return per consumed resource

## Inputs
- production quality target
- candidate plans
- Hardware/Model profiles
- budgets/deadlines
- Quality Court results

## Outputs
- cascade plan
- candidate shortlist
- stage decisions
- cost metrics
- final selected artifact path

## How it works
1. Translate final quality target into staged fidelity plan.
2. Generate low-cost candidates with enough fidelity for early discrimination.
3. Run fast applicable quality judges and eliminate obvious failures.
4. Rank survivors by predicted final quality/cost/time and diversity.
5. Spend enhancement/final render only on selected candidate(s) or regions.
6. Record predicted and actual economics per stage.
7. Learn where draft quality is or is not predictive of final acceptance.

## Canonical data / contracts
- RenderCascade
- CascadeStage
- Candidate
- Budget
- CostRecord
- ROIRecord

## Dependencies
- M02 Hardware
- M03 Models
- M19 Quality
- M20 Repair

## Failure modes and safeguards
- draft ranking mispredicts final → calibration update
- budget exhausted → stop/block or explicit scope decision
- quality sacrificed silently → forbidden
- cost provider data missing → mark estimate confidence

## Observability
- cost per accepted output
- waste %
- candidate survival
- predicted vs actual quality/cost
- time saved

## Security / rights
- cost optimization never bypasses mandatory safety/rights/quality gates

## Tests and benchmarks
- cascade vs max-fidelity benchmark
- budget enforcement
- ranking calibration
- selective enhancement savings

## Acceptance criteria for first usable V2 path
- [ ] representative workflow costs less compute than naive all-max baseline without breaching quality target
- [ ] budget/decision rationale is inspectable
- [ ] cost measured per accepted result

## Deliberately out of this module
- financial trading/billing engine
- autonomous external purchasing beyond configured provider use

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
