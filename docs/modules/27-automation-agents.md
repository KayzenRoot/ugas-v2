# M27 — Automation & Agents

**Round:** 27  
**Scope class:** CORE FOUNDATION / NECESSARY  
**Status:** PLANNED / NOT IMPLEMENTED

## Mission

Provide UGAS V2 with a governed automation layer that can run deterministic workflows, scheduled/event-driven jobs and bounded adaptive agents without granting opaque autonomy or bypassing canonical Production Graph, security, approval, quality, cost, provenance and observability rules.

M27 exists to automate production, not to create a second authority system. Every automated action remains a normal governed action executed through canonical contracts.

## Core principles

1. **Deterministic first.** If a task can be represented safely as a workflow/state machine, prefer that over an open-ended agent.
2. **Agents by necessity.** Use adaptive reasoning only when the task genuinely benefits from planning, ambiguity resolution or dynamic tool selection.
3. **No ambient authority.** Every automation/agent receives an explicit capability envelope from M24.
4. **Goals are bounded.** Goal, scope, budget, stop conditions and approval policy are mandatory agent context.
5. **Human control remains first-class.** Pause, cancel, resume, override and approval are canonical operations.
6. **State lives outside chat.** Long-running automation state is persisted in governed system storage and Production Graph records.
7. **Schedules/triggers are inputs, not permission.** A timer/event can request work but cannot grant capability.
8. **Retries are governed.** Idempotency, duplicate suppression, backoff, compensation and replay are explicit.
9. **Agents cannot rewrite governance.** Accepted ADRs, Scope, DoD, policies and rights records cannot be silently modified by agent reasoning.
10. **Observability is mandatory.** Significant automated decisions, tool calls, approvals and state transitions expose M26-compatible evidence.
11. **Quality/security remain upstream gates.** Automation does not bypass M19, M23 or M24.
12. **Provider independence.** Agent/model runtimes are replaceable behind contracts.

---

## Automation classes

### Deterministic Workflow
A versioned DAG/state machine whose transitions and tool calls are fully declared.

Examples:
- ingest reference → analyze → generate preview → quality check → repair → approve;
- batch localization;
- render cascade;
- backup/scrub jobs;
- publish preparation.

### Scheduled Workflow
Deterministic workflow started by a schedule/calendar/cron-like trigger.

### Event-Driven Workflow
Workflow started by a typed system event, webhook, file arrival, Production Graph transition or operator action.

### Guarded Agent Task
A reasoning-capable agent receives a bounded objective and may choose among pre-authorized tools/workflows while remaining inside capability/budget/approval boundaries.

### Multi-Agent Workflow
Multiple specialized agents collaborate through explicit contracts and message/state channels. Shared state and permissions are explicit; agents do not infer authority from each other.

### Human-in-the-Loop Workflow
Automation pauses at defined gates for operator review/selection/approval.

---

## Canonical execution model

Every automation execution should resolve to:

1. trigger/request;
2. authorization/context compilation;
3. workflow/agent plan selection;
4. budget and stop-condition binding;
5. deterministic and/or adaptive execution;
6. tool calls through canonical APIs;
7. quality/security/provenance checks;
8. approval gates if required;
9. result publication into Production Graph;
10. evidence and telemetry;
11. terminal state or governed retry/recovery.

## Workflow state model

Suggested states:
- `PENDING`
- `READY`
- `RUNNING`
- `WAITING_APPROVAL`
- `WAITING_DEPENDENCY`
- `PAUSED`
- `RETRY_WAIT`
- `COMPENSATING`
- `SUCCEEDED`
- `FAILED`
- `CANCELLED`
- `BLOCKED`
- `UNKNOWN`

State transitions must be auditable and idempotent where feasible.

## Agent execution envelope

Each agent invocation should bind:
- agent/workflow definition version;
- objective;
- allowed scope/entities;
- input references;
- capabilities/tools;
- security/data classification;
- model routing policy;
- compute budget;
- monetary/token budget where applicable;
- storage budget;
- time/deadline budget;
- maximum steps/tool calls;
- approval policy;
- quality threshold;
- stop conditions;
- escalation rules;
- correlation/trace IDs.

No field may be silently widened by the model.

---

