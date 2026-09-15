# M01 Replanning — Session 03: Production State Machine 2.0

Status: DISCUSSED / CANDIDATE
Program: #52

## Objective
Turn production lifecycle into an evidence-governed, branchable and repair-aware state machine that supports candidate tournaments, experiments and autonomous convergence without allowing quality to be averaged away.

## Core lifecycle
`DRAFT -> SPECIFIED -> READY -> RUNNING -> PRODUCED -> EVALUATING -> ACCEPTED`

Governed alternate states:
- BLOCKED
- FAILED
- CANCELLED
- REJECTED
- REPAIR_REQUIRED
- REPAIRING
- INVALIDATED
- SUPERSEDED
- ARCHIVED

Every transition is an event with actor, reason, source state, target state, policy version, evidence references and timestamp. State is derived from the append-only transition/event log and may be materialized for fast reads.

## Acceptance ladder
Media acceptance is typed, not boolean. Baseline levels:
- CONCEPT_ACCEPTED
- MASTER_ACCEPTED
- DERIVATIVE_ACCEPTED
- RIG_ACCEPTED
- MOTION_ACCEPTED
- RUNTIME_ACCEPTED
- DELIVERY_ACCEPTED

Recipes select which levels apply. Game-ready character delivery cannot skip RUNTIME_ACCEPTED when the target profile requires runtime proof.

## Candidate Tournament
A recipe may fan out one node into multiple candidate branches. Candidates can vary seed, model/provider, workflow, control/reference strategy, DCC operation or parameter set while preserving the same target contract.

Tournament phases:
1. cheap deterministic/preflight rejection;
2. hard quality gates;
3. domain judge scoring;
4. pairwise or ranked comparison where useful;
5. cost/latency/VRAM normalization;
6. diversity/novelty protection;
7. finalist high-assurance evaluation;
8. canonical winner promotion.

Aesthetic scores never override a hard usability failure such as invalid anatomy, broken topology, bad rig/deformation, rights violation or runtime incompatibility.

## Candidate proprietary technology: Evolutionary Production Tournament (EPT)
EPT is a governed search layer over Production Graph branches. It allocates more compute only to promising candidates and prunes weak branches early. It may use successive-halving/bandit-style resource allocation, Pareto fronts and quality uncertainty, but the strategy is replaceable and benchmarked.

Candidate objective vector:
`quality, contract adherence, identity consistency, runtime fitness, repairability, cost, latency, VRAM, provenance confidence`

No single scalar score is mandatory. Pareto-optimal candidates can survive when trade-offs are meaningful.

## Candidate proprietary technology: Evidence-Gated State Machine (EGSM)
A transition declares required evidence predicates. The state engine cannot promote a node if required predicates are UNKNOWN, INVALIDATED or missing. Carry-forward evidence is allowed only when its fingerprint remains compatible with the delta.

## Candidate proprietary technology: Bounded Autonomous Convergence (BAC)
Repair loops receive explicit budgets:
- max repair attempts;
- max wall-clock/GPU time;
- max monetary cost;
- allowed repair radius;
- allowed tool/model classes;
- minimum expected improvement;
- no-regression constraints.

If convergence stalls, BAC stops at BLOCKED/REQUIRES_REVIEW instead of burning compute indefinitely.

## Repair semantics
A failed judge emits a structured defect with affected dimensions and evidence. M20 compiles a repair plan. M01 state/graph semantics then:
1. open a repair revision/branch;
2. invalidate only intersecting proof dimensions;
3. preserve compatible accepted proof;
4. execute repair;
5. rerun affected gates;
6. merge repair only when no-regression requirements pass.

## Speculative creative execution
When compute is idle and policy permits, the planner may prepare or execute low-cost alternative candidates before a downstream choice is final. Speculative artifacts remain isolated and cannot become canonical without normal gates. This can hide latency in long media pipelines while controlling waste.

## Experiment branches
Experiments are first-class graph branches with declared hypothesis, changed dimensions, budget, success metrics and expiration policy. Experiments never silently mutate canonical production. A successful experiment is promoted through an explicit merge/promotion event with evidence.

## Human and agent authority
Transitions declare authority requirements. Routine deterministic transitions can be automatic. High-risk rights/security/destructive/publishing decisions can require stronger authorization. Creative approval may be automated only when the recipe and calibrated Quality Court permit it; a human escape hatch remains available for subjective/high-value decisions.

## New-technology assimilation hook
M01 does not hard-code model families. M03 may register a new model/tool candidate; EPT can evaluate it against the same production contract in an isolated branch. Promotion changes the capability routing registry only after benchmark/license/hardware evidence. This makes future model adoption an experiment rather than an architecture migration.

## Hardware-aware convergence
Candidate/repair scheduling receives hardware facts from M02 and routing economics from M21. For constrained local hardware, the state machine can progress through proxy/preview stages, offload only expensive stages, or queue background/headless DCC work without weakening the final acceptance contract.

## Event classes
Minimum event taxonomy:
- NODE_CREATED
- SPEC_LOCKED
- READY_DECLARED
- RUN_STARTED / RUN_FINISHED / RUN_FAILED
- ARTIFACT_PRODUCED
- EVALUATION_STARTED / JUDGE_RESULT
- REPAIR_REQUESTED / REPAIR_APPLIED
- EVIDENCE_INVALIDATED / EVIDENCE_CARRIED_FORWARD
- CANDIDATE_FORKED / CANDIDATE_PRUNED / CANDIDATE_PROMOTED
- EXPERIMENT_OPENED / EXPERIMENT_CLOSED
- ACCEPTANCE_GRANTED / ACCEPTANCE_REVOKED
- SNAPSHOT_CREATED / BRANCH_MERGED
- DELIVERY_PROMOTED

## Observability
M26 should visualize:
- state distribution and transition velocity;
- blocked/failed nodes;
- repair loops and convergence rate;
- tournament funnel and candidate costs;
- quality deltas per iteration;
- proof carry-forward/invalidation ratios;
- GPU/VRAM/time/cost per accepted artifact;
- experiment win/loss and promoted technology rate.

## Failure safeguards
- infinite repair loop -> BAC budgets and convergence stop;
- cheap candidate wins through score averaging -> hard gates before ranking;
- stale proof -> EGSM fingerprint validation;
- speculative branch contaminates canonical state -> isolated branch namespace;
- model update silently changes output -> immutable model/tool identity and benchmark promotion;
- race between concurrent runs -> optimistic version/precondition checks on promotion;
- non-deterministic replay -> event log plus explicit run environment/provenance.

## Session 03 acceptance
- acceptance is typed and evidence-gated;
- candidate competition is first-class;
- repair is bounded and delta-aware;
- experiments cannot mutate canonical state silently;
- new models/tools can be assimilated without architecture rewrites;
- local/cloud/headless execution can coexist;
- hard quality defects cannot be averaged away;
- autonomous loops have deterministic stop conditions.

## Next M01 session
Session 04: Production Recipes 2.0 and Quality Profiles, including AAA-isometric/game-runtime recipes, recipe inheritance/composition, target-quality contracts and how downstream modules plug specialized gates into the kernel.