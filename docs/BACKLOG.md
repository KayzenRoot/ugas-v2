# Backlog — UGAS V2

GitHub Issues are the execution backlog. This document defines dependency order.

## Phase 0 — Canonicalization and module planning
Source Pack; module specifications; ADR baseline; functional catalogs; EPIC Issues; scope/DoD freeze preparation.

Planning sequence currently:

- Rounds 01–23: specified and approved;
- Round 24: Security & Restricted Content — active planning increment;
- Round 25: Storage & Cache Fabric — next planned round after M24 approval;
- Round 26: Observability & Dashboard;
- Round 27: Automation & Agents;
- Round 28: Export & Delivery;
- later consolidation/scope-freeze/DoD/implementation-roadmap rounds remain subject to canonical planning.

## Phase 1 — Platform foundation
Production Graph/state machine; metadata persistence; artifact abstraction; run/attempt model; provider contract skeleton; security and observability foundations.

## Phase 2 — Intelligence
Hardware Genome; Model Registry/Genome; execution planner; routing; benchmark harness.

## Phase 3 — Creative representations
Multimodal IR; Asset DNA; identity; canon/memory primitives.

## Phase 4 — Studios
Image → Video → Motion → 3D → Voice → Music → Sound. Every studio plugs into canonical contracts, M24 security gates and Quality Court.

## Phase 5 — Applications
Narrative, Content Factory, Advertising, Brand/IP, Localization.

## Phase 6 — Quality/economics/memory/trust
Quality Court, Repair, Render Cascade, Memory/RAG, Provenance/Rights and Security/Restricted Content.

## Rule
During planning, complete the current round before advancing to the next planned round. During implementation, choose the smallest NECESSARY dependency that advances DoD without bypassing a blocker.
