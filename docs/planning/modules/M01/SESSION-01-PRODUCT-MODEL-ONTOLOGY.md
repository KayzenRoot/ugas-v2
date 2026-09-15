# M01 Replanning — Session 01: Product Model & Production Ontology

Status: DISCUSSED / CANDIDATE
Program: #52

## Decision summary
M01 evolves from a generic production graph into the UGAS Creative Production Kernel. It owns provider-independent production identity, typed graph semantics, lifecycle, recipes, dependency/invalidation semantics and execution-ready planning contracts. It does not own modality-specific generation quality or DCC implementation.

## Product hierarchy
`Workspace -> Project -> Production -> Sequence/Experience -> Scene/Composition -> Shot/Task -> AssetMaster -> Derivative -> Artifact -> Revision -> Run -> Evidence`

Not every production uses every level. The ontology supports film/video, games, advertising, product/menu media, music/audio, faceless content and mixed productions without forcing film terminology onto every domain.

## Core entities
- Workspace: policy, storage, compute and identity boundary.
- Project: durable creative/business objective and shared canon.
- Production: deliverable-oriented graph with budgets, targets and lifecycle.
- ProductionGraph: versioned typed dependency graph.
- ProductionNode: provider-independent unit of intent/work/state.
- AssetMaster: highest-authority reusable creative source for an identity.
- Derivative: purpose/runtime/channel-specific transformation of a master.
- Artifact: immutable produced file/object plus fingerprints.
- Revision: lineage-preserving change to canonical specification or artifact.
- ProductionRecipe: versioned recipe describing how a target class is produced and accepted.
- ExecutionPlan: deterministic set/wave of READY nodes compiled for execution.
- Run: one bounded execution attempt with tool/model/hardware/environment facts.
- Approval: governed acceptance decision.
- EvidenceBundle: machine-readable proof linked to run/node/revision.
- PolicyProfile: quality, hardware, cost, security, rights and delivery constraints.

## Typed node families
Initial families, extensible through versioned schemas:
- INTENT / BRIEF / CANON
- CHARACTER_MASTER / OBJECT_MASTER / ENVIRONMENT_MASTER / BRAND_MASTER
- IMAGE / TEXTURE / MATERIAL / MESH / RIG / ANIMATION / VFX
- SCENE / SHOT / VIDEO_TAKE
- VOICE / DIALOGUE / MUSIC / AUDIO_STEM / SFX
- NARRATIVE / CAMPAIGN / CREATIVE_VARIANT / LOCALIZATION
- RUNTIME_ASSET / PACKAGE / DELIVERY
- EVALUATION / REPAIR / APPROVAL / EVIDENCE

## Master First, Derivative Later
A production recipe may require an accepted master before downstream derivatives become READY. A derivative never silently becomes the canonical master. Character/game-ready paths must be able to enforce CR-001 G0-G12 quality gates through module-owned acceptance contracts.

## Production targets
Every Production and relevant node may declare target profiles:
- quality tier: DRAFT, PREVIEW, PRODUCTION, HERO, CINEMATIC
- runtime class: OFFLINE, REALTIME_DESKTOP, REALTIME_WEB, MOBILE, SOCIAL, PRINT, STREAMING
- visual target/reference profile
- resolution/geometry/texture/audio budgets
- latency and monetary budgets
- local/cloud/hybrid execution policy
- rights/security constraints

`HERO` or `CINEMATIC` is not a claim of AAA equivalence. It selects stricter recipes, evidence and acceptance thresholds.

## AAA-reference strategy
UGAS may use high-end titles and productions as visual-reference targets, but quality claims are benchmark/evidence based. The kernel stores reference profiles and measurable targets; modality modules define the actual geometry/material/lighting/animation/render metrics. This keeps M01 provider and engine neutral while allowing a Path-of-Exile-2-class aspiration to drive stricter downstream recipes.

## Production Recipe contract
A recipe is versioned and immutable after publication. It declares:
- applicable product/category/node types;
- required upstream masters/references;
- required stages and graph template;
- capability/tool classes, never a silently hard-coded provider;
- quality gates and owner modules;
- hardware/cost policy envelopes;
- test/benchmark/evidence requirements;
- derivative/export targets;
- invalidation rules;
- optional repair loops with maximum budgets.

Candidate recipes include `AAA_ISOMETRIC_CHARACTER_MASTER`, `AAA_ISOMETRIC_ENVIRONMENT`, `CINEMATIC_CHARACTER`, `GAME_RUNTIME_CHARACTER`, `PRODUCT_AD`, `SOCIAL_SHORT`, `FACELESS_EPISODE` and `FILM_SHOT`. Names are candidates until their owner modules are replanned.

## State semantics
Minimum node states:
`DRAFT -> SPECIFIED -> READY -> RUNNING -> PRODUCED -> EVALUATING -> ACCEPTED`

Alternate governed transitions:
`EVALUATING -> REPAIR_REQUIRED -> READY`
`EVALUATING -> REJECTED`
`READY/RUNNING -> BLOCKED`
`ACCEPTED -> INVALIDATED` only when a declared dependency/proof input changes.

Acceptance must identify the evaluation/approval evidence. A generated file alone cannot transition to ACCEPTED.

## Dependency and invalidation semantics
Edges are typed: REQUIRES, DERIVES_FROM, REFERENCES, CONSTRAINS, EVALUATED_BY, REPAIRS, PACKAGES, DELIVERS.

Every node fingerprints material inputs. A change invalidates only descendants whose declared dependency/proof inputs intersect the delta. This is the media equivalent of Test Economy and enables incremental creative rebuilds.

## Headless/background execution principle
M01 treats Blender, ComfyUI, encoders, renderers and future DCCs as capability/tool classes behind deterministic adapters. UI presence is never required by the production contract. Tools should support unattended/background execution where the underlying tool permits it. Selective MCP adapters may expose stable operations to agents, but Git contracts and deterministic CLI/Python/tool APIs remain the durable boundary.

## Ownership boundaries
M01 owns production semantics and compilation, not:
- model/provider qualification: M03;
- multimodal/Scene IR: M04;
- Asset DNA details: M05;
- visual generation: M06-M10;
- Quality Court metrics/judges: M19;
- repair algorithms: M20;
- cost/quality routing: M21;
- provenance/rights implementation: M23;
- storage/cache: M25;
- dashboard UI: M26;
- agent execution: M27;
- delivery adapters: M28.

A future DCC/3D Automation module and Real-Time Rendering/Engine Integration module are explicit gap-analysis candidates and must be decided during module replanning rather than hidden inside M01.

## Session 01 acceptance
- ontology covers all current multimodal product families without provider coupling;
- master vs derivative is explicit;
- immutable artifact/run/evidence lineage is explicit;
- quality/runtime/hardware/cost targets can be represented without M01 owning modality metrics;
- graph state cannot accept an unevaluated artifact;
- background/headless tool execution is architecturally supported;
- invalidation semantics support narrow rebuild/proof reuse;
- module ownership boundaries prevent M01 becoming a monolith.

## Next M01 session
Session 02: Production Graph 2.0, typed edges, fingerprints, invalidation engine, graph partitions and scale strategy.