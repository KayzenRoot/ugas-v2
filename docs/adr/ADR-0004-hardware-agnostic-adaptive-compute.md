# ADR-0004 — Hardware-agnostic adaptive compute

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
UGAS must run across different GPUs/CPUs/RAM/storage and cannot assume the current workstation forever.

## Decision
Execution planning uses Hardware Genome + empirical benchmarks/capability envelopes, never architecture-defining fixed GPU-name presets.

## Consequences
- more portable execution
- requires benchmarking/telemetry and confidence
- performance policy becomes testable

## Alternatives considered
- Optimize only for RTX 5050: rejected as architectural lock
- Lowest-common-denominator settings: rejected due quality/performance waste

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
