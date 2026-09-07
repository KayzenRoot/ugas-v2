# ADR-0016 — Bounded Automation, Deterministic First

**Status:** ACCEPTED  
**Date:** 2026-09-06

## Context
UGAS V2 needs automation across long multimodal production pipelines. Some tasks are deterministic and auditable; others benefit from model reasoning and adaptive tool selection. Treating every workflow as an autonomous agent would increase uncertainty, cost, security surface, replay difficulty and operational risk.

## Decision
UGAS V2 SHALL use deterministic workflow/state-machine orchestration by default and introduce agentic reasoning only for bounded subproblems that materially require it.

Every agent execution SHALL bind an explicit objective, scope, capabilities/tools, data/security context, budgets, approval policy and stop conditions. Schedules/events MAY request execution but SHALL NOT grant authority. All consequential actions SHALL pass canonical APIs/state machines and M24 authorization. Retries and external side effects SHALL use explicit idempotency/compensation controls. Long-running state SHALL persist outside chat context and significant decisions SHALL be observable through M26.

## Consequences

### Positive
- lower operational entropy and cost;
- easier audit/replay/recovery;
- smaller capability surface;
- human supervision remains explicit;
- agent reasoning can still be used where it adds measurable value;
- deterministic shells can contain bounded agent subtasks.

### Costs
- workflow definitions/state machines require engineering discipline;
- idempotency and compensation contracts add design overhead;
- agents need explicit envelopes/budgets rather than unconstrained prompts;
- some open-ended tasks may require decomposition into deterministic + adaptive phases.

## Rejected alternatives

### Agent-everything architecture
Rejected because deterministic workflows are cheaper, safer and more reproducible for many production tasks.

### Schedules/webhooks as implicit permission
Rejected because trigger source/timing does not establish authorization.

### Agent self-expansion of tools or scope
Rejected because model output is untrusted and cannot create capabilities.

### Chat history as long-running workflow state
Rejected because chat is non-canonical and unreliable as process state.
