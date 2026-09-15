# UGAS V2 Section -> Module -> Session Taxonomy

Status: CANDIDATE — UGASV2-WO-0002

## Canonical planning unit
`Section -> Module -> Session -> Capability -> Contract -> Dependency -> Acceptance Criteria -> Test/Benchmark -> Evidence -> Work Order`

A module remains the normative behavior owner already defined in `docs/modules/`. Sections and sessions organize execution without deleting or silently changing module semantics.

## Section map
| Section | Mission | Existing modules |
|---|---|---|
| S01 Production Kernel & Compute | deterministic production OS, adaptive hardware, model routing and shared IR | M01, M02, M03, M04 |
| S02 Asset Identity & Visual Creation | master assets, persistent humans, image/video/motion/3D production | M05, M06, M07, M08, M09, M10 |
| S03 Audio & Narrative | voice, music, sound, story/canon and continuity | M11, M12, M13, M14 |
| S04 Growth, Brand & Localization | faceless content, ads/UGC, brand/IP and localization | M15, M16, M17, M18 |
| S05 Quality, Repair & Economics | acceptance courts, bounded repair and quality/cost cascade | M19, M20, M21 |
| S06 Memory, Trust & Data Fabric | multimodal memory, provenance/rights, security and storage/cache | M22, M23, M24, M25 |
| S07 Operations, Automation & Delivery | real-time control plane, agents/automation and export/delivery | M26, M27, M28 |
| S08 Proprietary R&D | cross-domain candidate technologies and promotion governance | M29 |

All 29 existing modules are mapped exactly once. Cross-module dependencies remain explicit rather than duplicating ownership.

## Session contract
Every implementation session is a bounded convergence unit. A session MUST define:
- `sessionId` and owning module;
- objective and user-visible/system outcome;
- capabilities delivered;
- contracts/schemas touched;
- upstream/downstream dependencies;
- exact source/context pack;
- V1 reuse candidates, if any, with pinned provenance;
- allowed and forbidden paths;
- implementation sequence;
- acceptance criteria;
- A0/A1/A2 tests or benchmarks;
- evidence outputs and proof fingerprints;
- invalidation triggers;
- risk/task class/context radius;
- explicit STOP CONDITION.

## Default session decomposition by section
### S01 Production Kernel & Compute
1. `S01-01 Product taxonomy and production contract` — M01
2. `S01-02 Hardware fingerprint, budgets and adaptive profiles` — M02
3. `S01-03 Model/provider registry and qualification contracts` — M03
4. `S01-04 Multi-objective model director and fallback policy` — M03 + M21 dependency
5. `S01-05 Multimodal IR / Scene IR schema and compiler` — M04
6. `S01-06 Kernel vertical integration and evidence` — M01-M04

### S02 Asset Identity & Visual Creation
1. `S02-01 Asset DNA master/derivative graph` — M05
2. `S02-02 Persistent character identity and reference packs` — M06
3. `S02-03 Image Studio master-first pipeline` — M07
4. `S02-04 Video/Cinema scene and take pipeline` — M08
5. `S02-05 Motion, contact and continuity pipeline` — M09
6. `S02-06 3D geometry, topology, materials and LOD` — M10
7. `S02-07 Rig, skin and deformation integration` — M09 + M10
8. `S02-08 Golden Character Vertical Slice G0-G12` — M05-M10 + M19/M20

### S03 Audio & Narrative
1. `S03-01 Voice identity, synthesis and dialogue contracts` — M11
2. `S03-02 Music composition/stem/master contracts` — M12
3. `S03-03 Sound design and spatial/SFX contracts` — M13
4. `S03-04 Narrative canon, world/character continuity` — M14
5. `S03-05 Audio-narrative synchronization vertical slice` — M11-M14

### S04 Growth, Brand & Localization
1. `S04-01 Faceless channel/content production graph` — M15
2. `S04-02 Advertising and synthetic UGC campaign graph` — M16
3. `S04-03 Brand DNA, IP identity and guardrails` — M17
4. `S04-04 Localization/transcreation contracts` — M18
5. `S04-05 Campaign-to-delivery vertical slice` — M15-M18 + M28

### S05 Quality, Repair & Economics
1. `S05-01 Quality Court common verdict/evidence contract` — M19
2. `S05-02 Specialized media judges and thresholds` — M19
3. `S05-03 Bounded self-correction/repair planner` — M20
4. `S05-04 Render cascade and cost/quality policy` — M21
5. `S05-05 Repair economics and convergence controls` — M19-M21

### S06 Memory, Trust & Data Fabric
1. `S06-01 Multimodal memory/RAG contracts` — M22
2. `S06-02 Provenance, rights and C2PA lineage` — M23
3. `S06-03 Security/restricted-content policy plane` — M24
4. `S06-04 Storage/cache/artifact fabric` — M25
5. `S06-05 Trust-aware retrieval and artifact lifecycle` — M22-M25

### S07 Operations, Automation & Delivery
1. `S07-01 Real-time observability event model` — M26
2. `S07-02 Dashboard shell and live control plane` — M26
3. `S07-03 Agent/automation runtime and permissions` — M27
4. `S07-04 Export/package/delivery contracts` — M28
5. `S07-05 Operator vertical slice from job to delivery` — M26-M28

### S08 Proprietary R&D
1. `S08-01 Candidate technology registry and scoring` — M29
2. `S08-02 Experiment/benchmark sandbox` — M29
3. `S08-03 Promotion/retirement gate` — M29 + affected owner module

## Dependency waves
The section numbers are organizational, not a naive waterfall. Implementation SHOULD converge in dependency waves:
- **Wave A Foundation:** M01, M02, M03, M04, M05, M19, M23, M24, M25, M26.
- **Wave B Core creation:** M06-M14 plus M20-M22.
- **Wave C Product/growth:** M15-M18, M27, M28.
- **Wave D R&D promotion:** M29 candidates only after benchmark evidence and owner-module acceptance.

The dashboard shell/event model is intentionally in Wave A because V2 requires development to be observable through the dashboard as capabilities arrive.

## CR-001 integration
The Golden Character Vertical Slice is not a new module. It is a cross-module acceptance slice owned by S02 and gated by M19/M20. Its G0-G12 stages become session acceptance/benchmark fixtures before visual character pipelines can claim production readiness.

## Planning completeness rule
A module is `PLANNED_FOR_IMPLEMENTATION` only when all of its sessions have capability/contract/dependency/acceptance/test/evidence definitions. A section is `PLANNED_FOR_IMPLEMENTATION` only when every owning module meets that state and cross-module integration sessions have no UNKNOWN critical dependency.