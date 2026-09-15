from __future__ import annotations

"""Materialize the canonical M01-M36 PREPROGRAMMED tree.

This script is deterministic and intentionally dependency-free. It creates source/test files
with bounded CODEX-TASK contracts so Codex assembles implementation instead of rediscovering
architecture. Existing non-generated files are never overwritten.
"""
from pathlib import Path

MODULES = {
1:("product_production_os","production graph/state machine/recipes/snapshots/invalidation/scheduling"),2:("hardware_intelligence","hardware profile/probes/resource budgets/routing"),3:("model_intelligence","model registry/qualification/capability routing"),4:("multimodal_ir","canonical multimodal IR/transforms/validation"),5:("asset_dna","asset identity/DNA/continuity/lineage"),6:("digital_humans","digital-human identity/appearance/performance/consent"),7:("image_studio","image jobs/conditioning/routes/evidence"),8:("video_studio","video jobs/shot state/temporal generation/evidence"),9:("animation_studio","motion state/retargeting/animation validation"),10:("spatial_3d","3D masters/derivatives/LOD/runtime visual signature"),11:("voice_studio","voice identity/speech/performance/evidence"),12:("music_studio","music intent/composition/stems/evidence"),13:("sound_studio","SFX/Foley/ambience/audio scene/evidence"),14:("narrative_canon","canon/characters/worlds/beats/continuity"),15:("faceless_content","channel recipes/content factory/packaging"),16:("ads_synthetic_ugc","campaign creative/ad variants/claims/UGC"),17:("brand_ip","brand system/IP/identity validation"),18:("localization","locale/translation/dubbing/subtitles/quality"),19:("quality_court","quality dimensions/judges/acceptance"),20:("repair_engine","defect localization/selective repair/revalidation"),21:("render_cost","cost/render planning/route economics"),22:("memory_rag","memory/retrieval/project context/evidence retrieval"),23:("provenance_c2pa","provenance/rights/content credentials/audit"),24:("security","policy/secrets/threat controls/security evidence"),25:("storage_cache","artifact storage/cache/retention/locality"),26:("dashboard_observability","telemetry/dashboard/alerts/digital-twin views"),27:("agent_runtime","agent contracts/tools/delegation/execution"),28:("delivery","masters/exporters/platform packages/validation"),29:("technology_foundry","technology candidates/Golden Shards/benchmarks/qualification"),30:("dcc_automation","DCC-IR/scene transactions/Blender/procedural/runtime export"),31:("creative_director","creative intent/state/tournaments/cross-modal coherence"),32:("world_simulation","world state/causality/time/branches/synthetic scenarios"),33:("virtual_production","production session/stage/camera/takes/continuity/editorial"),34:("global_optimization","critical path/Pareto routing/proof reuse/resources"),35:("adaptive_experience","experience IR/adaptive derivatives/accessibility/experiments"),36:("neural_appearance","appearance IR/inverse rendering/neural materials/relighting")}

HEADER = '''# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.\n# Do not redesign ownership here. Follow planning canon + Context Pack.\n'''

def task(mid: str, purpose: str) -> str:
    return f'''{HEADER}\n# CODEX-TASK[{mid}-CORE]\n# WHAT: complete only the bounded {purpose} behavior described by this module's planning canon.\n# INPUT: typed contracts from contracts.py and canonical shared primitives.\n# OUTPUT: typed result/events plus evidence references; never raw provider state as domain truth.\n# INVARIANTS: provider-independent intent; deterministic lineage; hard gates preserved; delta proof reuse.\n# ERRORS: use typed failures from errors.py; mark retryability explicitly.\n# TEST: tests/test_contracts.py then tests/test_service.py; broader suites only via Test Impact Graph.\n# DONE: focused tests pass and no unresolved CORE task remains.\n'''

def write_new(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")

for n,(slug,purpose) in MODULES.items():
    mid=f"M{n:02d}"; root=Path("packages/py/ugas/modules")/f"m{n:02d}_{slug}"
    write_new(root/"__init__.py", HEADER+f'"""{mid}: {purpose}."""\n')
    write_new(root/"contracts.py", HEADER+"from dataclasses import dataclass, field\nfrom typing import Any, Mapping\n\n@dataclass(frozen=True, slots=True)\nclass Command:\n    operation: str\n    payload: Mapping[str, Any] = field(default_factory=dict)\n    correlation_id: str = \"\"\n\n@dataclass(frozen=True, slots=True)\nclass Result:\n    status: str\n    evidence_refs: tuple[str, ...] = ()\n    data: Mapping[str, Any] = field(default_factory=dict)\n")
    write_new(root/"ports.py", HEADER+"from typing import Protocol\nfrom .contracts import Command, Result\n\nclass CapabilityPort(Protocol):\n    async def execute(self, command: Command) -> Result: ...\n")
    write_new(root/"errors.py", HEADER+"class ModuleError(Exception):\n    retryable: bool = False\n\nclass ValidationError(ModuleError): pass\nclass CapabilityUnavailable(ModuleError): retryable = True\nclass PolicyBlocked(ModuleError): pass\n")
    write_new(root/"domain.py", task(mid,purpose)+"\ndef validate_invariants(command):\n    # CODEX-TASK: replace with module-specific pure invariant checks from planning canon.\n    if not command.operation:\n        raise ValueError('operation is required')\n    return command\n")
    write_new(root/"service.py", task(mid,purpose)+"\nfrom .contracts import Command, Result\nfrom .domain import validate_invariants\n\nclass Service:\n    def __init__(self, capability): self._capability = capability\n    async def execute(self, command: Command) -> Result:\n        command = validate_invariants(command)\n        # CODEX-TASK: implement module-specific orchestration; do not add provider SDK imports.\n        return await self._capability.execute(command)\n")
    write_new(root/"tests/test_contracts.py", HEADER+"# CODEX-TASK: add module-specific contract/invariant tests from acceptance criteria.\ndef test_scaffold_is_explicit():\n    assert True\n")
    write_new(root/"tests/test_service.py", HEADER+"# CODEX-TASK: add focused orchestration tests with fake ports; no GPU/network here.\ndef test_scaffold_is_explicit():\n    assert True\n")

print(f"Materialized {len(MODULES)} module packages under packages/py/ugas/modules")
