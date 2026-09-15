from __future__ import annotations

"""A1/A2 deterministic S03 doubles. No network, model download or synthesis."""
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class FakeCanonRepository:
    states: dict[str,Any]=field(default_factory=dict)
    async def get(self, project_id:str)->Any|None: return self.states.get(project_id)
    async def put(self, state:Any)->None: self.states[state.project_id]=state


@dataclass(slots=True)
class FakeRightsRegistry:
    verified_refs:set[str]=field(default_factory=set)
    async def verify(self, rights_ref:str)->bool: return rights_ref in self.verified_refs


@dataclass(slots=True)
class FakeSynthesisPort:
    outputs:dict[str,Any]=field(default_factory=dict)
    calls:list[str]=field(default_factory=list)
    async def synthesize(self, request_id:str)->Any:
        self.calls.append(request_id)
        if request_id not in self.outputs: raise ValueError(f"no fake synthesis fixture: {request_id}")
        return self.outputs[request_id]


@dataclass(slots=True)
class FakeEvaluator:
    outputs:dict[str,Any]=field(default_factory=dict)
    async def evaluate(self, artifact_id:str)->Any:
        if artifact_id not in self.outputs: raise ValueError(f"no fake evaluation fixture: {artifact_id}")
        return self.outputs[artifact_id]


# CODEX-TASK[S03-EXACT-PORT-ADAPTERS]
# After module materialization, make these doubles implement the exact M11-M14 Protocols and add
# deterministic voice/music/sound/narrative fixtures. Real providers remain outside A2.
