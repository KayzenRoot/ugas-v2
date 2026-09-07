# UGAS V2 — CURRENT CHECKPOINT

**Status:** ROUND_25_PLANNING_READY_FOR_AUDIT  
**Repository:** KayzenRoot/ugas-v2  
**Canonical branch:** main  
**Planning branch:** docs/round-25-storage-cache-fabric  
**Planning PR:** #32  
**Implementation status:** NOT STARTED  
**Last reconciled main SHA:** 23472460f9e16b556a1937cfd302009c2107fad0

## Canonical state established
UGAS V2 uses repository state and canonical documentation as the source of truth. Chat memory remains non-authoritative.

## Previously approved planning
- Source Pack bootstrap APPROVED;
- Rounds 01–24 represented as M01–M24;
- M24 Security & Restricted Content APPROVED and checkpointed;
- ADR-0001 through ADR-0013 ACCEPTED;
- repository governance and Source Pack Integrity CI active.

## Active planning increment
**Round 25 / M25 — Storage & Cache Fabric**

### Planned artifacts in this increment
- `docs/modules/25-storage-cache-fabric.md`;
- ADR-0014 — content-addressed storage and cache correctness;
- DEC-014 in Decisions Ledger;
- REQ-STO-001 through REQ-STO-016;
- M25 EPIC #31;
- Module/EPIC indexes through M25;
- functional catalog through Round 25.

## Round 25 architectural position
M25 is the durable storage/cache substrate for UGAS V2. It separates logical artifact identity/metadata from large payload locations, uses cryptographic content identity for immutable payloads, distinguishes canonical state from rebuildable/disposable state, and makes cache/GC/tiering/recovery correctness-aware.

### Hard invariants
- paths are locations, not canonical identity;
- SOURCE/CANONICAL/EVIDENCE cannot be silently evicted as cache;
- deduplicated bytes do not merge rights/security/provenance identities;
- cache reuse must match all correctness-relevant fingerprints;
- semantic cache cannot impersonate exact equality for final/provenance/security/rights outputs;
- GC respects graph roots, shared references, holds, pins and leases;
- M24 security/data-class policy constrains placement and replication;
- recovery distinguishes irreplaceable state from safely rebuildable state.

## Active EPIC
**#31 — [EPIC][M25] Storage & Cache Fabric**

## Audit evidence so far
- initial PR head `0c267dbff302647d0657c6ca7c18a7716a7b42f4` failed Source Pack Integrity;
- finding: module spec count was 25 while `docs/modules/INDEX.md` still listed 24;
- classification: CORRECTION REQUIRED / documentation-integrity finding;
- correction: M25 added to canonical module index;
- corrected head `0c6caaf9a757cdf689307fecb0f86c9c77cee168` passed Source Pack Integrity SUCCESS;
- no product implementation is present in this planning increment.

## Audit target
Audit Round 25 planning against:
1. Source Hierarchy;
2. accepted ADRs / Decisions Ledger;
3. Scope;
4. Definition of Done;
5. Architecture;
6. Requirements;
7. M01 Production Graph contracts;
8. M22 memory/RAG derived-index behavior;
9. M23 provenance/rights integrity;
10. M24 security/data-class placement;
11. M25 specification.

## Blocking rule
Do not advance to Round 26 while Round 25 requires correction or validation.
Product implementation remains out of this planning increment.

## Next after Round 25 APPROVED
**Round 26 — Observability & Dashboard.**

Expected focus: unified telemetry, project/production health, decision rationale, model/worker/storage/quality/cost/security/provenance views, traces/events/metrics, alerts, drill-down and operator controls without leaking restricted data.

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
