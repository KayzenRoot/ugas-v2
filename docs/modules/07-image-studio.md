# M07 — Image Studio

**Round:** 07  
**Scope class:** CORE / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission
Generate and edit professional still imagery with canonical constraints, selective repair, identity consistency and provenance.

## Responsibilities
- text/image/reference generation
- guided controls
- composition/light/style
- inpainting/outpainting
- retouch/relight/background/object edits
- upscale/restoration
- quality/repair integration

## Planned capabilities
- text-to-image
- image-to-image
- multi-reference guidance
- pose/depth/edge/segmentation controls
- inpaint/outpaint
- background/object replacement
- relighting/color matching
- selective regeneration
- super-resolution
- key art/thumbnail/product/editorial/game assets

## Candidate proprietary technologies
- **Composition Intelligence** — composition analysis/guidance
- **Reference Fusion Engine** — combines references while preserving intent
- **Lighting Reconstruction Engine** — derives/rebuilds lighting structure
- **Semantic Retouch Planner** — plans targeted edits
- **Perceptual Defect Locator** — finds meaningful visual defects
- **Selective Regeneration Masker** — selects minimal image region to regenerate

## Inputs
- Scene/Image IR
- Asset/Character/Brand DNA
- references
- model/hardware plan
- platform specs

## Outputs
- image artifacts
- masks/depth/auxiliary maps
- quality evidence
- edit lineage
- master/variants

## How it works
1. Author image intent in IR with references and DNA constraints.
2. Director selects model/provider and hardware execution plan.
3. Generate draft candidates at economical fidelity.
4. Quality Court evaluates identity, composition, anatomy, artifacts, brand and target constraints.
5. Repair planner creates masks/parameter/provider changes for localized failures.
6. Selected candidate is enhanced/upscaled only as justified and accepted as master.
7. Every edit creates transformation provenance from parent image.

## Canonical data / contracts
- ImageNode spec
- Artifact media metadata
- control/reference links
- Evaluation/RepairPlan

## Dependencies
- M02/M03/M04/M05/M06
- M19 Quality
- M20 Repair
- M21 Render Cascade
- M23 Provenance

## Failure modes and safeguards
- identity/anatomy artifacts → reject/repair
- control ignored → alternate model/control path
- over-editing → parent comparison
- upscale artifacts → re-evaluate

## Observability
- candidate acceptance rate
- repair area %
- quality by model
- cost per accepted image
- edit depth

## Security / rights
- reference rights/provenance checked
- sensitive metadata redacted from public export

## Tests and benchmarks
- golden fixture workflows
- identity/reference consistency
- mask-limited repair
- cross-provider compilation
- quality regression

## Acceptance criteria for first usable V2 path
- [ ] generate, evaluate, selectively repair and approve an image E2E
- [ ] all transformations trace to parent
- [ ] accepted output satisfies configured quality threshold

## Deliberately out of this module
- video temporal logic
- full DCC raster editor replacement

## Evidence expected
Implementation must link requirement IDs, exact SHA, test/benchmark artifacts, metrics, known limitations and proposed checkpoint delta.
