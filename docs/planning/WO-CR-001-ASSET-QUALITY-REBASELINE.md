# WO-CR-001 — UGAS V2 Asset Quality Rebaseline

**Change request:** #46  
**Risk:** STANDARD planning change; implementation remains blocked  
**Status:** ACTIVE / PLANNING

## OBJECTIVE
Rebaseline UGAS V2 before product implementation so character and game-asset quality is validated at final-use context, with anatomy, consistency, rigging, deformation and engine-oriented acceptance evidence.

## CONTEXT
UGAS V1 is complete, but production feedback found unacceptable quality failures: malformed legs/anatomy, visually weak generated characters/assets, and a gap between attractive concept generation and assets that remain good when used in a game-like runtime. Existing V2 planning already contains Model Intelligence, Asset DNA, Digital Humans, Image, Motion, 3D, Quality Court and Repair, but the requirements are too broad to guarantee a high-quality game-ready character path.

## SCOPE
- audit M03/M05/M06/M07/M09/M10/M19/M20 against the reported V1 failures;
- define a Character/Asset Quality Contract with measurable gates;
- define anatomy, proportion, pose, limb/hand/foot, silhouette and artifact checks;
- define multi-view/turnaround consistency requirements;
- define 2D-to-3D identity preservation and geometry/topology acceptance;
- define skeleton, skinning, joint placement, deformation, foot/contact and locomotion checks;
- define engine-import/runtime presentation verification without making the core engine-dependent;
- define model-family benchmark protocol and drift/version policy;
- define Golden Character Vertical Slice as the first implementation path after this rebaseline is APPROVED;
- update canonical requirements, benchmarks, DoD and affected module specs only after audit supports the change.

## OUT OF SCOPE
- production code implementation;
- replacing accepted ADRs without explicit supersession;
- locking UGAS V2 to one model/provider/game engine;
- broad cleanup unrelated to asset quality;
- full MMORPG/game implementation.

## FILES/SOURCES TO READ
1. `docs/checkpoint/CURRENT.md`
2. `docs/decisions/DECISIONS-LEDGER.md`
3. `docs/SCOPE.md`
4. `docs/DEFINITION-OF-DONE.md`
5. `docs/ARCHITECTURE.md`
6. `docs/REQUIREMENTS.md`
7. `docs/adr/ADR-0003-provider-independent-core.md`
8. `docs/adr/ADR-0004-hardware-agnostic-adaptive-compute.md`
9. `docs/adr/ADR-0007-dna-persistent-identity.md`
10. `docs/adr/ADR-0008-quality-before-acceptance.md`
11. `docs/adr/ADR-0009-minimal-repair-lineage.md`
12. `docs/modules/03-model-intelligence-multi-model-director.md`
13. `docs/modules/05-asset-dna-2-0.md`
14. `docs/modules/06-digital-humans-persistent-identity.md`
15. `docs/modules/07-image-studio.md`
16. `docs/modules/09-animation-motion.md`
17. `docs/modules/10-3d-spatial.md`
18. `docs/modules/19-quality-court.md`
19. `docs/modules/20-self-correction-repair.md`
20. `docs/TEST-BENCHMARK-PLAN.md`

## REQUIREMENTS
- Generated != accepted remains mandatory.
- A character cannot be promoted to game-ready on a single beauty image.
- High-quality character promotion SHALL require representative orthographic/turnaround evidence or equivalent structured multi-view evidence.
- Anatomy/proportion/limb topology and obvious generation defects SHALL be independently evaluated from aesthetic preference.
- Rigged characters SHALL be validated for skeleton hierarchy, joint placement, skinning and representative deformation poses.
- Locomotion SHALL validate feet/ground contact, sliding, knee/hip behavior and loop continuity where applicable.
- 3D outputs SHALL validate geometry/topology, UV/material/PBR and target-profile budgets before delivery.
- Final acceptance SHALL include target-context verification, including an engine/runtime smoke path for game assets.
- Model routing SHALL use empirical benchmark evidence and version pinning; newer model versions SHALL not auto-promote without regression evidence.
- Repair SHALL target localized defects when safe and SHALL re-run all affected gates.

