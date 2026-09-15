# M30 — Session 07: Rigging, Skinning, Deformation & Secondary Physics Automation

Status: PLANNED / IMPLEMENTATION-READY CANDIDATE

## Mission
Automate the conversion of accepted production geometry into a validated deformation system while preserving anatomy, silhouette, identity and runtime constraints.

## Pipeline
Rig Requirement Contract -> Skeleton Route -> Bone/Semantic Mapping -> Skin Bind -> Weight Refinement -> Deformation Pose Suite -> Corrective/Constraint Pass -> Secondary Motion Setup -> Bake/Runtime Preparation -> Quality Court.

## Proprietary technologies
### RRC — Rig Requirement Compiler
Derives required bones, control semantics, attachment points, facial needs, root-motion policy, deformation-critical regions and runtime skeleton constraints from asset/animation recipes.

### SDM — Semantic Deformation Map
Maps topology regions to anatomical/mechanical roles and expected deformation behavior. It links M10 topology requirements with M09 motion and prevents generic skinning from treating every vertex equally.

### DPC — Deformation Pose Court
Runs canonical stress poses for shoulders, elbows, wrists, fingers, spine, hips, knees, ankles, face and asset-specific joints. Judges volume loss, collapse, candy-wrapper twisting, intersections, silhouette damage and material/armor deformation.

### SWR — Skin Weight Repair
Uses causal DPC defects to apply bounded weight/corrective repairs only to affected regions, then re-runs impacted poses.

### SPS-Bridge — Secondary Physics Setup Bridge
Compiles cloth, hair, straps, chains and accessory secondary-motion intent into qualified DCC simulation/constraint operations. Physics output remains deterministic enough for production through pinned parameters/caches where required.

## Neural/automatic rigging
Qualified auto-rig/neural-rig routes may propose skeletons, joints, weights or motion bindings. They remain candidates and must pass RRC/DPC/runtime validation. Provider bone naming never becomes canonical UGAS semantics.

## Evidence
Skeleton manifest, semantic mapping, bind/weights fingerprints, pose-suite renders/metrics, repair history, simulation profile/cache, runtime skeleton/export validation and resource telemetry.

## Golden Shards
Humanoid armor; cloth-heavy humanoid; creature/non-standard limb layout; hard-surface articulated asset; broken skin weights requiring localized repair.

## Acceptance
A representative character can be rigged/skinned headlessly, pass the deformation pose suite, receive bounded repair, configure representative secondary motion and export a validated runtime-ready rig candidate without silently changing the accepted master.