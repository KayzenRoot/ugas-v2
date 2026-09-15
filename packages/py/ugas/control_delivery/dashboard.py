from __future__ import annotations
import hashlib,json
from typing import Sequence
from .contracts import DashboardProjection,ProjectionEvent

def project_events(project_id:str,events:Sequence[ProjectionEvent],previous:DashboardProjection|None=None)->DashboardProjection:
    expected=(previous.last_sequence+1) if previous else 1
    diagnostics=list(previous.diagnostic_refs if previous else ())
    material=[]
    for event in sorted(events,key=lambda e:e.sequence):
        if event.project_id!=project_id: raise ValueError("cross-project projection event")
        if event.sequence!=expected: raise ValueError(f"projection sequence gap: expected {expected}, got {event.sequence}")
        if event.kind=="diagnostic": diagnostics.append(event.payload_ref)
        material.append((event.sequence,event.kind,event.subject_ref,event.payload_ref)); expected+=1
    seed={"project_id":project_id,"previous":previous.state_fingerprint if previous else None,"events":material}
    fingerprint=hashlib.sha256(json.dumps(seed,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return DashboardProjection(project_id,expected-1,fingerprint,tuple(diagnostics))

# CODEX-TASK[M26-REALTIME-TRANSPORT]
# Feed projection from canonical event stream via SSE/WebSocket adapter with replay/resume. UI commands
# must enter governed command API, never mutate projection/client state as production truth.
