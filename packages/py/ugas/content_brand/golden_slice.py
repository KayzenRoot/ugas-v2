from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
from .contracts import BrandDNA,CampaignIntent,ChannelVariant,ContentRecipe,LocaleProfile,LocalizedText
from .faceless_policy import ChannelIdentity,ChannelObservation,validate_faceless_variant
from .governance import assert_brand_observation,assert_campaign_claims,assert_variant_lineage
from .localization import LocalizationObservation,validate_localization

@dataclass(frozen=True,slots=True)
class ContentBrandSlice:
    brand:BrandDNA
    campaign:CampaignIntent
    recipe:ContentRecipe
    identity:ChannelIdentity
    variant:ChannelVariant
    channel_observation:ChannelObservation
    observed_brand_traits:Mapping[str,str]
    localized_text:LocalizedText
    locale_profile:LocaleProfile
    localization_observation:LocalizationObservation

def evaluate_content_brand_slice(v:ContentBrandSlice,*,minimum_semantic_similarity:float)->tuple[str,...]:
    assert_brand_observation(v.brand,v.observed_brand_traits)
    assert_campaign_claims(v.campaign)
    assert_variant_lineage(v.variant,v.brand,v.campaign)
    channel_failures=validate_faceless_variant(v.variant,v.recipe,v.identity,v.channel_observation)
    locale_failures=validate_localization(v.localized_text,v.locale_profile,v.localization_observation,minimum_semantic_similarity=minimum_semantic_similarity)
    failures=channel_failures+locale_failures
    if failures: raise ValueError(";".join(failures))
    return (v.brand.fingerprint,v.variant.id,v.localized_text.semantic_fingerprint)

# CODEX-TASK[S04-GOLDEN-WIRING]
# Add approved-claim resolver and fake media/narrative assembly ports. Prove that channel adaptation
# and localization may vary presentation but cannot mutate brand locks, truth claims or lineage.