## Deterministic vs agent decision

M27 should include an **Agent Necessity Gate** that asks:

1. Is the task fully describable as deterministic steps?
2. Are all decisions reducible to explicit rules/thresholds?
3. Does dynamic reasoning materially improve success probability or flexibility?
4. Is the extra uncertainty/cost/security surface justified?
5. Can a bounded agent be inserted into only the ambiguous substep rather than owning the entire workflow?

Preferred pattern:

`deterministic shell → bounded agent subtask → deterministic validation/gates`

This limits agentic entropy while preserving useful reasoning.

---

## Trigger system

Supported planning concepts:
- manual trigger;
- schedule;
- Production Graph state event;
- file/object arrival;
- model/provider availability event;
- quality failure;
- storage pressure event;
- security incident/event;
- external webhook/integration event;
- queue message;
- threshold/condition event.

Triggers carry identity, payload fingerprint, source trust and correlation metadata.

Duplicate trigger detection must prevent accidental double execution.

---

## Tool use

Agents and workflows interact with:
- production/domain APIs;
- model providers;
- local/remote workers;
- storage;
- quality court;
- provenance/rights;
- publishing/export adapters;
- external services/plugins.

All tool calls must pass M24 authorization and security context.

A tool response cannot grant additional capabilities.

## Approval gates

Potential approval modes:
- none required;
- operator confirmation;
- two-step approval;
- role/capability-specific approval;
- conditional approval based on risk/cost/security;
- release/publish approval;
- destructive-action approval.

Approval records are canonical evidence and can expire/revoke.

---

## Idempotency and duplicate protection

Automation can fail catastrophically if retries duplicate external side effects. M27 therefore requires:
- idempotency intent keys;
- request fingerprints;
- external-action receipts;
- last-known outcome lookup;
- duplicate trigger suppression;
- retry policy per action class;
- explicit non-idempotent action handling.

Examples requiring special care:
- publication;
- billing/provider purchase;
- remote deletion;
- sending notifications/messages;
- exporting/releasing final artifacts;
- creating external campaigns.

---

## Retry and recovery

Retry policy dimensions:
- retryable error class;
- maximum attempts;
- exponential/linear/custom backoff;
- jitter;
- provider/model fallback;
- worker migration;
- local repair vs full rerun;
- approval revalidation;
- budget remaining;
- deadline remaining.

Retries must preserve lineage and attempt identity.

## Compensation

When side effects cannot be rolled back transactionally, M27 uses explicit compensation workflows.

Examples:
- revert external configuration;
- delete temporary publication;
- restore previous asset pointer;
- release a reserved resource;
- undo staging state.

Compensation itself is governed and auditable.

---

## Human control plane

Operators must be able to:
- see active automations;
- inspect current state/step;
- see what is waiting and why;
- pause;
- cancel;
- resume;
- approve/reject;
- retry from safe checkpoint;
- override a recommendation;
- reduce budgets/capabilities;
- inspect evidence/rationale;
- quarantine an automation definition.

Emergency stop should be available at workflow/project/system level where feasible.

---

## Memory integration with M22

Agent memory must be explicit by class:
- execution-local scratch memory;
- workflow state;
- project memory retrieval;
- approved outcome memory;
- failure memory;
- operator preference memory.

Agents cannot treat chat history as canonical memory.

Memory reads inherit project/security context. Memory writes require declared policy and must distinguish observations from accepted facts.

---

## Production Graph integration with M01

Automation definitions and executions should integrate as governed graph entities.

Potential entities:
- AutomationDefinition;
- WorkflowDefinition;
- WorkflowRun;
- AgentDefinition;
- AgentRun;
- StepRun;
- TriggerEvent;
- ApprovalGate;
- ToolInvocation;
- CompensationRun;
- AutomationEvidence.

Automation may create/advance Production Graph nodes only through normal contracts.

---

## Model/compute integration

### M03
- route reasoning tasks to appropriate model/provider;
- maintain agent-task/model affinity evidence;
- fallback on model/provider failure;
- record routing rationale.

### M02
- select local/remote compute for tool/model jobs;
- respect hardware constraints and budgets.

Agent orchestration itself should remain lightweight and not force expensive models for deterministic bookkeeping.

