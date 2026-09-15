# M30 — Session 03: Blender Headless Execution Engine

Status: PLANNED / IMPLEMENTATION-READY CANDIDATE

## Mission
Turn validated DCC-IR transactions into isolated, observable, recoverable Blender executions without requiring a human to open the desktop application.

## Execution architecture
Production Graph -> DCC-IR -> Capability Negotiation -> Job Compiler -> Blender Worker -> Python Operation Runtime -> Scene Transaction Engine -> Artifact/Evidence Store -> Quality Court.

## Worker lifecycle
QUEUED -> PREFLIGHT -> PREPARING -> RUNNING -> CHECKPOINTING -> VALIDATING -> COMMITTING -> SUCCEEDED.
Failure states: BLOCKED, TIMED_OUT, CRASHED, FAILED_VALIDATION, ROLLED_BACK, QUARANTINED.

## Headless worker contract
Each worker receives immutable job manifest, approved input roots, scratch root, output root, pinned Blender/tool profile, operation payload, resource budget, timeout, evidence requirements and expected artifact contract.

## Process isolation
Normal execution occurs in a dedicated process with per-job scratch space. Canonical masters are read-only inputs until transaction commit. Outputs are first written to staging, validated, fingerprinted and only then promoted.

## Proprietary technology: BWE — Blender Worker Envelope
BWE is the constrained runtime around each Blender process. It owns environment preparation, workspace isolation, process launch, heartbeat, stdout/stderr capture, telemetry, timeout, termination, output collection and cleanup.

## Proprietary technology: HSR — Headless Scene Recovery
HSR creates transaction-aware checkpoints at meaningful DCC boundaries. On crash, recovery resumes from the latest compatible checkpoint rather than restarting the entire expensive pipeline. Checkpoints are invalidated when their source/tool/operation fingerprints no longer match.

## Proprietary technology: VRAM Pressure Governor
A resource governor integrates with M02/M21 to avoid blind GPU oversubscription. It tracks estimated and observed VRAM/RAM, active heavy workers, model/tool residency and can delay, serialize, lower development fidelity or route work elsewhere. It never silently lowers final acceptance quality.

## Proprietary technology: DCC Warm Start Cache
Reusable immutable resources such as approved base scenes, node groups, shader libraries, geometry-node assets and adapter bootstrap data can be cached by fingerprint. Cache reuse requires compatibility proof.

## GPU and CPU modes
Execution profile declares CPU_ONLY, GPU_PREFERRED, GPU_REQUIRED or HYBRID. The worker records actual selected devices. A GPU request that falls back unexpectedly is surfaced as evidence and may fail performance-sensitive jobs.

## RTX 5050 8 GB profile
Local strategy: one heavy Blender/GPU task at a time unless measured headroom permits concurrency; aggressive staging; texture/bake tiles where valid; adaptive subdivision; sequential heavy stages; CPU preprocessing/postprocessing while GPU is occupied; cache approved immutable resources; release memory between incompatible workloads; coordinate with neural-model residency.

## Watchdog
Heartbeat contains process state, current op_id, elapsed time, CPU/RAM, GPU/VRAM when available, last checkpoint and progress hints. Stalls use staged response: diagnose -> graceful cancel -> checkpoint if safe -> terminate -> classify -> retry only if policy permits.

## Retry taxonomy
TRANSIENT_ENVIRONMENT: bounded retry.
RESOURCE_PRESSURE: reschedule/re-route.
DETERMINISTIC_OPERATION_FAILURE: no blind retry; defect/operation must change.
CORRUPT_INPUT: quarantine input and block.
TOOL_CRASH: recover checkpoint and bounded retry.
UNKNOWN: diagnostics + conservative escalation.

## Python operation runtime
Adapters expose tested functions rather than arbitrary generated scripts for common operations. Generated scripts, when exceptionally required, execute only through a restricted reviewed path with explicit provenance and policy. The long-term goal is to convert frequently successful agent procedures into deterministic primitives.

## Add-on policy
No automatic internet installation inside production workers. Add-ons are pinned, hashed, licensed, security-qualified and included in a tool profile. Experimental add-ons run in sandbox profiles and cannot silently become production dependencies.

## Scene commit
STE computes source fingerprint, executes operations in staging, computes target fingerprint, validates postconditions and artifact contracts, emits SFD delta and atomically promotes the resulting scene/artifacts only when commit conditions pass.

## Diagnostic outputs
On failure, preserve minimal useful diagnostics: operation log, crash/error summary, scene checkpoint when safe, source/tool fingerprints, resource trace and requested validation output. Avoid giant redundant evidence dumps.

## Observability
M26 receives job state, op state, Blender version/profile, device, CPU/RAM/GPU/VRAM, wall time, checkpoint, cache hit/miss, retry reason, artifacts, validation and estimated completion.

## Security
Approved workspace roots only; canonical source read-only until commit; no unrestricted shell from LLM; no arbitrary network from worker; secrets absent by default; generated content treated as untrusted; file import/export types validated; resource limits enforced.

## Acceptance benchmark
A representative headless job must create/open a scene, import or create geometry, run cleanup, assign a material, create target camera/light, render diagnostics, save a staged blend, export a runtime artifact, validate outputs and commit evidence. A forced mid-job crash must demonstrate bounded recovery or clean rollback without corrupting the accepted source.