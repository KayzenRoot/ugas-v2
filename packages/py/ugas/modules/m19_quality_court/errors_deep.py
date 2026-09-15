# GENERATED-DEEP-PREPROGRAMMED
class M19Error(Exception):
    retryable: bool = False

class ValidationFailure(M19Error): pass
class PolicyFailure(M19Error): pass
class CapabilityFailure(M19Error): retryable = True
class QualityFailure(M19Error): pass
class InvariantFailure(M19Error): pass
