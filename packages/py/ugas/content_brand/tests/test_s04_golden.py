from ugas.content_brand.contracts import *
from ugas.content_brand.evidence import *
from ugas.content_brand.faceless_policy import ChannelIdentity,ChannelObservation
from ugas.content_brand.golden_slice import ContentBrandSlice,evaluate_content_brand_slice
from ugas.content_brand.localization import LocalizationObservation,SubtitleSegment,validate_subtitle


def fixture():
    brand=BrandDNA("p","brand:f1",{"tone":"precise"},(),"rights:brand")
    claim=Claim("c1","Ships in 24h",ClaimState.SUPPORTED,("e:shipping",))
    campaign=CampaignIntent("camp","p","brand:f1","conversion",(claim,),"general")
    recipe=ContentRecipe("recipe","p","channel",("hook",),("body",),"brand:f1")
    identity=ChannelIdentity("channel","p","channel:f1",frozenset({"clear"}))
    variant=ChannelVariant("variant","p","recipe","brand:f1",("c1",),("camp",))
    observation=ChannelObservation(frozenset({"clear"}),1,1,"e:channel")
    localized=LocalizedText("copy","pt-BR","Envia em 24h","semantic:f1")
    profile=LocaleProfile("pt-BR","pt",(),25)
    locobs=LocalizationObservation(.99,(),"e:loc")
    return ContentBrandSlice(brand,campaign,recipe,identity,variant,observation,{"tone":"precise"},localized,profile,locobs)


def test_s04_golden_slice_accepts_governed_variant():
    assert len(evaluate_content_brand_slice(fixture(),minimum_semantic_similarity=.95))==3


def test_unsupported_claim_is_hard_rejected():
    v=fixture(); bad=Claim("c2","Guaranteed result",ClaimState.UNSUPPORTED,())
    campaign=CampaignIntent("camp","p","brand:f1","conversion",(bad,),"general")
    try: evaluate_content_brand_slice(ContentBrandSlice(v.brand,campaign,v.recipe,v.identity,v.variant,v.channel_observation,v.observed_brand_traits,v.localized_text,v.locale_profile,v.localization_observation),minimum_semantic_similarity=.95)
    except ValueError: pass
    else: raise AssertionError("unsupported claim must fail")


def test_subtitle_reading_rate_gate():
    profile=LocaleProfile("pt-BR","pt",(),10)
    assert validate_subtitle(SubtitleSegment("texto muito longo",0,500),profile)


def test_localization_delta_keeps_brand_proof():
    proofs=(ContentProof("brand","bf",frozenset({"brand"}),ProofState.PROVEN,"e1"),ContentProof("loc","lf",frozenset({"localization"}),ProofState.PROVEN,"e2"))
    updated=invalidate_content_proofs(proofs,frozenset({"localization"}))
    assert updated[0].state is ProofState.CARRY_FORWARD
    assert updated[1].state is ProofState.INVALIDATED

# CODEX-TASK[S04-A2-EXPANSION]
# Add brand-lock mismatch, missing rights, deceptive-pattern gate, cultural violation, dub timing and
# approved channel adaptation fixtures. Keep A2 deterministic and provider-free.
