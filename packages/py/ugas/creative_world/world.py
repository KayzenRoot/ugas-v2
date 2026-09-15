from __future__ import annotations
from typing import Sequence
from .contracts import WorldEntity,WorldEvent,WorldSnapshot

def apply_world_events(snapshot:WorldSnapshot,events:Sequence[WorldEvent])->WorldSnapshot:
    states={e.id:e for e in snapshot.entity_states}
    applied=set()
    for event in events:
        if any(c not in applied for c in event.cause_refs): raise ValueError(f"unresolved world cause: {event.id}")
        current=states.get(event.target_entity_id)
        if current is None: raise ValueError(f"unknown world entity: {event.target_entity_id}")
        if current.state_fingerprint!=event.before_fingerprint: raise ValueError(f"stale world transition: {event.id}")
        states[event.target_entity_id]=WorldEntity(current.id,event.after_fingerprint); applied.add(event.id)
    return WorldSnapshot(f"{snapshot.id}:v{snapshot.version+1}",snapshot.project_id,snapshot.version+1,tuple(states[k] for k in sorted(states)),snapshot.id)

# CODEX-TASK[M32-CAUSAL-GRAPH]
# Support causes from prior persisted events/snapshots, deterministic event ordering and rollback/replay.
# World truth is structured state plus causal events; image/video output is evidence/derivative only.
