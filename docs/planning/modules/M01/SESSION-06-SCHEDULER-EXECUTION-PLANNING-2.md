# M01 Replanning — Session 06: Scheduler & Execution Planning 2.0

Status: DISCUSSED / CANDIDATE
Program: #52

## Objective
Compile READY production graph nodes into efficient execution waves across heterogeneous compute without weakening recipe quality gates. The scheduler must optimize time-to-accepted-artifact, not raw task throughput.

## Scheduling inputs
Each executable node declares or receives estimates for:
- CPU cores/threads and RAM;
- GPU class, VRAM floor/target and compute capability;
- model/tool residency and warm-cache state;
- disk/scratch/storage bandwidth;
- network/upload/download requirements;
- DCC/runtime exclusivity constraints;
- expected duration and uncertainty;
- monetary cost;
- quality profile/fidelity level;
- deadline/priority;
- dependency criticality;
- preemptibility/checkpointability;
- privacy/rights/offload policy;
- evidence/test requirements.

## Resource topology
M02 provides a live Hardware/Compute Topology. Resources may include local CPU, local GPU(s), integrated GPU, RAM, NVMe/scratch, remote GPU workers, provider APIs, headless DCC workers, render workers and future specialized accelerators.

The topology is dynamic. Thermal pressure, VRAM fragmentation, model residency, provider health and remote cost can alter effective capacity.

## Candidate proprietary technology: QACP — Quality-Aware Critical Path
Traditional critical path minimizes completion time. QACP estimates the path to an **accepted** artifact, incorporating probability of Quality Court failure, expected repair cost, evidence cost and candidate uncertainty.

A slightly slower high-confidence operation may outrank a faster operation when the latter statistically causes expensive downstream repair.

## Candidate proprietary technology: VRAM Elastic Packing (VEP)
VEP schedules GPU jobs according to measured/learned VRAM envelopes, model residency, fragmentation and safe headroom. It can:
- keep a hot model resident when beneficial;
- evict/unload models deliberately;
- serialize incompatible peaks;
- overlap CPU/DCC/I/O work with GPU generation;
- select lower-fidelity stages for exploration;
- route oversized stages to tiled/sequential/offloaded execution when recipe permits.

No optimistic overcommit is allowed when OOM risk exceeds policy.

## Candidate proprietary technology: Creative Compute Exchange (CCX)
CCX is a policy-driven local/cloud/provider execution broker. It evaluates qualified implementations against quality, privacy, rights, latency, monetary cost, transfer overhead, hardware fit and current availability.

It does not automatically choose the cheapest provider. Hard quality/security/rights constraints filter candidates first; optimization happens inside the valid set.

## Candidate proprietary technology: Acceptance ETA (AETA)
AETA predicts remaining time/cost to acceptance rather than only current-job ETA. It uses DAG state, historical durations, candidate tournament survival, expected repairs, cache state and current hardware/provider health. M26 can expose confidence bands rather than false precision.

## Execution waves
The planner compiles work into bounded waves:
1. deterministic/preflight work;
2. low-cost candidate/proxy generation;
3. early hard-gate evaluation;
4. finalist promotion to expensive fidelity;
5. DCC/render/runtime work;
6. focused Quality Court/repair;
7. convergence evidence.

Independent CPU, GPU, I/O and DCC work may overlap when resource envelopes and dependency semantics allow it.

## RTX 5050 8 GB strategy
For constrained local GPUs the default strategy should favor:
- one heavy VRAM consumer at a time unless profiling proves safe overlap;
- CPU preprocessing/postprocessing during GPU occupancy;
- model warm-residency only when reuse benefit exceeds memory pressure;
- proxy/preview tournaments before expensive hero generation;
- tiled/chunked/temporal-window execution where validated;
- aggressive reuse of accepted artifacts/proofs;
- background/headless Blender tasks coordinated with GPU pressure;
- optional offload for stages that cannot meet the recipe envelope locally.

The hardware profile is discovered, not hard-coded to this GPU.

## Preemption and checkpointing
Tasks declare NONE, RESTARTABLE or CHECKPOINTABLE. High-priority critical-path work may preempt safe lower-priority work. Partial outputs are promoted only if the tool contract defines valid resumable state. Killing a process is not considered checkpointing.

## Speculative execution policy
The scheduler may use spare resources for alternative candidates or likely-next operations only when:
- the branch is isolated;
- budget remains;
- expected value exceeds configured waste threshold;
- no higher-priority accepted-path work is delayed;
- speculative artifacts cannot silently become canonical.

## Thermal and health awareness
Sustained local production must observe temperatures, throttling, OOM/restart history, disk pressure and worker health. A degraded worker can be derated or quarantined. Performance policy must never disable hardware safety controls.

## Model/tool cold-start economics
Execution planning accounts for model downloads, load/unload time, shader/kernel compilation, DCC startup, remote transfer and cache locality. The planner can batch compatible work to amortize cold starts without violating priority or quality constraints.

## Failure-aware scheduling
Retries are classified. Deterministic contract failures do not receive blind retries. Transient provider/network/worker failures may retry under bounded policy. OOM triggers envelope correction or alternate execution plan, not infinite identical retries.

## Evidence-aware scheduling
A0/A1-style focused checks occur near the capability that changed. Expensive Golden Set/full-runtime convergence is scheduled at deliberate promotion boundaries. Previously compatible PROVEN/CARRY_FORWARD evidence is not recomputed merely because another branch executed.

## Scheduler decision record
Every non-trivial routing decision can emit a compact record:
- candidate resources considered;
- hard filters;
- selected resource/tool capability;
- predicted duration/cost/quality confidence;
- cache/residency assumptions;
- fallback plan;
- policy version.

This supports audit, optimization and future learned scheduling.

## Learned scheduler boundary
Historical telemetry may train duration, VRAM, failure and repair-risk estimators. Learned models can rank valid plans but cannot bypass hard contracts, rights/security policy, recipe gates or deterministic dependency semantics.

## Dashboard contract
M26 should show live:
- CPU/RAM/GPU/VRAM and worker topology;
- running/queued/blocked work;
- critical path and QACP path;
- model residency/cache;
- local vs remote routing;
- predicted acceptance ETA/cost confidence range;
- GPU utilization vs idle/waste;
- OOM/retry/thermal events;
- speculative compute spend and win rate;
- proof reuse savings.

## Session 06 acceptance
- scheduler optimizes time-to-accepted-artifact;
- heterogeneous CPU/GPU/DCC/I/O work can safely overlap;
- VRAM constraints and model residency are first-class;
- local/cloud routing honors quality/security/rights before cost;
- preemption/checkpoint semantics are explicit;
- speculative work is bounded and isolated;
- failures change plans instead of causing blind retry loops;
- learned optimization cannot override deterministic hard gates;
- RTX 5050-class hardware can operate through progressive fidelity and selective offload without lowering final recipe acceptance.

## Next M01 session
Session 07: Snapshots, Branches & Experiment System 2.0, including immutable production snapshots, cheap copy-on-write branches, candidate/repair/technology experiments, merge semantics, conflict detection and reproducible replay.