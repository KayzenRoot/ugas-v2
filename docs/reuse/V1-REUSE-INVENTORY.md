# UGAS V1 -> V2 Reuse Inventory

Status: CANDIDATE — UGASV2-WO-0002
Upstream V1 pin: `KayzenRoot/ugas@0169f84248703931bb7578177d9773bce319c14e`
V2 base: `dba55712b50b05388710eb274ed04830858b1023`

## Purpose
This inventory treats UGAS V1 as an upstream evidence and implementation source, never as canonical V2 truth. Promotion into V2 requires provenance, compatibility, license, security, architecture, quality and regression evidence.

## Classification meanings
- `REUSE_AS_IS`: contract/implementation is sufficiently isolated and compatible to transplant after focused verification.
- `REUSE_WITH_ADAPTER`: useful implementation or pattern, but V2 contracts, observability, storage, provider, quality or orchestration boundaries require an adapter.
- `REWRITE`: capability remains valuable, but V2 architecture/quality requirements make direct code reuse unsafe or inefficient.
- `REFERENCE_ONLY`: retain behavior, tests, fixtures or lessons as design evidence; do not promote implementation.
- `RETIRE`: intentionally do not carry forward.

## Qualified inventory
| V1 capability | Provenance at pinned V1 | Classification | V2 target | Promotion notes / quality caveat |
|---|---|---|---|---|
| Provider-neutral generation request/result contract | `src/ugas/generation.py` | REUSE_WITH_ADAPTER | M03, M04, M07-M13 | Preserve deterministic request/result shape and explicit failure. Extend for V2 Scene IR, quality states, model/tool/hardware fingerprints and richer provenance. |
| ComfyUI HTTP adapter | `src/ugas/comfyui_client.py` | REUSE_WITH_ADAPTER | M03, M07-M10, M21 | Useful thin adapter and timeout/error pattern. Must be wrapped behind V2 provider/MCP boundary, health telemetry and artifact lineage. |
| Capability registry and fallback ordering | `src/ugas/capabilities.py` | REUSE_WITH_ADAPTER | M01, M03, M21 | Preserve registry concept and explicit unsupported-capability failure. Replace simple priority with policy-aware multi-objective routing. |
| Model manifest registry | `src/ugas/model_registry.py` | REUSE_WITH_ADAPTER | M03 | Preserve manifest discovery/validation pattern. V2 needs benchmark-backed qualification, license policy, provider/hardware profiles and no silent promotion. |
| Workflow manifest registry | `src/ugas/workflow_registry.py` | REUSE_WITH_ADAPTER | M01, M04, M27 | Preserve deterministic manifest lookup and validation. V2 workflow graph must bind Scene IR, contracts, evidence and repair loops. |
| Provider manifest registry | `src/ugas/provider_registry.py` | REUSE_WITH_ADAPTER | M03, M24 | Preserve provider metadata concept. Add trust/security policy, capability negotiation, cost/latency/quality evidence and selective MCP adapters. |
| Asset registry / asset IDs | `src/ugas/asset_registry.py` | REUSE_WITH_ADAPTER | M05, M25, M28 | Useful storage abstraction and stable asset identity. V2 needs immutable lineage, master/derivative states, cache fabric and delivery contracts. |
| Provenance sidecar and SHA-256 identity | `src/ugas/provenance.py` | REUSE_WITH_ADAPTER | M05, M23, M28 | Strong deterministic primitive. Extend to complete generation lineage, rights/license facts, C2PA path and Quality Court receipts. |
| Persistent identity store | `src/ugas/identity.py` | REUSE_WITH_ADAPTER | M05, M06, M17 | Keep identity/locking/atomic-write ideas. V2 must separate character/brand/asset identity domains and cross-view identity evidence. |
| Job lifecycle/state model | `src/ugas/jobs.py` | REUSE_WITH_ADAPTER | M01, M26, M27 | Preserve explicit state transitions. V2 needs distributed/agent execution, retries, cancellation, evidence pointers and live dashboard events. |
| QA manifest contract | `src/ugas/qa.py` | REFERENCE_ONLY | M19, M20 | Binary pass/fail QA is too coarse for V2. Keep deterministic manifest/testing lessons, replace with specialized Quality Court judges and bounded repair. |
| Observability service/store/dashboard backend | `src/ugas/observability/service.py`, `src/ugas/observability/store.py`, `src/ugas/observability/dashboard_app.py` | REUSE_WITH_ADAPTER | M26 | Reuse telemetry/event/storage patterns where compatible. V2 dashboard is mandatory real-time control plane, so UI/API/event contracts require redesign and broader coverage. |
| Hardware/profile detection and installer patterns | `src/ugas/installer.py`, `src/ugas/profiles.py` | REUSE_WITH_ADAPTER | M02 | Preserve deterministic detection/profile idea. V2 requires benchmark-derived adaptive compute, VRAM/RAM constraints, provider/local routing and continuous health. |
| Context/cache primitives | `src/ugas/context.py` | REUSE_WITH_ADAPTER | M22, M25 | Useful local cache/context pattern. V2 requires multimodal RAG, project/asset memory, invalidation, deduplication and governed context packs. |
| Direction/runtime orchestration | `src/ugas/direction_runtime.py`, `src/ugas/orchestration_runtime_v0247.py` | REFERENCE_ONLY | M01, M04, M27 | Preserve orchestration lessons and tests, not version-stamped monolithic runtime shape. V2 decomposes into contracts, sessions, agents and deterministic tool boundaries. |
| Router | `src/ugas/router.py` | REWRITE | M03, M21 | V1 routing is intentionally small/simple. V2 needs quality/cost/latency/hardware/policy/benchmark-aware routing with fail-closed qualification. |
| Render node execution | `src/ugas/render_node.py` | REUSE_WITH_ADAPTER | M02, M21, M27 | Preserve subprocess isolation/timeout/retry concepts. Add resource leases, telemetry, cancellation, deterministic evidence and heterogeneous compute. |
| Asset revision lineage | `src/ugas/asset_revision.py`, revision-related tests/evidence | REUSE_WITH_ADAPTER | M05, M20, M23 | Preserve parent/revision lineage concept. Integrate immutable master/derivative graph and repair provenance. |
| V1 final capability/evidence matrix | `REVIEW-UGAS-V1-FINAL-ACCEPTANCE.md`, `docs/ugas-v1-capability-matrix.json`, `docs/evidence/v1-final-acceptance/**` | REFERENCE_ONLY | all affected modules | Valuable proof map and regression seed. V1 acceptance does not imply V2 production quality. Revalidate against V2 contracts and quality thresholds. |
| Version-stamped vertical runtimes (`*_v02xx.py`) | `src/ugas/**` | REFERENCE_ONLY | M07-M18, M28 | Mine behaviors, fixtures and failure cases selectively. Do not bulk transplant historical runtime snapshots into V2 architecture. |
| V1 character/creative output acceptance as game-ready proof | V1 media/character evidence and historical acceptance | RETIRE | M05, M06, M07, M09, M10, M19 | CR-001 established that generated output alone is not production proof. Anatomy, limbs, cross-view identity, rig/deformation, motion/contact and runtime evidence are mandatory in V2. |

## Reuse promotion gate
No row above authorizes copying code. A future implementation Work Order promoting a V1 candidate MUST record:
1. exact V1 commit and paths;
2. V2 target contract and owner module/session;
3. license/provenance result;
4. architecture compatibility result;
5. security and data-boundary result;
6. focused regression/benchmark IDs;
7. quality evidence when media/creative behavior is affected;
8. final classification at promotion time, which may become stricter than this inventory.

## Key conclusion
The highest-value V1 inheritance is the deterministic substrate: registries, manifests, provenance, identity, jobs, telemetry, hardware/profile detection and evidence patterns. The lowest-confidence inheritance is final creative quality and monolithic/version-stamped orchestration. V2 should reuse the bones, not inherit the old ceiling.