# ADR-0008 — Quality before acceptance

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
A provider returning a file does not establish that the asset is usable, consistent or policy-compliant.

## Decision
Generated artifacts must pass configured Quality Court gates and/or explicit human approval before becoming accepted production outputs.

## Consequences
- acceptance is evidence-based
- quality judge calibration becomes required
- failed outputs feed Repair rather than silently replacing masters

## Alternatives considered
- Auto-accept successful API calls: rejected
- Manual-only QA: too expensive and not scalable, though human override remains

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
