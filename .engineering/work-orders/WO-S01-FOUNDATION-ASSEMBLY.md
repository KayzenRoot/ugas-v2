# WO-S01 Foundation Assembly

Status: PREPARED / EXECUTE ONLY AFTER S00 PROVEN
Executor: Codex
Authority: repository canon + GEF/HEDS + MODULE-MAP-FROZEN-v1

## Mission
Complete the preprogrammed M01-M05 foundation without redesigning UGAS.

## Preconditions
- local checkout synchronized to exact approved HEAD
- S00 Evidence Bundle reports kernel A1 green and contract fingerprint
- materializers completed successfully if generated surfaces are absent
- clean working tree

## Required reading
Only S01 manifest/context pack, S00 evidence/fingerprint, prepared M01-M05 targets and directly referenced kernel contracts. Expand context only after recording a concrete unresolved contract.

## Execution
1. A0 for M01-M05 imports/surfaces.
2. Complete M04 bounded tasks + A1.
3. Complete M01 bounded tasks + A1.
4. Complete M05 bounded tasks + A1.
5. Complete M02 bounded tasks + A1.
6. Complete M03 bounded tasks + A1.
7. Prove `IRDocument -> ProductionGraph -> AssetDNA -> ResourceEnvelope -> RouteDecision`.
8. Run impacted A2 only.
9. Emit exact-head Evidence Bundle and STOP.

## Kernel compatibility
Use kernel Evidence Graph/failure/adapter/observability semantics. Do not duplicate them. If a legacy S01 type conflicts, add the narrowest bridge and focused test. Kernel changes require STOP and a Correction Request, not silent modification.

## Acceptance
Deterministic canonical fingerprints; invalid IR/transitions/cycles rejected; DNA locks preserved; unknown hardware explicit; unqualified model route rejected; deterministic route tie-break; no circular imports/provider SDK leakage; proof invalidation limited to causal delta.

## Failure protocol
Classify the smallest failure, fix only its dependency cone and rerun the smallest relevant scope. No full-suite loop after tiny fixes.

## STOP CONDITION
S01 acceptance evidenced or one concrete blocker documented. Never proceed to S02 in this execution.
