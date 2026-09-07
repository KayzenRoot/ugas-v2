# ADR-0009 — Minimal repair with lineage

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
Regenerating entire images, shots or mixes after a localized defect wastes compute and may destroy already-correct details.

## Decision
Repair planning should minimize affected region/segment/node while preserving parent/child provenance and rerunning relevant quality gates.

## Consequences
- lower cost and less identity drift
- defect localization is important
- repair loops need bounded stop conditions

## Alternatives considered
- Always full-regenerate: wasteful
- Edit in place without parent record: breaks lineage

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
