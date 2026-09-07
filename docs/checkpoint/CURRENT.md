# UGAS V2 — CURRENT CHECKPOINT

**Status:** ROUND_27_PLANNING_READY_FOR_AUDIT  
**Repository:** KayzenRoot/ugas-v2  
**Canonical branch:** main  
**Planning branch:** docs/round-27-automation-agents  
**Implementation status:** NOT STARTED  
**Last reconciled main SHA:** a70d92aa48facee5afe8e2b1c391b160cb334e3b

## Canonical state established
UGAS V2 uses repository state and canonical documentation as the source of truth. Chat memory remains non-authoritative.

## Previously approved planning
- Source Pack bootstrap APPROVED;
- Rounds 01–26 represented as M01–M26;
- M26 Observability & Dashboard APPROVED and checkpointed;
- ADR-0001 through ADR-0015 ACCEPTED;
- repository governance and Source Pack Integrity CI active.

## Active planning increment
**Round 27 / M27 — Automation & Agents**

### Planned artifacts in this increment
- `docs/modules/27-automation-agents.md`;
- ADR-0016 — Bounded Automation, Deterministic First;
- DEC-016 in Decisions Ledger;
- REQ-AUT-001 through REQ-AUT-016;
- M27 EPIC #37;
- Module/EPIC indexes through M27;
- functional catalog through Round 27.

## Round 27 architectural position
M27 is the governed orchestration layer for deterministic workflows, schedules/events and bounded reasoning agents. It does not create a parallel authority system: all consequential actions continue through canonical Production Graph/domain APIs, M24 security, M19 quality, M23 provenance/rights and M26 observability.

### Hard invariants
- deterministic workflow/state-machine execution is preferred when open-ended reasoning is unnecessary;
- agent use requires explicit objective, scope, capabilities/tools, security context, budgets, approvals and stop conditions;
- schedules/events/webhooks request work but never grant authority;
- model/agent output cannot create, widen or transfer capabilities;
- retries/duplicate triggers require idempotency or explicit equivalent safeguards;
- recovery and non-transactional rollback use governed compensation semantics;
- long-running workflow/agent state persists outside chat;
- multi-agent messages do not transfer privileges;
- agents cannot silently modify accepted governance/rights sources;
- significant automated decisions/tool actions expose M26-compatible evidence/rationale.

## Active EPIC
**#37 — [EPIC][M27] Automation & Agents**

## Audit target
Audit Round 27 planning against Source Hierarchy, Decisions, Scope, DoD, Architecture, Requirements and cross-module boundaries with M01, M02, M03, M19, M20, M21, M22, M23, M24, M25 and M26.

## Blocking rule
Do not advance to Round 28 while Round 27 requires correction or validation.
Product implementation remains out of this planning increment.

## Next after Round 27 APPROVED
**Round 28 — Export & Delivery.**

Expected focus: export packages/presets, platform/channel targets, validation, manifests, codecs/formats, game-engine/DCC delivery adapters, release bundles, rights/provenance credential attachment, resumable transfer and delivery evidence.

## New-chat bootstrap
When a new chat asks to continue UGAS V2:
1. fetch this checkpoint from GitHub;
2. reconcile current main SHA;
3. follow Source Hierarchy;
4. inspect active planning/implementation PR and EPIC;
5. read relevant ADRs, Scope, DoD, Architecture, Requirements and module specs;
6. never overwrite accepted repository decisions from chat memory;
7. continue only the current necessary increment.

## Historical evidence
- `docs/checkpoint/history/WO-PRE-001-SOURCE-PACK-BOOTSTRAP.md`
- `docs/checkpoint/history/ROUND-24-SECURITY-RESTRICTED-CONTENT.md`
- `docs/checkpoint/history/ROUND-25-STORAGE-CACHE-FABRIC.md`
- `docs/checkpoint/history/ROUND-26-OBSERVABILITY-DASHBOARD.md`
