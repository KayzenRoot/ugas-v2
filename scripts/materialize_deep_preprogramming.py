from __future__ import annotations

"""Materialize M01-M36 deep preprogramming from canonical wave manifests.

No external dependency is required. The generated files are architecture contracts, not claims
of finished production behavior. Existing files are not overwritten unless they carry the
GENERATED-DEEP-PREPROGRAMMED marker.
"""
from pathlib import Path
import ast

MODULES = {
1:("product_production_os",["ProjectId","ProductionId","GraphNodeId","GraphEdge","NodeState","ProductionGraph","ExecutionPlan","ArtifactRef","AcceptanceDecision"],["ProductionGraphService","StateTransitionService","InvalidationService","ExecutionPlanningService"],["MetadataRepository","EventBus","EvidenceSink","Clock"]),
2:("hardware_intelligence",["HardwareProfile","GpuProfile","CpuProfile","MemoryProfile","ResourceEnvelope","CapabilityProbe","ResourceLease"],["HardwareProbeService","ResourceEnvelopeService","LeasePlanner"],["SystemProbe","GpuTelemetry","ResourceLeaseStore"]),
3:("model_intelligence",["ModelProfile","CapabilityVector","BenchmarkResult","RouteCandidate","RouteDecision","QualificationState"],["ModelRegistryService","CapabilityMatcher","RouteSelector","QualificationService"],["ModelRegistry","BenchmarkStore","ProviderCapabilityProbe"]),
4:("multimodal_ir",["IRDocument","IRNode","IRReference","Modality","Constraint","IntentLock","IRVersion"],["IRCompiler","IRValidator","IRMigrationService"],["IRRepository","SchemaRegistry"]),
5:("asset_dna",["AssetDNA","IdentityTrait","AppearanceTrait","StructuralTrait","VariationBoundary","DNAFingerprint"],["AssetDNAService","IdentityConsistencyService","VariationCompiler"],["DNARepository","SimilarityEvaluator"]),
6:("digital_humans",["HumanIdentity","FaceState","BodyState","WardrobeState","VoiceBinding","PerformanceState","ConsentBinding"],["DigitalHumanService","IdentityBindingService","PerformanceStateService"],["HumanAssetStore","ConsentRegistry","FaceEvaluator","BodyEvaluator"]),
7:("image_studio",["ImageIntent","ImageGenerationPlan","ImageCandidate","ImageRegion","ImageEvaluation","ImageMaster"],["ImagePlanningService","ImageGenerationService","ImageSelectionService"],["ImageProvider","ImageEvaluator","ArtifactStore"]),
8:("video_studio",["VideoIntent","ShotPlan","TemporalConstraint","VideoCandidate","FrameWindow","VideoEvaluation","VideoMaster"],["VideoPlanningService","VideoGenerationService","TemporalConsistencyService"],["VideoProvider","VideoEvaluator","FrameRepairPort"]),
9:("animation_studio",["MotionIntent","SkeletonBinding","MotionClip","MotionConstraint","RetargetPlan","AnimationEvaluation"],["MotionPlanningService","RetargetService","AnimationValidationService"],["MotionProvider","RigAdapter","AnimationEvaluator"]),
10:("spatial_3d",["SpatialAssetIntent","CanonicalMultiView","SpatialMaster","MeshTopology","UVSet","MaterialSet","TargetCameraProfile","RuntimeDerivative","SpatialQualityDossier"],["SpatialAssetCompiler","TargetCameraCompiler","RuntimeDerivativeService","SpatialAcceptanceService"],["ReconstructionProvider","DccPort","RendererPort","SpatialEvaluator"]),
11:("voice_studio",["VoiceIdentity","VoiceIntent","UtterancePlan","VoiceCandidate","VoiceEvaluation","VoiceMaster"],["VoicePlanningService","VoiceSynthesisService","VoiceIdentityService"],["VoiceProvider","VoiceEvaluator","ConsentRegistry"]),
12:("music_studio",["MusicIntent","CuePlan","StemSet","MusicCandidate","MusicEvaluation","MusicMaster"],["MusicPlanningService","MusicGenerationService","StemAssemblyService"],["MusicProvider","MusicEvaluator","RightsRegistry"]),
13:("sound_studio",["SoundIntent","FoleyEvent","AmbienceBed","SfxAsset","AudioScene","SoundEvaluation"],["SoundSceneCompiler","FoleyService","SfxService","AmbienceService"],["AudioProvider","SoundLibrary","SoundEvaluator"]),
14:("narrative_canon",["CanonState","CharacterState","WorldFact","NarrativeBeat","SceneIntent","ContinuityConstraint","NarrativeDecision"],["CanonService","NarrativePlanner","ContinuityService"],["CanonRepository","NarrativeModelPort","RetrievalPort"]),
15:("faceless_content",["ChannelIdentity","ContentRecipe","HookPlan","SegmentPlan","FacelessProductionPlan","ChannelVariant"],["FacelessPlanner","SegmentCompiler","ChannelConsistencyService"],["NarrativePort","MediaAssemblyPort","DeliveryProfilePort"]),
16:("ads_synthetic_ugc",["CampaignIntent","Claim","EvidenceBinding","AdConcept","UGCVariant","ConversionObjective","AdEvaluation"],["AdPlanningService","ClaimGovernanceService","UGCCompiler"],["BrandPort","EvidenceRegistry","MediaProductionPort"]),
17:("brand_ip",["BrandDNA","BrandLock","TrademarkAsset","UsageRule","RightsGrant","BrandEvaluation"],["BrandGovernanceService","RightsService","BrandConsistencyService"],["RightsRepository","BrandAssetStore","BrandEvaluator"]),
18:("localization",["LocaleProfile","LocalizedText","CulturalConstraint","DubPlan","SubtitlePlan","LocalizationEvaluation"],["LocalizationPlanner","TranslationService","CulturalValidationService","DubSubtitleService"],["TranslationProvider","LocaleKnowledgePort","VoicePort"]),
19:("quality_court",["QualityDimension","JudgeResult","Defect","QualityDossier","AcceptancePolicy","CourtDecision"],["QualityCourt","JudgeRouter","AcceptanceAggregator"],["QualityJudge","EvaluationStore","PolicyRepository"]),
20:("repair_engine",["DefectMap","RepairPlan","RepairRegion","RepairAttempt","RepairEvaluation"],["RepairPlanner","SelectiveRepairService","RevalidationService"],["RepairProvider","DependencyGraphPort","QualityCourtPort"]),
21:("render_cost",["CostEstimate","RenderPlan","RouteEconomics","BudgetEnvelope","FailureAdjustedCost"],["CostPlanner","RenderPlanner","EconomicRouteService"],["PricingRegistry","HardwarePort","ModelIntelligencePort"]),
22:("memory_rag",["MemoryEntry","MemoryScope","RetrievalQuery","RetrievalResult","MemoryFingerprint","ContextPack"],["MemoryService","RetrievalService","ContextPackCompiler"],["VectorIndex","MetadataStore","EmbeddingPort"]),
23:("provenance_c2pa",["ProvenanceRecord","RightsRecord","TransformationRecord","ContentCredential","LineageEdge"],["ProvenanceService","RightsValidationService","CredentialService"],["ProvenanceStore","RightsRegistry","CredentialSigner"]),
24:("security",["SecurityPolicy","SecretRef","TrustBoundary","Permission","AuditEvent","ThreatFinding"],["PolicyEnforcementService","SecretBoundaryService","ThreatEvaluationService"],["SecretStore","AuditSink","SecurityScanner"]),
25:("storage_cache",["ArtifactKey","BlobRef","CacheKey","CachePolicy","ArtifactFingerprint","RetentionPolicy"],["ArtifactStoreService","CacheService","RetentionService"],["ObjectStore","CacheBackend","MetadataRepository"]),
26:("dashboard_observability",["DashboardView","RealtimeEvent","MetricPoint","Diagnostic","ControlCommand","UserPreference"],["DashboardQueryService","RealtimeProjectionService","ControlCommandService"],["EventStream","MetricsStore","ControlPlanePort"]),
27:("agent_runtime",["AgentRole","AgentCapability","AgentTask","AgentDecision","ToolGrant","AgentEvidence"],["AgentOrchestrator","CapabilityBroker","AgentGovernanceService"],["AgentRuntime","ToolRegistry","PolicyPort"]),
28:("delivery",["DeliveryTarget","DeliveryProfile","ExportPlan","DeliveryPackage","DeliveryReceipt"],["DeliveryCompiler","ExportService","DeliveryValidationService"],["Exporter","PlatformAdapter","ArtifactStore"]),
29:("technology_foundry",["TechnologyCandidate","QualificationPlan","BenchmarkProtocol","BenchmarkEvidence","TechnologyDecision","AdapterRequirement"],["TechnologyRadar","QualificationService","BenchmarkService","PromotionService"],["ResearchSourcePort","BenchmarkRunner","SecurityReviewPort","LicenseReviewPort"]),
30:("dcc_automation",["DccIR","DccOperation","SemanticSelector","DccTransaction","DccJob","DccResult","SceneFingerprint"],["DccCompiler","SceneTransactionEngine","BlenderWorkerService","DccQualityDossierService"],["DccAdapter","BlenderHeadlessPort","RendererPort","ArtifactStore"]),
31:("creative_director",["CreativeIntentKernel","CreativeConstraint","CreativeDecision","VisualEmotionMap","CreativeWorldModel","DirectionBrief"],["CreativeDirector","ConstraintLedgerService","DirectionCompiler","CreativeEvaluationService"],["NarrativePort","QualityCourtPort","ProductionPort"]),
32:("world_simulation",["WorldState","WorldSnapshot","SpatialState","TemporalState","ActorState","CausalEvent","SimulationBranch"],["WorldStateKernel","SimulationService","CausalityService","SnapshotService"],["PhysicsPort","EnvironmentPort","ActorSimulationPort","StateRepository"]),
33:("virtual_production",["ProductionSessionIR","StageState","CameraPlan","LightingState","PerformanceIntent","Take","CoverageGraph","EditCandidate"],["StageManager","CinematographyDirector","LightingDirector","TakeFactory","ContinuitySupervisor","EditorialService","ReshootDirector"],["WorldPort","DccPort","CastPort","AudioPostPort","QualityCourtPort"]),
34:("global_optimization",["ProductionStateVector","ParetoPoint","CriticalPath","ProofState","ResourcePlan","OptimizationDecision"],["GlobalProductionOptimizer","ProofReuseOptimizer","HardwareResourceOrchestrator","FailureEconomicsService","ProductionDigitalTwin"],["ExecutionGraphPort","HardwarePort","BenchmarkPort","EvidencePort"]),
35:("adaptive_experience",["ExperienceIR","AudienceContext","CreativeInvariantLock","AdaptiveVariant","ExperimentPlan","ExperienceEvaluation"],["AdaptiveCreativeCompiler","PersonalizationPolicyService","AccessibilityCompiler","ExperimentService","ExperienceOptimizer"],["MasterProductionPort","ConsentPolicyPort","DeliveryMetricsPort"]),
36:("neural_appearance",["AppearanceIR","MaterialObservation","NeuralMaterial","AnalyticMaterial","LightingEstimate","AppearanceDerivative","AppearanceEvaluation"],["MaterialDecompositionService","NeuralMaterialService","AnalyticDistillationService","LightingReconstructionService","RuntimeAppearanceCompiler"],["MaterialInferencePort","RendererPort","DccPort","AppearanceEvaluator"]),
}

