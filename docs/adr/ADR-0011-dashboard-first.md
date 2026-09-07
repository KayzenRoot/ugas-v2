# ADR-0011 — Dashboard-first operator experience

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
UGAS V2 spans many modalities and decisions. A CLI-only or hidden automation surface would make complex production hard to understand and control.

## Decision
The dashboard is the primary operator interface. It exposes standard workflows, advanced controls, graph state, decisions, quality, compute, costs, provenance and system health.

## Consequences
- UI architecture is a first-class concern
- explainability data must be available from services
- CLI/API may remain supporting interfaces

## Alternatives considered
- CLI-first: insufficient for intended studio operation
- Provider UIs as main interface: fragments control and memory

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
