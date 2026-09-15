# GENERATED-DEEP-PREPROGRAMMED
class M33Error(Exception):
    retryable: bool = False

class ValidationFailure(M33Error): pass
class PolicyFailure(M33Error): pass
class CapabilityFailure(M33Error): retryable = True
class QualityFailure(M33Error): pass
class InvariantFailure(M33Error): pass
