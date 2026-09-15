# M30 — Session 10: Golden Factory Acceptance & Implementation Handoff

Status: PLANNED / MODULE PLANNING COMPLETE CANDIDATE

## Mission
Close M30 planning with an executable acceptance program proving that UGAS can autonomously drive DCC production from governed intent to validated runtime asset.

## Golden Factory Slice A — Character
Governed brief/reference -> neural/procedural/manual-source candidate -> NDB -> DCC-IR -> Blender headless -> geometry conditioning -> retopo -> UV -> bake -> materials -> rig/skin -> deformation -> representative motion -> runtime derivatives -> export/re-import -> Quality Court -> bounded repair -> RUNTIME_ACCEPTED.

Required evidence includes editable master, provenance, transaction logs, GHP, topology/UV/bake/material reports, rig/deformation proof, target-camera views, runtime derivative evidence, RVS and resource/cost telemetry.

## Golden Factory Slice B — Environment
Governed composition -> authored anchors -> PAC/CPG procedural assembly -> Blender headless -> geometry/material refinement -> semantic-zone validation -> lighting/camera diagnostics -> runtime chunk/LOD/instance preparation -> export/re-import -> integrated target-camera Quality Court -> repair -> RUNTIME_ACCEPTED.

## Golden Factory Slice C — Failure & Recovery
Force representative failures: Blender crash mid-transaction, VRAM pressure, broken neural mesh, invalid UV/bake, deformation failure and runtime export drift. System must recover/checkpoint/rollback, classify causally and avoid corrupting accepted masters.

## Golden Factory Slice D — Delta Economy
Start from an accepted asset and make localized changes to material, topology region and procedural density separately. Demonstrate SFD/PGD/RIM proof invalidation and carry-forward. Unaffected expensive proofs must not rerun without a justified dependency reason.

## M30 acceptance gates
1. DCC-IR schema validates and capability negotiation works.
2. STE transactions are staged, fingerprinted and rollback-capable.
3. Blender headless worker is isolated, observable and recoverable.
4. PAC produces reproducible constrained procedural assets.
5. NDB ingests heterogeneous neural spatial candidates without treating them as automatically production-ready.
6. Retopo/UV/bake/material pipeline produces validated production derivatives.
7. Rig/skin/deformation/secondary-motion automation passes representative stress tests.
8. Runtime compiler creates target-specific derivatives and EIV catches export/import drift.
9. DCC Quality Court can causally diagnose and selectively repair defects.
10. M26 exposes live production/quality/resource state.
11. M20 repair and M21 route/cost decisions cannot weaken hard acceptance criteria.
12. M29 can qualify a new DCC/neural technology through the adapter/capability boundary without redesigning M30.
13. RTX 5050 8GB local profile has measured supported routes and explicit offload/fallback routes for workloads outside the local envelope.
14. Character and environment Golden Factory slices reach RUNTIME_ACCEPTED with evidence.

## Implementation waves
W1 schemas/contracts: DCC-IR, capability manifest, transaction/evidence schemas.
W2 Blender adapter + BWE + STE + headless Golden Shard.
W3 GHP/diagnostics/observability/recovery.
W4 PAC/Geometry Nodes library + semantic constraints.
W5 NDB/RIQ/NGC/MTF/VCC provider-neutral bridge.
W6 retopo/UV/bake/material compiler and courts.
W7 rig/skin/deformation/secondary-motion automation.
W8 runtime compiler/LOD/export-import/RVS.
W9 DQD/CDR-DCC/RIM/AQC-DCC repair convergence.
W10 Golden Character + Golden Environment + Failure/Recovery + Delta Economy acceptance.

## Codex execution policy
Codex receives bounded Work Orders and minimum Context Packs. It does not rediscover architecture, choose product scope or silently change acceptance policy. Local implementation/testing should use the assurance ladder: A0 edit/static, A1 focused unit/contract, A2 impacted integration/Golden Shards, A3 promotion CI, A4 HEDS delta review. No full-suite rerun loop after every small fix.

## Technology evolution
Blender is first DCC adapter, not the permanent architecture. Neural 3D models, retopology systems, rigging models, texture/material generators, reconstruction systems, add-ons and MCP adapters enter through M29 qualification. New technology must compete on Golden Shards for quality, reliability, cost, hardware, license/provenance and integration complexity before becoming routable.

## M30 planning STOP CONDITION
Planning is complete when Sessions 01-10 jointly specify foundation, DCC-IR, execution, procedural compilation, neural bridge, production geometry/materials, rig/deformation, runtime compilation, quality/repair/observability and end-to-end Golden Factory acceptance.

This condition is now satisfied at planning-candidate level. Canonical promotion still requires governed review/HEDS.

## M30 implementation STOP CONDITION
Implementation is not complete until required Golden Factory slices reach their acceptance states with reproducible evidence and failure/recovery + delta-economy tests pass. A successful Blender render alone is never M30 completion.