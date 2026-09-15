from __future__ import annotations

"""Hard truth/rights/brand gates for M16-M17."""
from typing import Mapping

from .contracts import BrandDNA,CampaignIntent,ChannelVariant,ClaimState


def assert_brand_ready(brand:BrandDNA)->None:
    if not brand.rights_ref: raise ValueError("brand usage requires rights reference")


def assert_campaign_claims(intent:CampaignIntent)->None:
    for claim in intent.claims:
        if claim.state is not ClaimState.SUPPORTED:
            raise ValueError(f"claim not eligible for production: {claim.id}:{claim.state.value}")
        if not claim.evidence_refs:
            raise ValueError(f"supported claim missing evidence: {claim.id}")


def assert_brand_observation(brand:BrandDNA,observed_traits:Mapping[str,str])->None:
    assert_brand_ready(brand)
    for key,expected in sorted(brand.locked_traits.items()):
        if observed_traits.get(key)!=expected:
            raise ValueError(f"brand lock violation: {key}")


def assert_variant_lineage(variant:ChannelVariant,brand:BrandDNA,intent:CampaignIntent)->None:
    if variant.project_id!=brand.project_id or intent.project_id!=brand.project_id:
        raise ValueError("content/brand/campaign project mismatch")
    if variant.brand_fingerprint!=brand.fingerprint or intent.brand_fingerprint!=brand.fingerprint:
        raise ValueError("stale or mismatched brand fingerprint")
    allowed={claim.id for claim in intent.claims if claim.state is ClaimState.SUPPORTED}
    if not set(variant.claim_refs).issubset(allowed):
        raise ValueError("variant references unapproved claim")
    if intent.id not in variant.lineage:
        raise ValueError("variant must retain campaign lineage")


# CODEX-TASK[M16-DECEPTIVE-PATTERN-GATE]
# Add explicit policy/evaluator port for deceptive/manipulative patterns and unsupported implication.
# It is a hard rejection gate, not a score dimension that aesthetic quality can compensate for.
