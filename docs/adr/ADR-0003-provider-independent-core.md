# ADR-0003 — Provider-independent core

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
Generative model vendors and APIs change rapidly. Provider coupling would make identity, workflows and project memory unstable.

## Decision
Canonical domain models and IR cannot depend on provider SDK types. Provider adapters declare capabilities and translate normalized requests/results.

## Consequences
- providers/models become replaceable
- adapter contracts and capability negotiation are required
- provider-specific features may require explicit extensions

## Alternatives considered
- Hard-code preferred provider: rejected due lock-in
- Store prompts as canonical truth: rejected because semantics cannot be preserved reliably

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
