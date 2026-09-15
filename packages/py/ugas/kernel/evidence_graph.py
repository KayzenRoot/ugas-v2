from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum
from hashlib import sha256
import json
from typing import Iterable, Mapping

class ProofState(StrEnum): PROVEN="proven"; CARRY_FORWARD="carry_forward"; INVALIDATED="invalidated"; UNKNOWN="unknown"; NOT_REQUIRED="not_required"
@dataclass(frozen=True,slots=True)
class EvidenceNode:
    id:str; project_id:str; subject_fingerprint:str; dimension:str; state:ProofState; producer_ref:str; dependency_refs:tuple[str,...]=(); evidence_ref:str|None=None; dependency_fingerprints:tuple[tuple[str,str],...]=()
@dataclass(frozen=True,slots=True)
class EvidenceGraph:
    project_id:str; nodes:tuple[EvidenceNode,...]

def _by_id(graph:EvidenceGraph)->dict[str,EvidenceNode]:
    return {n.id:n for n in graph.nodes}

def detect_cycles(graph:EvidenceGraph)->tuple[tuple[str,...],...]:
    """Return dependency cycles as node-id paths, deterministically ordered and deduplicated.

    Each returned tuple is a closed dependency path; a self-dependency is reported as a 1-tuple.
    """
    by_id=_by_id(graph); state:dict[str,int]={}; cycles:list[tuple[str,...]]=[]; seen:set[frozenset[str]]=set()
    for root in sorted(by_id):
        if state.get(root,0)!=0: continue
        stack:list[tuple[str,int]]=[(root,0)]; path:list[str]=[]
        while stack:
            node_id,index=stack[-1]
            if index==0: state[node_id]=1; path.append(node_id)
            deps=sorted(d for d in by_id[node_id].dependency_refs if d in by_id)
            if index<len(deps):
                stack[-1]=(node_id,index+1); nxt=deps[index]
                if state.get(nxt,0)==1:
                    cycle=tuple(path[path.index(nxt):]); key=frozenset(cycle)
                    if key not in seen: seen.add(key); cycles.append(cycle)
                elif state.get(nxt,0)==0: stack.append((nxt,0))
            else:
                state[node_id]=2; path.pop(); stack.pop()
    return tuple(sorted(cycles))

def validate_graph(graph:EvidenceGraph)->None:
    by_id=_by_id(graph)
    if len(by_id)!=len(graph.nodes): raise ValueError("duplicate evidence node")
    for n in graph.nodes:
        if n.project_id!=graph.project_id: raise ValueError("cross-project evidence forbidden")
        if n.state in {ProofState.PROVEN,ProofState.CARRY_FORWARD} and not n.evidence_ref: raise ValueError(f"proof lacks evidence: {n.id}")
        missing=set(n.dependency_refs)-set(by_id)
        if missing: raise ValueError(f"missing evidence dependencies: {sorted(missing)}")
    cycles=detect_cycles(graph)
    if cycles: raise ValueError(f"cyclic evidence dependencies: {[list(c) for c in cycles]}")

def graph_fingerprint(graph:EvidenceGraph)->str:
    """Deterministic content fingerprint, independent of node ordering.

    Two graphs with the same project and the same node set produce the same fingerprint regardless of the
    order nodes were supplied in.
    """
    payload=[{"id":n.id,"subject":n.subject_fingerprint,"dimension":n.dimension,"state":str(n.state),
              "producer":n.producer_ref,"dependencies":sorted(n.dependency_refs),
              "dependency_fingerprints":sorted(list(p) for p in n.dependency_fingerprints),
              "evidence":n.evidence_ref} for n in sorted(graph.nodes,key=lambda n:n.id)]
    return sha256(json.dumps({"project_id":graph.project_id,"nodes":payload},sort_keys=True,separators=(",",":")).encode()).hexdigest()

def invalidate(graph:EvidenceGraph,changed_subjects:Iterable[str])->EvidenceGraph:
    changed=set(changed_subjects); affected={n.id for n in graph.nodes if n.subject_fingerprint in changed}
    grew=True
    while grew:
        grew=False
        for n in graph.nodes:
            if n.id not in affected and set(n.dependency_refs)&affected: affected.add(n.id); grew=True
    nodes=tuple(EvidenceNode(n.id,n.project_id,n.subject_fingerprint,n.dimension,ProofState.INVALIDATED if n.id in affected else n.state,n.producer_ref,n.dependency_refs,n.evidence_ref if n.id not in affected else None,n.dependency_fingerprints) for n in graph.nodes)
    return EvidenceGraph(graph.project_id,nodes)

def record_dependency_fingerprints(graph:EvidenceGraph)->EvidenceGraph:
    """Snapshot every node's dependency subject fingerprints so carry-forward can be checked later."""
    by_id=_by_id(graph)
    nodes=tuple(EvidenceNode(n.id,n.project_id,n.subject_fingerprint,n.dimension,n.state,n.producer_ref,n.dependency_refs,n.evidence_ref,tuple((d,by_id[d].subject_fingerprint) for d in sorted(n.dependency_refs) if d in by_id)) for n in graph.nodes)
    return EvidenceGraph(graph.project_id,nodes)

def carry_forward(graph:EvidenceGraph,current_fingerprints:Mapping[str,str])->EvidenceGraph:
    """Promote proven work to CARRY_FORWARD only when it is provably unchanged.

    The canonical invariant is that unchanged proofs carry forward by fingerprint, so a node carries forward
    only when both hold: its own subject fingerprint is verified unchanged, and every dependency fingerprint
    recorded at proof time still matches. current_fingerprints maps node id to the current subject fingerprint.

    Fail-closed: a node whose own subject cannot be verified, or that has dependencies but no complete recorded
    snapshot, is INVALIDATED rather than carried forward. An unverifiable fingerprint must never be treated as
    an unchanged proof.
    """
    out:list[EvidenceNode]=[]
    for n in graph.nodes:
        if n.state not in {ProofState.PROVEN,ProofState.CARRY_FORWARD}: out.append(n); continue
        recorded=dict(n.dependency_fingerprints)
        own_unchanged=current_fingerprints.get(n.id)==n.subject_fingerprint
        deps_unchanged=all(d in recorded and recorded[d]==current_fingerprints.get(d) for d in n.dependency_refs)
        if own_unchanged and deps_unchanged:
            out.append(EvidenceNode(n.id,n.project_id,n.subject_fingerprint,n.dimension,ProofState.CARRY_FORWARD,n.producer_ref,n.dependency_refs,n.evidence_ref,n.dependency_fingerprints))
        else:
            out.append(EvidenceNode(n.id,n.project_id,n.subject_fingerprint,n.dimension,ProofState.INVALIDATED,n.producer_ref,n.dependency_refs,None,n.dependency_fingerprints))
    return EvidenceGraph(graph.project_id,tuple(out))

# CODEX-TASK[KERNEL-EVIDENCE-DAG]
# Done: cycle detection, deterministic immutable graph fingerprint, dependency-fingerprint carry-forward,
#       and legacy-bundle bridge adapters (kernel/legacy_evidence_bridge.py).
# Remaining: reason-coded invalidation beyond the causal closure in invalidate(). Still open; do not claim
#            it as done.
