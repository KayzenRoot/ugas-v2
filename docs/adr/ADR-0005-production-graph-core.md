# ADR-0005 — Production Graph as orchestration nucleus

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
Multimodal work has dependencies, versions, repairs and derived assets. File folders alone cannot safely express impact or reproducibility.

## Decision
Every governed production is modeled as a versioned Production Graph with typed nodes/edges, fingerprints, states, artifacts, evaluation and lineage.

## Consequences
- enables incremental rebuild and impact analysis
- graph/state invariants become critical
- all modules must integrate through graph semantics

## Alternatives considered
- Loose workflow files: insufficient lineage/impact
- Single linear pipeline: cannot represent branching multimodal work

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
