# ADR-0001 — Repository is canonical source

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
UGAS V2 must survive chat limits and model-memory drift. Conversation history is convenient but not deterministic or reviewable.

## Decision
KayzenRoot/ugas-v2 and its governed Git history are the source of truth. Chat memory is advisory only. New chats bootstrap from CURRENT checkpoint and canonical hierarchy.

## Consequences
- handoffs become deterministic
- documentation updates are mandatory after approved increments
- chat recollection cannot override repository state

## Alternatives considered
- Use chat memory as primary source: rejected because it is not durable/reviewable
- Keep one monolithic external document: rejected because it lacks Git-native review and modularity

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
