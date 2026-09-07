# ADR-0006 — Provider-independent multimodal IR

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
Prompts and provider parameters are implementation details; UGAS needs durable intent across executors.

## Decision
Scene/Character/Camera/Motion/Audio/Music/Narrative/Platform intent is stored as versioned IR and compiled through provider adapters. Unsupported semantics must be explicit.

## Consequences
- intent is diffable/reusable
- compiler and schema evolution required
- silent capability loss is prohibited

## Alternatives considered
- Provider prompt as source: rejected
- One universal raw JSON pass-through: rejected because it simply relocates provider coupling

## Supersession
This ADR remains authoritative until explicitly superseded by a later accepted ADR and Decisions Ledger update.
