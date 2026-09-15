from __future__ import annotations

"""Provider-independent contracts for S04 M15-M18."""
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Mapping


class ClaimState(StrEnum):
    SUPPORTED="supported"
    UNSUPPORTED="unsupported"
    PROHIBITED="prohibited"


@dataclass(frozen=True, slots=True)
class BrandDNA:
    project_id:str
    fingerprint:str
    locked_traits:Mapping[str,str]=field(default_factory=dict)
    usage_rules:tuple[str,...]=()
    rights_ref:str=""


@dataclass(frozen=True, slots=True)
class Claim:
    id:str
    text:str
    state:ClaimState
    evidence_refs:tuple[str,...]=()


@dataclass(frozen=True, slots=True)
class CampaignIntent:
    id:str
    project_id:str
    brand_fingerprint:str
    objective:str
    claims:tuple[Claim,...]
    audience_context:str


@dataclass(frozen=True, slots=True)
class ContentRecipe:
    id:str
    project_id:str
    channel_identity_ref:str
    hook_constraints:tuple[str,...]
    segment_constraints:tuple[str,...]
    brand_fingerprint:str


@dataclass(frozen=True, slots=True)
class ChannelVariant:
    id:str
    project_id:str
    recipe_ref:str
    brand_fingerprint:str
    claim_refs:tuple[str,...]
    lineage:tuple[str,...]


@dataclass(frozen=True, slots=True)
class LocaleProfile:
    locale:str
    language:str
    cultural_constraints:tuple[str,...]=()
    max_subtitle_chars_per_second:float=20.0


@dataclass(frozen=True, slots=True)
class LocalizedText:
    source_ref:str
    locale:str
    text:str
    semantic_fingerprint:str


# CODEX-TASK[S04-CONTRACT-EXPANSION]
# Add M15 HookPlan/SegmentPlan, M16 AdConcept/UGCVariant, M17 BrandLock/RightsGrant and
# M18 DubPlan/SubtitlePlan/Evaluation contracts from deep specs. Keep claims/rights/lineage explicit.
