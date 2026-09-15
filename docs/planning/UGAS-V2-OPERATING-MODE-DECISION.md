# UGAS V2 Operating Mode Decision

Status: PROPOSED FOR HEDS APPROVAL
Work Order: UGASV2-WO-0001
Decision owner: Project Brain / GEF
Date: 2026-09-15

## Decision

UGAS V2 SHALL use a hybrid architecture for its engineering/development control plane. It SHALL NOT be implemented as only an MCP server or only a Skill.

The canonical operating model is:

**GEF V1 + HEDS Delta + repository-native governance + deterministic CLI/automation + Skills + selective MCP adapters.**

This mirrors the engineering philosophy used by Hive Coder while adapting it to UGAS V2 media, model, GPU, workflow and asset-quality requirements.

## Roles

### 1. Project Brain / GEF
The Project Brain owns product intent, planning, architecture, source precedence, module/session decomposition, Work Orders, Context Locks, acceptance criteria, test/evidence requirements, risk classification and STOP CONDITION.

The Project Brain compiles intent into bounded executable work. It is the decision layer.

### 2. Codex / executor
Codex is a bounded implementation executor. It receives the smallest sufficient Context Pack and SHALL NOT rediscover product intent, redesign architecture, broaden scope or silently change dependencies/models.

Codex SHALL:
- read only the required context radius unless evidence requires escalation;
- implement only the current Work Order;
- use deterministic tools before exploratory LLM reasoning where possible;
- run the required local assurance gates;
- emit machine-readable evidence;
- stop at the declared STOP CONDITION.

### 3. Repository-native governance
Git is canonical. `.engineering/`, canonical project docs, ADRs, checkpoint, Work Orders, Context Locks, evidence bundles and GitHub checks define durable project truth.

This layer works even when an MCP server, Skill or a specific LLM provider is unavailable.

### 4. Skills layer
Skills SHALL package repeatable high-level procedures and domain playbooks such as:
- Work Order compilation;
- HEDS review;
- V1 reuse assessment;
- image/video/audio/3D pipeline procedures;
- model qualification;
- Quality Court procedures;
- benchmark/evaluation procedures;
- release and evidence procedures.

Skills are procedural knowledge, not the canonical project database and not unrestricted executors.

### 5. MCP adapter layer
MCP SHALL be used selectively when a stable tool/resource boundary materially improves execution, especially for local or external systems such as:
- ComfyUI and media generation backends;
- model registries/providers;
- Blender/3D tooling where appropriate;
- asset catalog and metadata retrieval;
- GPU/hardware telemetry;
- benchmark/evaluation services;
- storage and artifact services;
- other deterministic tool integrations.

MCP is an adapter/tool plane, not the project brain. UGAS V2 MUST NOT depend on one monolithic MCP server for governance or project memory.

### 6. Deterministic CLI/automation layer
Stable repository operations, validation, manifests, schema checks, benchmark launchers, evidence collection and CI-compatible tasks SHOULD be implemented as deterministic scripts/CLIs before being exposed through Skills or MCP.

This creates one testable primitive that can be invoked by humans, Codex, CI, Skills or MCP adapters.

## Why hybrid

Skill-only would be too dependent on prompt/runtime behavior and would provide weak deterministic integration with media/GPU tooling.

MCP-only would centralize too much project intelligence in a tool server, increase coupling, make governance harder to audit and force the executor to perform more discovery.

The hybrid model separates concerns:

`Project Brain -> GEF Work Order -> Context Pack -> Codex -> deterministic CLI/tools -> selective MCP adapters -> Evidence Bundle -> HEDS Delta -> checkpoint/merge`

Skills can assist the Brain or executor at defined boundaries without replacing repository truth.

## Codex minimum-effort contract

Every implementation Work Order SHOULD precompile, where applicable:
- exact objective;
- source precedence;
- base/head identity;
- task class, risk and context radius;
- files to read;
- files allowed to change;
- forbidden paths;
- architecture decisions already made;
- APIs/contracts/schemas;
- dependency/model versions or approved selection policy;
- implementation sequence;
- commands to run;
- acceptance criteria;
- tests/benchmarks;
- expected evidence fields;
- STOP CONDITION.

Codex SHOULD NOT be asked broad prompts such as `implement module X` when the Brain can compile that module into deterministic sessions/Work Orders first.

## Planning hierarchy

UGAS V2 planning SHALL use:

`Section -> Module -> Session -> Capability -> Contract -> Dependency -> Acceptance Criteria -> Test/Benchmark -> Evidence -> Work Order`

Large modules SHALL be compiled into independently reviewable sessions so the executor context remains bounded.

## V1 reuse boundary

UGAS V1 is an upstream reference and reuse source, not canonical V2 truth. Every candidate SHALL be classified as one of:
- REUSE_AS_IS
- REUSE_WITH_ADAPTER
- REWRITE
- REFERENCE_ONLY
- RETIRE

Promotion requires provenance, compatibility, security, architecture, quality and regression evidence. Known V1 quality weaknesses MUST NOT be inherited merely to reduce implementation effort.

## Media-specific rule

For image, video, audio, 3D, animation and digital-human work, successful file generation is not proof of production quality. Work Orders SHALL include target-use quality evidence and applicable Quality Court gates.

## Failure behavior

UNKNOWN is never PASS. If canonical sources conflict, evidence is unavailable, scope must expand, architecture is undecided or a high-risk requirement cannot be proven, execution stops with the corresponding GEF stop state rather than improvising.

## Consequence

UGAS V2 becomes portable across Codex and future executors because project intelligence remains in the repository and GEF contracts. MCP and Skills remain replaceable capability layers rather than single points of architectural dependency.

## Promotion gate

This decision becomes canonical only after exact-head HEDS approval of the governance bootstrap and checkpoint/decision-ledger promotion. Until then it is a proposed decision on the current governance branch.