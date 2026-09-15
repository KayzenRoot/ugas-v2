# M10 — Autonomous 3D Factory & Quality Convergence

Status: PLANNED / CANDIDATE

## Purpose
Convert M10 from a collection of 3D capabilities into an autonomous production factory. The factory receives a governed brief and attempts to converge on an accepted runtime asset through bounded generation, DCC execution, evaluation and repair.

## Autonomous loop
1. Normalize brief/canon/target profile.
2. Produce or retrieve reference pack.
3. Generate candidate masters through qualified routes.
4. Run cheap geometry/reference hard gates.
5. Rank surviving candidates.
6. Promote finalist to DCC refinement.
7. Execute topology/UV/material/lookdev/rig-readiness pipeline.
8. Compile target-camera/runtime derivatives.
9. Evaluate in Screen-Space Quality Court.
10. Localize defects to semantic/spatial causes.
11. Apply smallest bounded repair.
12. Re-evaluate invalidated proof only.
13. Stop on acceptance, budget exhaustion, irreducible defect or policy escalation.

## Proprietary technology: AQC — Autonomous Quality Convergence
AQC is the control loop that drives an asset toward its target quality vector without unlimited agent iteration. It uses explicit quality dimensions, defect severity, expected repair gain, cost and remaining budget.

AQC never uses an LLM statement such as `looks good` as acceptance. Acceptance requires machine-readable evidence and configured Quality Court thresholds.

## Proprietary technology: PQR — Perceptual Quality Residual
PQR represents the remaining distance between current artifact and target visual contract across dimensions such as silhouette, anatomy, geometry, material readability, lighting, identity, deformation, runtime fitness and screen-space presentation.

The repair scheduler prioritizes defects with the largest perceptual impact per unit of expected repair cost.

## Proprietary technology: CDR — Causal Defect Router
CDR maps visible symptoms to probable production causes.
Examples:
- weak armor readability -> material contrast / roughness / target lighting / screen-space scale;
- floating feet -> rig/contact/grounding/animation;
- muddy silhouette -> geometry/pose/camera/environment separation;
- texture shimmer -> mip/UV/material/runtime sampling;
- broken elbow -> topology/joint placement/skin weights/deformation;
- environment noise -> procedural density/art hierarchy/lighting/value structure.

It can request diagnostic renders before choosing a repair branch.

## Proprietary technology: MVR — Multi-View Reality Check
MVR prevents a generated asset from being accepted because one view is attractive. It evaluates canonical views, gameplay views, silhouette views, material diagnostics and deformation views and checks cross-view consistency.

## Proprietary technology: APS — Asset Production Score
APS is an explainable composite dashboard score, never a replacement for hard gates. It summarizes:
- master quality;
- runtime quality;
- target-camera quality;
- technical health;
- provenance/reproducibility;
- performance efficiency;
- repair debt.

A beautiful asset with broken topology can have high visual subscore but cannot pass the corresponding hard gate.

## Quality tournaments
Candidate generation uses staged tournaments rather than rendering every candidate at hero fidelity:
- Stage A: cheap reference/silhouette screening.
- Stage B: geometry and identity hard gates.
- Stage C: proxy target-camera comparison.
- Stage D: finalist DCC refinement.
- Stage E: production-quality evaluation.

This prevents expensive GPU/DCC work on candidates already known to be weak.

## Diagnostic render suite
DCC adapters should be able to create standardized renders automatically:
- beauty;
- clay;
- wireframe;
- normals;
- UV checker;
- albedo/base color;
- roughness/metallic;
- silhouette;
- depth;
- contact/grounding;
- target-camera near/mid/far;
- deformation poses;
- runtime-equivalent view.

These outputs are evidence, not presentation decoration.

## 3D-to-screen quality bridge
M10 must explicitly measure both object-space and image-space results. A technically excellent mesh can still fail if its silhouette, material hierarchy or lighting collapses at target distance. Conversely, a clever runtime derivative may reduce invisible detail while preserving or improving perceived quality.

I2P + SDA + DVM + SVQ + MRP + LIS + SSQC form the core perceptual chain.

## Runtime derivative families
One accepted master may produce distinct derivatives:
- cinematic/marketing;
- hero closeup;
- gameplay near;
- gameplay mid;
- gameplay far;
- crowd/NPC;
- web/mobile preview;
- icon/portrait/reference render.

Derivatives inherit master identity and provenance but have independent runtime/perceptual proof.

## Autonomous Blender strategy
Normal production uses headless Blender execution through deterministic Python/API operations and DCC-IR. An MCP adapter may provide higher-level tool access to agents, but all material operations must be logged, bounded and translated into evidence-bearing production actions.

The system should prefer deterministic procedural operations for repeatable tasks and reserve generative/LLM reasoning for ambiguity, art direction, diagnosis and candidate proposal.

## Failure containment
AQC stops and escalates when:
- repeated repair does not reduce PQR;
- defect oscillates between stages;
- budget is exhausted;
- required tool/model is unavailable;
- provenance/license is unacceptable;
- target cannot be achieved on available route;
- repair would require unauthorized canon/art-direction change.

No infinite `agent fixes agent fixes agent` loop.

## Golden character benchmark
A representative humanoid benchmark must include armor/clothing, hands/feet, face/head, asymmetric accessories, material variety, difficult joints, locomotion and target-camera views. Acceptance requires technical and perceptual evidence.

## Golden environment benchmark
A representative environment must include architecture, terrain, props, vegetation/debris, layered materials, focal landmark, traversal corridor, foreground/mid/background hierarchy, target-camera occlusion and representative lighting.

## M26 observability
Dashboard should expose factory stage, current candidate, APS, PQR by dimension, failed gates, repair attempts, GPU/VRAM, DCC operation, model/tool route, estimated acceptance time, proof reuse, artifact lineage and cost.

## M20/M21 integration
M20 consumes CDR/PQR defects to create bounded repair plans. M21 can select alternate qualified routes when the current tool/model has poor expected quality/cost. Route switching cannot weaken hard acceptance criteria.

## M29 integration
M29 Technology Foundry feeds newly qualified 3D, texture, material, rigging, animation, reconstruction and DCC technologies into M10 capability slots. They first compete against the incumbent on Golden Shards. Promotion is evidence-based.

## Final convergence contract
An asset is accepted only when required hard gates pass, PQR is below target thresholds, runtime evidence exists, provenance is valid, no unresolved critical defect remains and the configured acceptance state has been reached.

This closes the distinction between `generated`, `beautiful render`, `master accepted`, and `runtime accepted`.