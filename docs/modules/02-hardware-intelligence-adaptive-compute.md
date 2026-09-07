# M02 — Hardware Intelligence & Adaptive Compute

**Round:** 02  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Convert heterogeneous hardware into a measured capability model and safe adaptive execution policy.

## Responsibilities
- hardware discovery
- empirical benchmarking
- VRAM/RAM/storage/runtime characterization
- capability envelopes
- precision/offload/chunk decisions
- thermal/energy telemetry
- remote worker capability registration

## Planned capabilities
- discover CPU/RAM/GPU/VRAM/runtime/storage
- first-run microbenchmark
- continuous performance fingerprint
- predict OOM risk
- adapt batch/tile/chunk/precision
- GPU→RAM→NVMe offload planning
- thermal-aware scheduling
- ECO/BALANCED/QUALITY/MAX/CUSTOM modes
- decision explanations

## Candidate proprietary technologies
- **Hardware Genome** — versioned normalized hardware capability profile
- **Adaptive Execution Fabric** — maps workload + hardware to safe execution strategy
- **Dynamic VRAM Governor** — controls memory-sensitive execution knobs
- **Hardware-Aware Model Resolver** — filters/ranks models by hardware fit
- **Precision Auto-Tuner** — selects numeric precision/quantization
- **Adaptive Offload Planner** — plans VRAM/RAM/NVMe placement
- **Compute Digital Twin** — predictive model of machine behavior
- **Predictive OOM Shield** — pre-run/run-time memory risk detection
- **Hardware Learning Loop** — recalibrates from real runs
- **Compute Decision Ledger** — explains compute choices

## Inputs
- worker hardware/runtime telemetry
- model memory profiles
- workload specification
- quality/time/cost mode

## Outputs
- HardwareProfile/Genome
- capability envelope
- execution constraints
- resource reservation
- decision rationale
- observed performance fingerprint

## How it works
1. Probe hardware and runtimes without relying on GPU-name presets.
2. Run bounded calibration workloads to establish empirical throughput/memory observations.
3. Build a Hardware Genome combining declared specs and measured confidence.
4. For a workload, intersect requirements with the capability envelope and model candidates.
5. Compile precision, batch, chunk, tile, cache, residency and offload plan.
6. Reserve resources, execute and monitor thermal/memory pressure.
7. Feed actual results back into the performance fingerprint and future predictions.

## Canonical data / contracts
- HardwareProfile
- Worker
- BenchmarkRun
- CapabilityEnvelope
- ExecutionPlan compute section

## Dependencies
- M01 Production OS
- M03 model capability metadata
- execution workers

## Failure modes and safeguards
- probe unavailable → partial genome with reduced confidence
- OOM prediction wrong → fail safely/replan lower envelope
- thermal throttling → scheduler reduces concurrency
- stale driver/runtime → capability invalidation

## Observability
- VRAM/RAM use
- throughput
- temperature/power where exposed
- predicted vs actual memory/time
- OOM near-miss/failure
- offload overhead

## Security / rights
- remote workers authenticate
- hardware probes must not expose secrets
- worker capabilities are claims until verified empirically

## Tests and benchmarks
- fixture-based probe parsing
- real hardware smoke tests
- OOM prediction calibration
- policy comparison benchmarks
- thermal/offload behavior where supported

## Acceptance criteria for first usable V2 path
- [ ] system characterizes a supported workstation without hard-coded model name
- [ ] planner selects a safe plan from workload constraints
- [ ] predicted/actual metrics are stored
- [ ] OOM/failure produces a bounded replan path

## Deliberately out of this module
- vendor-specific tuning that belongs in adapter libraries
- unbounded cloud autoscaling

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
