# WO-S01 Foundation Assembly

Status: READY / S00 PROVEN
Executor: Codex
Authority: repository canon + GEF/HEDS + MODULE-MAP-FROZEN-v1
Approved base: `planning/m01-replan@4392002d324483a77c7909cfd1ec939768ae371e`
Predecessor proof: S00 merged at `71f0f5b95f5b5fe6fb3a1281fcbe97416232828f`

## Mission
Complete the preprogrammed M01-M05 foundation without redesigning UGAS.

## Preconditions
- local checkout synchronized to the exact approved base above, or a later S01-governance-only descendant explicitly recorded before execution
- S00 Evidence Bundle exists at `.engineering/evidence/s00-kernel-sync/S00-KERNEL-SYNC-EVIDENCE.json` and reports the proven kernel contract/fingerprints
- materialized M01-M05 surfaces are present
- clean working tree
- isolated Python 3.14 environment; positive guard that `ugas` resolves to this UGAS V2 checkout

## Required reading
Only `AGENTS.md`, Codex policy, S01 manifest/context pack, this Work Order, S00 evidence/fingerprint, `packages/py/ugas/foundation/**`, prepared M01-M05 targets and directly referenced kernel contracts. Expand context only after recording a concrete unresolved contract. Repository-wide exploration is forbidden by default.

## Allowed implementation scope
- `packages/py/ugas/foundation/**`
- `packages/py/ugas/modules/m01_product_production_os/**`
- `packages/py/ugas/modules/m02_hardware_intelligence/**`
- `packages/py/ugas/modules/m03_model_intelligence/**`
- `packages/py/ugas/modules/m04_multimodal_ir/**`
- `packages/py/ugas/modules/m05_asset_dna/**`
- `.engineering/evidence/s01-foundation/**` for evidence/reproduction tooling

## Do not touch
- `packages/py/ugas/kernel/**`; kernel is a proven predecessor
- M06+
- provider SDK implementations
- dashboard, CI/release policy, model downloads, GPU/ComfyUI/Blender setup
- unrelated tests or broad cleanup

A focused S01 test that proves a kernel incompatibility requires STOP + Correction Request. Do not patch the kernel from this Work Order.

## Execution
1. Verify exact base/clean tree/Python 3.14/V2 source identity and carry forward S00 evidence.
2. A0 for foundation + M01-M05 imports/surfaces.
3. Complete M04 bounded tasks + A1: canonical serialization/validation, locked-path preservation, reference integrity, migration/version/fingerprint boundary.
4. Complete M01 bounded tasks + A1: graph invariants/transitions/cycle rejection, downstream invalidation, proof bridge, idempotent mutation/persistence boundary.
5. Complete M05 bounded tasks + A1: immutable identity, DNA locks, allowed variation, parent/derivative lineage and deterministic fingerprints.
6. Complete M02 bounded tasks + A1: normalized measured hardware/resource envelopes, unknown/degraded semantics, stable fingerprints and bounded lease/resource planning.
7. Complete M03 bounded tasks + A1: qualified model registry/routing, capability residuals, hardware filtering, deterministic rank/tie-break and canonical RouteDecision explanation.
8. Prove the Golden Foundation path: `IRDocument -> ProductionGraph -> AssetDNA -> ResourceEnvelope -> RouteDecision` with fake/in-memory ports only.
9. Run impacted A2 only for Golden Foundation and compatibility bridges actually changed.
10. Run mutation/negative controls for safety-critical S01 invariants where practical: locked-trait mutation, invalid transition/cycle acceptance, unqualified route, unknown hardware coercion, unrelated proof invalidation and duplicate domain effect.
11. Reproduce focused evidence from a clean checkout/isolated environment where practical.
12. Emit exact-head machine Evidence Bundle and report under `.engineering/evidence/s01-foundation/`, open/update PR, and STOP.

## Kernel compatibility
Use kernel Evidence Graph/failure/adapter/observability semantics. Do not duplicate them. If a legacy S01 type conflicts, add the narrowest bridge and focused test inside S01 scope. Kernel changes require STOP and a Correction Request, not silent modification.

## Acceptance
- deterministic canonical serialization/fingerprints; mapping/set/input order cannot alter semantic fingerprints
- invalid IR, broken locked paths/references, illegal transitions and graph cycles rejected
- downstream invalidation limited to causal dependency cone; unaffected siblings/proofs carry forward where kernel fingerprints allow
- idempotency key reuse with a different request fingerprint rejected; committed mutation does not execute twice under sequential replay
- AssetDNA locked traits and canonical identity preserved; derivative points to canonical parent fingerprint
- hardware UNKNOWN/DEGRADED remains explicit and is never silently converted to measured zero/capability
- unqualified model route rejected; insufficient capability/hardware rejected
- model route ranking and tie-break deterministic independent of input order
- canonical `RouteDecision` carries requirements/hardware fingerprints and explanation reason codes
- Golden Foundation slice produces evidence-addressable lineage without provider/network/GPU calls
- no circular imports/provider SDK leakage
- S00 kernel files unchanged and predecessor evidence carried forward unless an explicit dependency fingerprint invalidation is recorded

## Test law
A0 = S01 syntax/import/static only.
A1 = focused unit/contract/service tests for M01-M05/foundation.
A2 = Golden Foundation + changed compatibility bridges only.
A3 = hosted Governance/Source Pack Integrity on the PR.
A4 = HEDS exact-head review.
Do not run a repository-wide suite by default. After a tiny correction rerun the smallest affected scope first.

## Evidence requirements
Comply with `.engineering/gef/GEF-EVIDENCE-SPEC.md`. Record at least: schemaVersion, workOrder, projectFingerprint, baseSha, code/evidence head meaning, taskClass, contextRadius, risk, changedFiles with implementation-vs-evidence scope, decisions, tests with command/status/exitCode, lint/type/build states, security, integration, benchmarks, gates, resolved/open findings, risks, checkpointDelta and stopState. Include S00 carry-forward proof/fingerprint relation, S01 foundation contract fingerprint, exact Python/source identity and remaining CODEX-TASK ids.

## Failure protocol
Classify the smallest failure, fix only its dependency cone and rerun the smallest relevant scope. No full-suite loop after tiny fixes. Policy/quality/capability/integrity failures do not receive blind retry. STALE_STATE requires reconciliation/refetch/new causal state before retry.

## STOP CONDITION
S01 acceptance evidenced or one concrete blocker documented. Never proceed to S02 in this execution. Do not merge the PR. Request HEDS Delta Review of the exact head.
