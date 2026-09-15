from __future__ import annotations
from dataclasses import replace
from typing import Any

from .evidence_graph import EvidenceGraph, EvidenceNode, ProofState

"""Bridge adapters from legacy module evidence bundles into the canonical evidence graph.

M07/M11/M15 (media, audio_narrative, content_brand) each declare their own ProofState StrEnum. Those are
parallel definitions of the canonical taxonomy: media duplicates all five members, audio_narrative and
content_brand omit NOT_REQUIRED. Per CODEX-TASK[KERNEL-PRIMITIVE-MIGRATION] the transition is incremental
and must not be a repo-wide blind rewrite, so this module adapts legacy records by VALUE and leaves module
contracts untouched.

Deliberately duck-typed: the kernel must not import product modules, so the adapters read the shared legacy
attribute shape (proof_id, subject_fingerprint, dimensions, state, evidence_ref) instead of importing it.

Lineage is fail-closed: an unresolved legacy causal_ref raises rather than being dropped.
"""

CANONICAL_STATE_BY_VALUE: dict[str,ProofState]={s.value:s for s in ProofState}

def canonical_proof_state(legacy_state:Any)->ProofState:
    """Map a legacy module ProofState onto the canonical taxonomy.

    Fail-closed: an unrecognised value raises instead of defaulting, so an unknown state can never be
    silently promoted to proof.
    """
    value=str(getattr(legacy_state,"value",legacy_state))
    try: return CANONICAL_STATE_BY_VALUE[value]
    except KeyError: raise ValueError(f"unknown legacy proof state: {value!r}") from None

def evidence_nodes_from_legacy_proof(proof:Any,*,project_id:str,producer_ref:str)->tuple[EvidenceNode,...]:
    """Expand one legacy multi-dimension proof into one canonical node per dimension.

    Legacy proofs carry a frozenset of dimensions; canonical nodes are single-dimension. Expanding rather
    than merging preserves the invariant that dimensions stay independently invalidatable, so a repair in
    one dimension cannot invalidate an unrelated one. Node ids are deterministic.
    """
    state=canonical_proof_state(proof.state)
    return tuple(EvidenceNode(f"{proof.proof_id}::{dim}",project_id,proof.subject_fingerprint,dim,state,producer_ref,(),proof.evidence_ref) for dim in sorted(proof.dimensions))

def evidence_graph_from_legacy_bundle(bundle:Any,*,producer_ref:str)->EvidenceGraph:
    """Adapt a legacy module evidence bundle into the canonical evidence graph.

    Legacy causal_refs point at other proofs; canonical dependencies are node ids, so a causal reference to
    proof X expands to every canonical node derived from X.

    Fail-closed on lineage: a causal reference that resolves to no canonical node raises ValueError naming the
    proof and the unresolved refs. Silently dropping it would convert missing causal evidence into a
    valid-looking graph, which is exactly the failure this bridge exists to prevent.
    """
    project_id=bundle.project_id
    per_proof:list[tuple[Any,tuple[EvidenceNode,...]]]=[]
    node_ids_by_proof:dict[str,list[str]]={}
    for proof in bundle.proofs:
        nodes=evidence_nodes_from_legacy_proof(proof,project_id=project_id,producer_ref=producer_ref)
        per_proof.append((proof,nodes))
        node_ids_by_proof.setdefault(proof.proof_id,[]).extend(n.id for n in nodes)
    linked:list[EvidenceNode]=[]
    for proof,nodes in per_proof:
        refs=tuple(getattr(proof,"causal_refs",()) or ())
        unresolved=sorted({c for c in refs if c not in node_ids_by_proof})
        if unresolved:
            raise ValueError(f"unresolved causal reference(s) in proof {proof.proof_id!r}: {unresolved}")
        resolvable=tuple(sorted({nid for c in refs for nid in node_ids_by_proof[c]}))
        linked.extend(replace(n,dependency_refs=resolvable) for n in nodes)
    return EvidenceGraph(project_id,tuple(linked))

def legacy_proof_states(bundle:Any)->tuple[str,...]:
    """Value-level state names present in a legacy bundle, for parity checks during transition."""
    return tuple(sorted({str(p.state) for p in bundle.proofs}))
