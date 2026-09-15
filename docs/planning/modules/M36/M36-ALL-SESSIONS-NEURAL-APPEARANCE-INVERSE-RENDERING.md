# M36 — Neural Appearance, Inverse Rendering & Material Intelligence

Status: PLANNING COMPLETE CANDIDATE
Sessions: 15/15

## Mission
Create a next-generation appearance layer that converts pixels/video/captures/generative priors into editable, relightable, physically grounded material and lighting representations, then compiles them into efficient production/runtime forms. M36 complements M07/M10/M30 rather than replacing them.

## 2026 technology signals to qualify through M29
- Neural Material Adapter style workflows: high-fidelity material appearance mapped into efficient analytic BRDF parameterizations.
- Neural Render Proxies: scene-specific differentiable relighting proxies for fast lighting iteration.
- VideoNeuMat-style extraction: reusable neural material knowledge extracted from controlled generative video observations.
- NeuMatEx-style neural materials from multiview images.
- Rich layered/neural material generation beyond basic PBR.
- Neural-initialized progressive differentiable inverse rendering for material/lighting reconstruction.
- Gaussian/splat and hybrid scene representations where appearance capture benefits.
These are candidates/signals, not automatic production dependencies.

## S01 Appearance State Kernel
Define Appearance IR separating geometry, material, lighting, view dependence, uncertainty, provenance and target representation.
Technologies: ASK, AIR, Appearance State Fingerprint.

## S02 Inverse Rendering Intake
Normalize single image, multiview, video, HDR/light-probe and rendered reference observations.
Technologies: IRI, Observation Confidence Envelope, Capture Sufficiency Score.

## S03 Neural-Prior Physical Solver
Use neural predictions as initialization while physically based/differentiable optimization refines editable scene/material parameters.
Technologies: NPPS, Physical Consistency Residual, Neural Prior Trust Map.

## S04 Material Decomposition Intelligence
Recover/estimate albedo, roughness, metallic, normal, displacement/height, opacity/transmission and richer layered appearance when supported.
Technologies: MDI, Channel Ambiguity Graph, Material Evidence Ledger.

## S05 Neural Material Representation
Support richer compact neural appearance for effects basic PBR cannot express well, while retaining an explicit compatibility/fallback path.
Technologies: NMR, Neural Material Capability Descriptor, Appearance Complexity Router.

## S06 Analytic Material Distillation
Distill expensive/neural/high-order appearance into efficient analytic BRDF/BSDF approximations for target runtimes.
Technologies: AMD, Appearance Distillation Error, BRDF Compatibility Compiler.

## S07 Video-to-Material Intelligence
Use controlled generated/captured view-light trajectories as material observations, separating appearance from geometry and illumination where evidence permits.
Technologies: VMI, Virtual Gonioreflectometer, Temporal Material Consistency Court.

## S08 Lighting Reconstruction
Estimate environment/lighting state and uncertainty, then refine it against observations through qualified inverse-rendering routes.
Technologies: LRI, Illumination Evidence Graph, Relighting Consistency Residual.

## S09 Neural Render Proxy Layer
Build qualified scene/light proxies for rapid relighting and image-space lighting optimization before expensive final rendering.
Technologies: NRP-L, Light Transport Proxy Cache, Inverse Lighting Controller.

## S10 Layered Material Synthesis
Generate/author substrate, coating, dust, clearcoat, fuzz, moisture, dirt, age, damage and narrative layers under physical/artistic constraints.
Technologies: LMS, Layer Interaction Graph, Material Story Compiler.

## S11 Cross-Representation Appearance Translation
Translate among neural materials, analytic PBR/BSDF, baked textures and target-engine material graphs while measuring lost appearance dimensions.
Technologies: CAT, Representation Loss Passport, Appearance Round-Trip Test.

## S12 Perceptual Material Optimization
Optimize appearance for actual target camera/resolution/lighting and M10 isometric readability, not close-up material beauty alone.
Technologies: PMO, Screen-Space Material Residual, Perceptual Lobe Budget.

## S13 Hardware & Runtime Appearance Compiler
Choose neural/analytic/baked/hybrid material representation by quality, latency, VRAM, platform support and acceptance evidence.
Technologies: HARC, Appearance Residency Planner, Runtime Material Frontier.

## S14 Appearance Quality Court & Repair
Judge physical plausibility, reference agreement, relightability, channel validity, view dependence, temporal consistency and target-camera readability. Repair only affected appearance dimensions.
Technologies: AQC, Material Causal Defect Router, Appearance Repair Invalidation Matrix.

## S15 Golden Appearance Acceptance
Golden A: single-image material/lighting reconstruction -> editable relighting.
Golden B: multiview/video -> reusable richer neural material.
Golden C: neural/high-order material -> analytic runtime distillation with measured loss.
Golden D: interactive proxy lighting -> final render agreement.
Golden E: premium isometric asset whose material classes remain readable near/mid/far.
Golden F: local material edit proves selective proof invalidation and no unnecessary full rerender/retest.

## Architecture boundaries
M07 owns image production. M10 owns 3D/spatial asset quality and material intent. M30 owns DCC execution/material graph operations. M33 owns studio production. M34 optimizes global execution. M36 owns appearance reconstruction, neural/physical material intelligence, representation translation and relighting intelligence.

## RTX 5050 8GB strategy
Prefer compact proxies, staged inverse-render optimization, tiled material work, cached transport/observations, analytic distillation and selective high-fidelity validation. Neural material/runtime routes must prove memory/performance viability; otherwise compile to analytic/baked forms. Final quality target is not lowered because a representation exceeds local VRAM.

## Technology qualification
Every external 2026 research/model/tool enters via M29 with Golden Shards for reference fidelity, editability, relightability, temporal/view consistency, runtime cost, VRAM, license/provenance, reproducibility and integration complexity.

## Planning STOP CONDITION
All 15 sessions define appearance state, inverse-render intake, neural/physical solving, material decomposition, neural materials, distillation, video extraction, lighting reconstruction, neural proxies, layered synthesis, representation translation, perceptual optimization, runtime compilation, quality/repair and Golden acceptance. Satisfied at planning-candidate level.

## Implementation STOP CONDITION
M36 is implemented only when Golden A-F demonstrate editable physically grounded appearance, controlled relighting, richer-than-basic-PBR capability where justified, efficient runtime distillation, target-camera quality and selective repair/proof reuse.