# WO-S00 Kernel Sync

Status: PREPARED / DO NOT EXECUTE YET
Executor: Codex
Context Pack: .engineering/preprogramming/S00-KERNEL-SYNC-CONTEXT-PACK.md

## Mission
Complete and prove the frozen UGAS V2 cross-cutting kernel so all later shards share evidence, adapter, failure and observability semantics.

## Constraints
- No architecture redesign.
- No M41+ proposal.
- No broad repository exploration.
- No provider/model installation.
- No GPU/media benchmark.
- No full test suite.
- Existing module behavior changes only when a focused compatibility test demonstrates a contract conflict.

## Acceptance
- evidence graph detects cycles and produces deterministic fingerprint
- carry-forward checks dependency fingerprints
- adapter qualification is version-specific and fail-closed
- retry classification cannot retry policy/quality/capability/integrity rejection
- telemetry records are secret-safe and trace/evidence correlated
- kernel A0/A1 green
- changed compatibility bridges, if any, have focused A2 proof
- exact-head evidence bundle produced

## Failure handling
Retry only the smallest failing scope. Fix the causal defect. Do not rerun unrelated shards. If a source-of-truth conflict requires architecture change, STOP and report it rather than improvising.

## STOP CONDITION
Produce evidence and stop after S00 acceptance. S01 requires a separate bounded execution.
