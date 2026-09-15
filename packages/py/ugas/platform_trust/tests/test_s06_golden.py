from ugas.platform_trust.contracts import *
from ugas.platform_trust.golden_slice import PlatformTrustSlice,evaluate_platform_trust_slice
from ugas.platform_trust.memory import plan_context
from ugas.platform_trust.provenance import validate_provenance_graph
from ugas.platform_trust.security_storage import content_hash,validate_cache_entry


def test_memory_retrieval_cannot_cross_project_scope():
    a=ProjectScope("a","tenant"); b=ProjectScope("b","tenant")
    records=(MemoryRecord("1",a,"f1","a:1","p1",10),MemoryRecord("2",b,"f2","b:1","p2",1))
    result=plan_context(ContextRequest(a,"q",20),records)
    assert tuple(r.id for r in result)==("1",)


def test_provenance_cycle_is_rejected():
    nodes=(ProvenanceNode("a","fa","sa","ra",("b",)),ProvenanceNode("b","fb","sb","rb",("a",)))
    try: validate_provenance_graph(nodes)
    except ValueError as exc: assert "cycle" in str(exc)
    else: raise AssertionError("provenance cycle must fail")


def test_stale_cache_fingerprint_is_rejected():
    source=StoredObject("abc",3,"x","s3:x")
    try: validate_cache_entry(CacheEntry("k","different","cache:x"),source)
    except ValueError as exc: assert "stale" in str(exc)
    else: raise AssertionError("stale cache must fail")


def test_s06_golden_slice():
    scope=ProjectScope("p","t"); data=b"asset"; digest=content_hash(data)
    v=PlatformTrustSlice(
        ContextRequest(scope,"q",20),(MemoryRecord("m",scope,"mf","memory:m","prov:m",10),),
        (ProvenanceNode("root","pf","source","rights",()),),
        (CapabilityGrant("agent","read","project:p",None),),"agent","read","project:p",100,
        StoredObject(digest,len(data),"application/octet-stream","s3:asset"),data,None)
    r=evaluate_platform_trust_slice(v)
    assert r.context_refs==("memory:m",)
    assert r.provenance_node_ids==("root",)
    assert r.content_hash==digest

# CODEX-TASK[S06-A2-EXPANSION]
# Add expired grant denial, missing rights/source provenance, corrupted object, cache-loss correctness,
# secret-redaction and deterministic context-budget fixtures. Keep A2 external-service free.
