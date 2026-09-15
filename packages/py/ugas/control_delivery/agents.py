from __future__ import annotations
from dataclasses import dataclass
from .contracts import AgentTask

@dataclass(frozen=True,slots=True)
class AgentUsage:
    steps:int=0; tool_calls:int=0; cost:float=0.0

def authorize_agent_action(task:AgentTask,usage:AgentUsage,*,capability:str,incremental_cost:float=0.0)->None:
    b=task.budget
    if capability not in b.allowed_capabilities: raise PermissionError("agent capability denied")
    if usage.steps>=b.max_steps: raise RuntimeError("agent step budget exhausted")
    if usage.tool_calls>=b.max_tool_calls: raise RuntimeError("agent tool-call budget exhausted")
    if usage.cost+incremental_cost>b.max_cost: raise RuntimeError("agent cost budget exhausted")

def next_usage(usage:AgentUsage,*,tool_call:bool,cost:float)->AgentUsage:
    if cost<0: raise ValueError("agent cost cannot be negative")
    return AgentUsage(usage.steps+1,usage.tool_calls+(1 if tool_call else 0),usage.cost+cost)

# CODEX-TASK[M27-LOOP-GUARD]
# Add repeated-state/low-progress loop detection, per-tool grants, checkpointing and mandatory evidence
# emission. Agent may stop early; it may never silently expand its own capability or budget.
