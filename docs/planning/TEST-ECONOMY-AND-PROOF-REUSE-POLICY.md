# UGAS V2 Test Economy & Proof Reuse Policy

Status: CANDIDATE — WO-0002

## Goal
Maximize engineering throughput without turning tests into either a bottleneck or theater. Codex must spend most execution time implementing useful increments, not repeatedly rerunning unaffected proof.

## Core principle
**Test what changed; reuse what did not; invalidate only what the delta can affect; converge with broader gates at deliberate checkpoints.**

Exact-head confidence does not mean every test must execute on every commit. It means every required claim at the exact head has either fresh proof or explicitly valid carry-forward proof whose inputs and assumptions did not change.

## Proof states
- PROVEN: executed for current relevant inputs.
- CARRY_FORWARD: prior proof remains compatible with current delta.
- INVALIDATED: delta touches an input/dependency/contract that proof relied on.
- UNKNOWN: insufficient evidence; never PASS.
- NOT_REQUIRED: outside current assurance requirement.

## Test Impact Graph
Every implementation session SHOULD declare:
- changed components/files;
- contracts touched;
- direct dependents;
- test/benchmark IDs covering them;
- proof inputs/fingerprints;
- invalidation triggers.

The executor uses this graph to select the smallest sufficient test set.

## Assurance ladder
### A0 — edit loop, seconds to a few minutes
Syntax, schema, formatting/static checks and tiny deterministic smoke checks for changed files only.

### A1 — capability loop
Focused unit/contract tests directly covering the changed capability. Run after a coherent patch, not after every keystroke.

### A2 — session convergence
Impacted integration/regression/eval tests for the session dependency cone. Run when the session reaches a candidate state or when a correction changes a relevant contract.

### A3 — promotion/PR convergence
Hosted CI, security, platform and selected broader regression. Full or near-full regression is used only when required by risk, shared-core changes, release convergence or scheduled promotion policy.

### A4 — HEDS
Independent delta/evidence review. HEDS verifies whether carried proofs remain compatible and rejects unjustified reuse.

## Correction-loop rule
When a test fails:
1. identify the failure's smallest causal component;
2. fix within the same Work Order;
3. rerun the failed test plus its immediate dependency cone;
4. do NOT rerun unrelated green suites;
5. expand only if the correction touches a broader contract or the focused proof exposes uncertainty;
6. perform A2/A3 once the correction converges.

No `full suite -> one failure -> tiny fix -> full suite -> repeat` loop by default.

## Proof cache
Evidence SHOULD be addressable by fingerprints including, where applicable:
- test ID/version;
- relevant source hashes;
- contract/schema hashes;
- dependency lock hash;
- model/tool version;
- fixture/golden-set hash;
- hardware/provider profile when material;
- environment/runtime version.

If none of a proof's material inputs changed, the proof may be CARRY_FORWARD. If any material input changed, it is INVALIDATED and must be rerun at the appropriate assurance level.

## Test budgets
Each Work Order SHALL declare a test budget and expected implementation budget. Default planning targets:
- A0 <= 5 minutes per coherent patch cycle;
- A1 <= 15 minutes per capability convergence;
- A2 <= 30 minutes per session convergence unless media benchmarks require longer;
- A3 may be longer but SHOULD run once per promotion candidate rather than every correction;
- expensive GPU/media benchmarks are sampled during development and run as complete golden-set gates only at defined quality convergence points.

Budgets are targets, not reasons to suppress a required safety/security/quality proof. Exceeding a budget triggers test optimization/sharding/caching analysis before repeated execution.

## Long Codex runs
A 5–6 hour Codex Work Order is acceptable when it produces multiple coherent capabilities and evidence checkpoints. It is NOT acceptable for most of that time to be consumed by repeated unaffected regression.

Long WOs SHOULD be partitioned internally into implementation waves:
`implement wave -> A0/A1 -> continue -> A0/A1 -> session A2 -> final A3`

Codex SHALL persist intermediate evidence so a late failure does not erase prior compatible proof.

## Media/AI-specific economy
Generation and quality evaluation can be expensive. Use:
- deterministic micro-fixtures for plumbing/contracts;
- small representative quality samples during edit loops;
- cached model downloads and immutable model/version identities;
- golden-set shards selected by impacted quality dimensions;
- full Golden Set only at promotion/release or when a model/pipeline stage materially changes;
- no regeneration of unchanged accepted assets merely to re-prove unrelated code.

## Mandatory full/broad regression triggers
Broader proof is required when the delta changes shared core contracts, dependency/runtime foundations, persistence/schema compatibility, security boundaries, model-routing semantics, asset lineage/provenance rules, Quality Court acceptance semantics, release packaging, or when HEDS cannot justify carry-forward.

## Throughput metric
Track separately:
- implementation time;
- test execution time;
- test rerun waste;
- proof reuse ratio;
- invalidation ratio;
- flaky retry time;
- GPU benchmark time.

Target: reduce rerun waste, not reduce meaningful coverage.

## Anti-patterns forbidden
- rerunning the entire suite after every small correction;
- changing tests merely to make a failure green without requirements evidence;
- declaring PASS because an old run exists when inputs changed;
- running expensive media generation when deterministic fixtures prove the changed plumbing;
- allowing Codex to explore thousands of tests to infer what should be run when the Work Order can precompile the impacted set.

## Delivery-speed objective
The engineering system SHALL be optimized for an aggressive V2 construction window measured in approximately 1–2 weeks of concentrated execution. This is a throughput target, not permission to bypass HIGH_ASSURANCE gates or falsify evidence.