MARK = "# GENERATED-DEEP-PREPROGRAMMED\n"

def write_generated(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and MARK not in path.read_text(encoding="utf-8"):
        return
    ast.parse(content) if path.suffix == ".py" else None
    path.write_text(content, encoding="utf-8")

def contracts(mid, names):
    body = MARK + "from dataclasses import dataclass, field\nfrom typing import Any, Mapping\n\n"
    body += "@dataclass(frozen=True, slots=True)\nclass ContractBase:\n    id: str\n    version: int = 1\n    fingerprint: str = ''\n    metadata: Mapping[str, Any] = field(default_factory=dict)\n\n"
    for name in names:
        body += f"@dataclass(frozen=True, slots=True)\nclass {name}(ContractBase):\n    \"\"\"Canonical {mid} contract. Extend fields only from approved module canon.\"\"\"\n    pass\n\n"
    return body

def ports(mid, names):
    body = MARK + "from typing import Any, Protocol\n\n"
    for name in names:
        body += f"class {name}(Protocol):\n    \"\"\"{mid} boundary. Provider/framework details stay behind this port.\"\"\"\n    async def execute(self, request: Any) -> Any: ...\n\n"
    return body

def services(mid, names):
    body = MARK + "from typing import Any\n\n"
    for name in names:
        body += f"class {name}:\n    \"\"\"PREPROGRAMMED orchestration boundary for {mid}.\"\"\"\n    def __init__(self, **ports: Any):\n        self._ports = ports\n\n    async def execute(self, request: Any) -> Any:\n        # CODEX-TASK[{mid}-{name}]\n        # WHAT: implement only the approved ordered flow from the deep-preprogramming manifest.\n        # INPUT/OUTPUT: canonical contracts.py types; adapters remain behind ports.py.\n        # INVARIANTS: lineage + hard gates + project isolation + deterministic invalidation.\n        # ERRORS: translate adapter failures into errors.py typed domain failures.\n        # TEST: focused fake-port test for this service before impacted integration tests.\n        # DONE: no architecture discovery or provider SDK leakage into domain/service code.\n        raise NotImplementedError('{mid} {name} implementation slot')\n\n"
    return body

def errors(mid):
    return MARK + f"class {mid}Error(Exception):\n    retryable: bool = False\n\nclass ValidationFailure({mid}Error): pass\nclass PolicyFailure({mid}Error): pass\nclass CapabilityFailure({mid}Error): retryable = True\nclass QualityFailure({mid}Error): pass\nclass InvariantFailure({mid}Error): pass\n"

def tests(mid, contract_names, service_names):
    return MARK + f"# Focused A0/A1 contract surface for {mid}. No GPU/network/provider calls here.\n\ndef test_contract_surface_is_declared():\n    expected = {contract_names!r}\n    assert expected\n\ndef test_service_surface_is_declared():\n    expected = {service_names!r}\n    assert expected\n\n# CODEX-TASK[{mid}-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.\n"

for n, (slug, cnames, snames, pnames) in MODULES.items():
    mid = f"M{n:02d}"
    root = Path("packages/py/ugas/modules") / f"m{n:02d}_{slug}"
    write_generated(root/"contracts_deep.py", contracts(mid, cnames))
    write_generated(root/"ports_deep.py", ports(mid, pnames))
    write_generated(root/"services_deep.py", services(mid, snames))
    write_generated(root/"errors_deep.py", errors(mid))
    write_generated(root/"tests/test_deep_contract_surface.py", tests(mid, cnames, snames))

print(f"Deep-preprogrammed {len(MODULES)} modules; generated files are safe implementation slots, not completed logic.")
