# ADR-0002 — Local-first, not local-only

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
UGAS must use local compute efficiently while retaining access to APIs, LAN workers and remote GPUs when justified.

## Decision
The control/domain system is designed to operate locally and to add remote executors through explicit worker/provider contracts.

## Consequences
- privacy/cost/offline benefits remain possible
- remote capacity can be introduced without redesigning core
- network/provider failures must be first-class

## Alternatives considered
- Local-only: too restrictive
- Cloud-first: creates unnecessary dependency and cost

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