---

## Quality integration with M19/M20

Automation-generated outputs are not accepted automatically.

Workflows can:
- request Quality Court evaluation;
- branch based on quality result;
- invoke minimal repair;
- escalate to human review;
- terminate after quality budget is exhausted.

An agent cannot self-declare its media output accepted without the required gates.

---

## Cost integration with M21

Each automation can define:
- total budget;
- per-step budget;
- model/provider budget;
- retry budget;
- deadline;
- maximum quality escalation tier.

Budget exhaustion may:
- pause for approval;
- degrade to a cheaper allowed path;
- terminate as BLOCKED/FAILED;
- never silently exceed policy.

---

## Storage integration with M25

Automation state, evidence and artifacts follow M25 storage classes and retention semantics.

Large scratch/intermediate data should be marked rebuildable/TEMP/CACHE when appropriate.

Automations under storage pressure may be paused or replanned before creating unsafe amplification.

---

## Security integration with M24

Hard rules:
- agent capabilities are explicit and scoped;
- no tool/capability escalation from prompts or model output;
- sensitive/restricted data follows M24 placement/egress rules;
- high-risk/destructive actions require matching policy/approval;
- external content is untrusted input;
- plugins/workers/providers must be security-compatible;
- secret access uses references/scoped leases;
- agent-generated shell/code/tool parameters remain untrusted until contract validation.

---

## Observability integration with M26

Expose at least:
- active/scheduled automation counts;
- run state distribution;
- queue/wait time;
- step duration;
- retries/backoff;
- agent step/tool count;
- model/provider decisions;
- budget consumption;
- approval wait time;
- operator interventions;
- failures by class;
- duplicate-trigger suppression;
- compensation activity;
- capability/approval denials;
- outcome quality;
- cost per successful automation;
- evidence/rationale links.

Every major agent decision should expose a Decision Explainability Envelope or equivalent contract.

---

## Multi-agent architecture

Multi-agent systems are allowed only when specialization provides measurable value over one bounded agent or deterministic workflow.

Each agent has:
- role;
- explicit inputs/outputs;
- capability scope;
- budget;
- contract/schema;
- stop conditions.

Agent-to-agent messages do not transfer privileges.

A coordinator is not a superuser; it only owns orchestration capabilities explicitly granted.

---

## Candidate proprietary technologies

### Workflow Determinism Compiler — WDC
Converts declarative production intent into the maximum deterministic workflow possible, identifying only the substeps that genuinely require adaptive reasoning.

### Agent Necessity Gate — ANG
Scores whether agentic execution is justified versus a deterministic workflow using ambiguity, branching complexity, expected value, risk and cost.

### Capability-Bound Agent Envelope — CBAE
Runtime envelope cryptographically/logically binding an agent to explicit goal, scope, tools, data classes, budgets and approval policy.

### Autonomy Budget Ledger — ABL
Tracks how much open-ended decision latitude, tool usage, cost and step budget an agent has consumed and can still exercise.

### Goal-to-Graph Compiler — GGC
Compiles bounded high-level objectives into Production Graph/workflow tasks without granting execution authority beyond canonical contracts.

### Human Control Plane — HCP
Unified pause/cancel/resume/approve/override/escalate layer for all workflows and agents.

### Approval Path Synthesizer — APS
Computes required approval gates from action consequence, security classification, cost, rights and publication state.

### Idempotency Intent Key — IIK
Canonical fingerprint representing one intended external side effect so retries/duplicate triggers do not execute it twice.

### Compensation Graph Engine — CGE
Models side-effect compensation as an explicit dependency graph rather than ad-hoc rollback code.

### Agent Drift Sentinel — ADS
Detects when an agent's actions/plans diverge materially from objective, constraints, policy or expected workflow boundary.

### Tool Consequence Forecaster — TCF
Predicts likely side effects/risk class of a proposed tool call before execution to choose approval/sandbox/deny behavior.

### Multi-Agent Contract Bus — MACB
Typed collaboration fabric for specialist agents that preserves data, schema, lineage and capability boundaries.

### Stop Condition Engine — SCE
Evaluates success, budget, time, quality, risk, repetition and stagnation signals to terminate or escalate an agent deliberately.

