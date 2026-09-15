from __future__ import annotations
from typing import Mapping,Sequence
from .contracts import ProvenanceNode

def validate_provenance_graph(nodes:Sequence[ProvenanceNode])->None:
    by_id={n.id:n for n in nodes}
    if len(by_id)!=len(nodes): raise ValueError("duplicate provenance node id")
    for node in nodes:
        if not node.fingerprint or not node.source_ref or not node.rights_ref:
            raise ValueError(f"incomplete provenance node: {node.id}")
        missing=set(node.parent_refs)-set(by_id)
        if missing: raise ValueError(f"missing provenance parents for {node.id}: {sorted(missing)}")
    visiting=set(); visited=set()
    def visit(node_id:str)->None:
        if node_id in visiting: raise ValueError("provenance cycle detected")
        if node_id in visited: return
        visiting.add(node_id)
        for parent in by_id[node_id].parent_refs: visit(parent)
        visiting.remove(node_id); visited.add(node_id)
    for node_id in sorted(by_id): visit(node_id)

# CODEX-TASK[M23-CREDENTIAL-BRIDGE]
# Add transformation records and content-credential/C2PA adapter behind a port. Credentials must be
# derived from complete internal lineage; external credential failure must not erase internal proof.
