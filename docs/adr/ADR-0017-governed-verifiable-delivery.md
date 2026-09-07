# ADR-0017 — Governed, Verifiable Delivery

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
UGAS V2 produces many artifact types for local use, DCCs, game engines, media pipelines and external destinations. Treating export as a simple file-save or upload step would lose dependency, quality, rights, security, reproducibility and retry semantics. Platform-specific rules must also not leak into canonical creative intent.

## Decision
UGAS V2 SHALL model export/delivery as a governed domain boundary with versioned Export Profiles and Delivery Targets, explicit dependency closure, target capability validation, release manifests, M19 readiness gates, M23 rights/provenance attachment, M24 egress authorization, M25 staging, M27 retry/idempotency semantics and M26 evidence/observability.

A delivery SHALL distinguish transport completion from verified delivery. Unsupported target capabilities SHALL fail explicitly or use an approved downgrade plan. Consequential external retries SHALL reconcile ambiguous outcomes before replay. Delivery adapters SHALL remain replaceable and platform/provider/DCC/engine-specific behavior SHALL stay outside canonical creative intent.

## Consequences
### Positive
- reproducible and auditable releases;
- safer external egress;
- explicit fidelity loss instead of silent degradation;
- retry-safe/resumable delivery;
- consistent delivery semantics across modalities and destinations;
- easier DCC/game-engine/platform adapter evolution.

### Costs
- more domain records and validation;
- target capability profiles require maintenance;
- adapter conformance/testing overhead;
- post-transfer verification may add latency/cost.

## Rejected alternatives
### Export equals file copy/upload
Rejected because transfer alone cannot prove completeness, compatibility, rights/security compliance or destination correctness.

### Platform-specific state inside Production Graph creative intent
Rejected because provider/platform coupling would damage portability and canonical intent.

### Silent target downgrade
Rejected because fidelity/metadata/capability loss must be visible and governed.

### Blind retry after timeout
Rejected because external side effects may already have succeeded and duplicate delivery/publication can result.