### Automation Replay Ledger — ARL
Records deterministic replay/audit information for workflow/agent runs without pretending nondeterministic model reasoning can be perfectly reproduced.

### Recovery-Oriented Orchestrator — ROO
Plans execution around resumability, checkpoints, idempotency and compensation instead of treating recovery as an afterthought.

> All candidate proprietary technologies remain R&D hypotheses until prior-art research, benchmark comparison and explicit validation.

---

## Canonical contracts

### AutomationDefinition
- stable ID/version;
- class;
- trigger definitions;
- workflow/agent definition reference;
- default security context/policy references;
- budgets;
- approval policy;
- retry/recovery policy;
- enabled/disabled state.

### WorkflowDefinition
- nodes/steps;
- dependencies;
- inputs/outputs;
- deterministic conditions;
- tool/API contracts;
- compensation mapping;
- checkpoint policy.

### AgentDefinition
- role/purpose;
- permitted task classes;
- tool/capability profile;
- model-routing policy;
- default budgets;
- memory policy;
- stop-condition policy.

### AutomationRun
- run ID;
- definition/version;
- trigger fingerprint;
- actor/requester;
- security context;
- state;
- current step;
- budget consumption;
- approvals;
- attempts;
- evidence references.

### AgentRun
- objective;
- scope;
- model/provider selections;
- tool invocations;
- step/decision log references;
- memory references;
- budget state;
- stop reason;
- outcome/evidence.

### ToolInvocation
- intended action;
- tool/contract/version;
- parameters fingerprint;
- capability used;
- risk/consequence class;
- approval reference if needed;
- idempotency key;
- outcome/receipt.

### TriggerEvent
- type/source;
- timestamp;
- payload fingerprint;
- trust/security context;
- deduplication key;
- correlation IDs.

### ApprovalGate
- required capability/role;
- reason/risk;
- expiry;
- approved/rejected actor;
- evidence;
- resulting scope.

---

## Failure modes and safeguards

- **Agent loop/stagnation** → stop-condition engine, max steps, repetition detection.
- **Runaway cost** → hard budgets and escalation gates.
- **Tool hallucination** → tools are registry/contracts only; invalid calls rejected.
- **Capability escalation attempt** → M24 deny + security event.
- **Duplicate webhook/trigger** → dedup + idempotency keys.
- **Retry duplicates external action** → receipt lookup/idempotency guard.
- **Agent changes objective implicitly** → drift detection and block/escalate.
- **Human cancels during side effect** → safe cancellation boundary or compensation.
- **Provider/model failure** → governed fallback/retry.
- **Worker crash** → persisted checkpoint + resumable step.
- **Memory contamination** → source/authority classification and M22 policy.
- **Telemetry outage** → canonical state persists; M26 health becomes UNKNOWN/DEGRADED.
- **Automation definition drift** → versioned definitions; running instance pinned to version unless governed migration.
- **Concurrent runs conflict** → locks/leases/idempotency/resource policy.

---

## Planning acceptance criteria

Round 27 planning is acceptable when:
1. deterministic workflows and adaptive agents are clearly separated;
2. agent use requires a bounded execution envelope;
3. tool use cannot bypass M24;
4. schedules/triggers cannot grant authority;
5. retries/duplicate triggers/idempotency are explicit;
6. recovery/compensation semantics are defined;
7. human control and approval gates are first-class;
8. agent state/memory are outside chat and integrated with M22;
9. Production Graph integration with M01 is explicit;
10. M03/M02/M19/M20/M21/M25/M26 boundaries are explicit;
11. multi-agent privilege propagation is prohibited;
12. stop conditions and budgets bound open-ended execution;
13. requirements and architectural decision are canonicalized;
14. module/EPIC/catalog/checkpoint sources are synchronized;
15. Source Pack Integrity passes and independent audit finds no unresolved HIGH/CRITICAL defect.

## Out of scope for this planning round

- implementing an agent runtime;
- choosing a specific framework such as LangGraph/Temporal/Celery/etc.;
- creating unrestricted autonomous internet agents;
- allowing agents to self-modify governance/policies;
- automatic publication/payment/destructive execution without explicit policy;
- implementation of external connector catalog;
- M28 Export & Delivery specifics.
