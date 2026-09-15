from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum
from typing import Iterable

class ProofState(StrEnum): PROVEN="proven"; CARRY_FORWARD="carry_forward"; INVALIDATED="invalidated"; UNKNOWN="unknown"; NOT_REQUIRED="not_required"
@dataclass(frozen=True,slots=True)
class EvidenceNode:
    id:str; project_id:str; subject_fingerprint:str; dimension:str; state:ProofState; producer_ref:str; dependency_refs:tuple[str,...]=(); evidence_ref:str|None=None
@dataclass(frozen=True,slots=True)
class EvidenceGraph:
    project_id:str; nodes:tuple[EvidenceNode,...]

def validate_graph(graph:EvidenceGraph)->None:
    by_id={n.id:n for n in graph.nodes}
    if len(by_id)!=len(graph.nodes): raise ValueError("duplicate evidence node")
    for n in graph.nodes:
        if n.project_id!=graph.project_id: raise ValueError("cross-project evidence forbidden")
        if n.state in {ProofState.PROVEN,ProofState.CARRY_FORWARD} and not n.evidence_ref: raise ValueError(f"proof lacks evidence: {n.id}")
        missing=set(n.dependency_refs)-set(by_id)
        if missing: raise ValueError(f"missing evidence dependencies: {sorted(missing)}")

def invalidate(graph:EvidenceGraph,changed_subjects:Iterable[str])->EvidenceGraph:
    changed=set(changed_subjects); affected={n.id for n in graph.nodes if n.subject_fingerprint in changed}
    grew=True
    while grew:
        grew=False
        for n in graph.nodes:
            if n.id not in affected and set(n.dependency_refs)&affected: affected.add(n.id); grew=True
    nodes=tuple(EvidenceNode(n.id,n.project_id,n.subject_fingerprint,n.dimension,ProofState.INVALIDATED if n.id in affected else n.state,n.producer_ref,n.dependency_refs,n.evidence_ref if n.id not in affected else None) for n in graph.nodes)
    return EvidenceGraph(graph.project_id,nodes)

# CODEX-TASK[KERNEL-EVIDENCE-DAG]
# Add explicit cycle detection, immutable graph fingerprint, reason-coded invalidation and bridge adapters
# from legacy module evidence bundles. Carry-forward requires unchanged dependency fingerprints.