## ARCHITECTURE RULES
- Preserve provider-independent core and hardware-agnostic adaptive compute.
- Preserve Production Graph, Multimodal IR and Asset/Character DNA authority.
- Add specialized evaluators behind versioned contracts rather than embedding one vendor/model into domain logic.
- Treat game engines/DCCs as adapters/verification targets, not canonical creative intent.
- Preserve lineage for every generation, repair, rig, retopo, texture, LOD and export transformation.

## CONSTRAINTS
- Local-first, not local-only.
- Current known local target includes 8 GB VRAM-class hardware; heavy models may require quantization/offload/remote burst and must degrade explicitly rather than silently lowering quality.
- Quality is prioritized over accepting cheap/fast outputs.
- No unsupported claim that a named model is universally best.

## CONTEXT LOCK
- base SHA: `8a7807848f79cacbb8cf3d0df9c46c489a0cbfec`
- checkpoint fingerprint: `fcd9c3230fa1aad11263e3f069c4fefaece3beaa`
- source hierarchy fingerprint: `a0860cc9ca0b3be198bf9daf09b53a358ee95ea5`
- requirements fingerprint: `9cad25445ad378871dfbf8d1b80060e008075b2a`
- M05 fingerprint: `dbcd87ece9c9a7d5ee21bbe7882eb10d3c2ba500`
- M06 fingerprint: `50f6d0c06d1057561724f0db33b63ad10b4c3db5`
- M07 fingerprint: `b605b21776630207baead6e6adb7b18b7f807dbf`
- M09 fingerprint: `6ec3f233657bb2003724e5a2e95f350c155210b4`
- M10 fingerprint: `828f703bf3420c018b97a285f7f4c1322c2e220e`
- ADR-0008 fingerprint: `c64d5afe753a9495b776ca9fc55b8af0ca5f43ac`

## PREFLIGHT
- reconcile branch base with `main`;
- verify no newer accepted checkpoint/ADR changes the quality architecture;
- inventory all existing quality/anatomy/rigging/engine-import language before adding duplicates;
- record external model/tool research as candidates, not commitments;
- identify which proposed changes are NECESSARY vs IMPORTANT/FUTURE.

## ACCEPTANCE CRITERIA
- [ ] root causes from V1 feedback are mapped to missing/weak V2 controls;
- [ ] Character/Asset Quality Contract is specified with objective gates and evidence;
- [ ] affected module deltas are explicit and non-duplicative;
- [ ] benchmark matrix covers at least concept image, multi-view identity, anatomy, 3D geometry, rig/deformation and in-engine verification;
- [ ] first implementation vertical slice is narrow enough to test end-to-end quality before broad feature development;
- [ ] no accepted architectural decision is silently overwritten;
- [ ] audit finds no HIGH/CRITICAL planning defect.

## TESTS
Planning validation:
- source-pack integrity;
- requirement traceability review;
- contradiction/duplication audit;
- benchmark reproducibility review;
- hardware-envelope review for 8 GB VRAM-class local operation and explicit higher-compute tiers.

## DELIVERABLES
- rebaseline findings document;
- Character/Asset Quality Contract;
- canonical deltas to Requirements / DoD / Test Benchmark Plan / affected modules;
- model/tool candidate benchmark matrix;
- Golden Character Vertical Slice implementation Work Order proposal;
- Evidence Bundle and Checkpoint Delta proposal.

## EVIDENCE BUNDLE
Must include base/head SHA, files changed, requirement/ADR mapping, external research sources and dates, contradiction audit, checks run, risks/limitations and proposed checkpoint delta.

## REVIEW FORMAT
Verdict in Brazilian Portuguese: `APPROVED`, `CORRECTION REQUIRED` or `BLOCKED`, with findings by severity and exact source references.

## CHECKPOINT DELTA PROPOSAL
Only after audit approval: record CR-001 as approved rebaseline, update the next necessary increment from generic Round 30 R&D planning to the approved quality-first implementation/planning sequence, and preserve the prior Round 29 history.

## STOP CONDITION
Stop after the rebaseline documentation and audit are complete. Do not start production implementation until the rebaseline is APPROVED and a separate implementation Work Order is active.
