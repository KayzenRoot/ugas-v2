from ugas.runtime_experience.adapter import EngineCapabilities,validate_adapter
from ugas.runtime_experience.compiler import compile_runtime_plan
from ugas.runtime_experience.contracts import *

def target(memory=100): return RuntimeTarget("t","desktop","ref", "hw",FrameBudget(60,8,8,memory,100))

def test_compiler_streams_over_budget_asset_with_lod():
    scene=RuntimeScene("s","world",("a","b"),"interactions","cam")
    assets=(RuntimeAsset("a","m1","d1",("a:l0",),70,"proof:a"),RuntimeAsset("b","m2","d2",("b:l0","b:l2"),70,"proof:b"))
    plan=compile_runtime_plan(scene,target(),assets)
    assert plan.resident_assets==("a",); assert plan.streamed_assets==("b",); assert plan.fallback_refs==("b:l2",)

def test_over_budget_without_lod_fails_closed():
    scene=RuntimeScene("s","world",("a",),"i","cam")
    try: compile_runtime_plan(scene,target(10),(RuntimeAsset("a","m","d",(),20,"proof"),))
    except ValueError as exc: assert "without LOD" in str(exc)
    else: raise AssertionError("must fail")

def test_adapter_requires_headless_build():
    plan=RuntimeCompilePlan("p","s","t",(),(),())
    cap=EngineCapabilities("x",True,True,False,frozenset({"desktop"}))
    try: validate_adapter(cap,target(),plan)
    except ValueError as exc: assert "headless" in str(exc)
    else: raise AssertionError("must fail")

# CODEX-TASK[M37-A2]
# Add deterministic streaming-cell, frame-budget benchmark fixture, interaction-state replay and
# engine-neutral package round-trip tests. Do not require a real engine in A1/A2.
