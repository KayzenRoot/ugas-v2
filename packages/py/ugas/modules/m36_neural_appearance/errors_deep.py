# GENERATED-DEEP-PREPROGRAMMED
class M36Error(Exception):
    retryable: bool = False

class ValidationFailure(M36Error): pass
class PolicyFailure(M36Error): pass
class CapabilityFailure(M36Error): retryable = True
class QualityFailure(M36Error): pass
class InvariantFailure(M36Error): pass
