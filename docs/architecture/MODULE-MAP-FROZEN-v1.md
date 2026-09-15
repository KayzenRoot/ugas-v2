# UGAS V2 Module Map Frozen v1

Status: FROZEN FOR IMPLEMENTATION PREPARATION
Scope: M01-M40
Branch: planning/m01-replan
Date: 2026-09-15

## Freeze decision
The two transversal architecture audits found no independent capability gap that justifies M41+ before implementation. M01-M40 therefore becomes the canonical module map for the first implementation program.

Freeze does not mean immutable forever. A new module requires an Architecture Change Record proving: independent ownership, contracts not naturally owned by an existing module, material product/operational value, dependency impact, migration path and acceptance/evidence plan. New technology alone is not a reason for a module; it enters through M29 Technology Foundry.

## Cross-cutting kernel required by all shards
- canonical project/subject/fingerprint primitives
- command/event/failure envelopes
- unified Evidence Graph and causal proof invalidation
- version-specific Adapter Qualification registry
- failure taxonomy and observability correlation
- project isolation, provenance, rights/security and evidence are fail-closed boundaries

## Canonical implementation bands
Foundation M01-M05; Core Media M06-M10; Audio/Narrative M11-M14; Content/Brand M15-M18; Quality/Repair/Economics M19-M21; Platform Trust M22-M25; Control/Agents/Delivery M26-M28; Technology/DCC M29-M30; Creative/World/Studio M31-M33; Optimization/Experience/Appearance M34-M36; Runtime M37; Dataset/Eval/Training M38; Extension SDK M39; Distributed Fabric M40.

## Implementation law
Codex receives bounded shards, explicit READ/MODIFY/CREATE/DO-NOT-TOUCH manifests, contracts, acceptance criteria, focused tests and evidence requirements. Repository-wide exploration is not the default. Test what changed, reuse what did not, invalidate only the causal dependency cone.

## STOP CONDITION
The module map remains frozen until an Architecture Change Record is accepted. Next work is implementation-readiness closure: kernel tests, compatibility bridges, final shard manifests/context packs/work orders, exact-head review and then Codex materialization/implementation.
