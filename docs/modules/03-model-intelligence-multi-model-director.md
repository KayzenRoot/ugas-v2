# M03 — Model Intelligence & Multi-Model Director

**Round:** 03  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Make models/providers discoverable, empirically characterized, comparable and routable instead of hard-coded choices.

## Responsibilities
- model registry
- empirical model cards
- assimilation/benchmarks
- task/style/character affinity
- fitness scoring
- routing
- champion/challenger
- provider escalation/fallback
- drift tracking

## Planned capabilities
- discover/register model and version
- record license/origin/capabilities
- run modality/task benchmark suites
- compare quality/cost/latency/memory
- rank models for a workload
- route single or multi-model plans
- record rationale
- detect model/provider drift
- learn from approved/rejected outputs

## Candidate proprietary technologies
- **Model Genome** — multidimensional empirical capability profile
- **Empirical Model Card** — UGAS-derived evidence rather than vendor claims
- **Model Fitness Engine** — scores task/hardware/quality/cost fit
- **Task-Model Affinity Graph** — learned/evidenced task affinity
- **Character-Model Affinity** — identity-specific fit
- **Style-Model Affinity** — style-specific fit
- **Model Assimilation Pipeline** — standard onboarding/benchmark process
- **Model Drift Tracker** — detects behavior/version changes
- **Champion/Challenger** — controlled incumbent/candidate comparison
- **Pareto Model Routing** — multi-objective selection
- **Model Tournament** — candidate competition
- **Multi-Model Director** — global model/provider planner
- **Confidence-Based Provider Escalation** — uses expensive providers only when justified
- **Director Decision Ledger** — routing explanation history

## Inputs
- registered providers/models
- empirical benchmark evidence
- Hardware Genome
- task/IR/DNA constraints
- quality/cost/time budgets

## Outputs
- ModelProfile/Genome
- fitness scores
- selected candidates
- routing/execution plan
- decision rationale
- drift alerts

## How it works
1. Assimilate a model through provider metadata, license review and controlled benchmark fixtures.
2. Create empirical capability metrics and confidence by modality/task/hardware.
3. At planning time, filter incompatible models using hard constraints.
4. Score remaining models on task fit, identity/style affinity, hardware, quality, cost, latency and reliability.
5. Choose Pareto-efficient candidate(s); optionally run tournament/champion-challenger.
6. Execute through provider adapters and attach outcomes to the decision ledger.
7. Update affinity evidence and detect drift without silently rewriting historical benchmarks.

## Canonical data / contracts
- ModelProfile
- Provider
- ModelBenchmark
- AffinityRecord
- RoutingDecision

## Dependencies
- M02 Hardware Intelligence
- M04 IR
- M19 Quality Court
- provider adapters

## Failure modes and safeguards
- missing benchmark → lower-confidence routing
- provider outage → declared fallback/escalation
- model version drift → quarantine/rebenchmark
- license unknown → block restricted use

## Observability
- selection frequency
- win/loss by task
- quality/cost/latency
- fallback rate
- drift events
- confidence

## Security / rights
- provider secrets isolated
- license/origin recorded
- remote output treated as untrusted until validated

## Tests and benchmarks
- registry/version tests
- fitness determinism
- routing Pareto fixtures
- fallback tests
- drift detection
- benchmark reproducibility

## Acceptance criteria for first usable V2 path
- [ ] two interchangeable model/provider paths can be registered and compared
- [ ] routing explains why a model was chosen
- [ ] unsupported hardware/model pair is rejected before execution
- [ ] drift invalidates stale empirical confidence

## Deliberately out of this module
- training foundation models
- provider billing administration beyond usage/cost ingestion

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
