# GENERATED-DEEP-PREPROGRAMMED
class M11Error(Exception):
    retryable: bool = False

class ValidationFailure(M11Error): pass
class PolicyFailure(M11Error): pass
class CapabilityFailure(M11Error): retryable = True
class QualityFailure(M11Error): pass
class InvariantFailure(M11Error): pass
