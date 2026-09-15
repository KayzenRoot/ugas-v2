# GENERATED-DEEP-PREPROGRAMMED
class M10Error(Exception):
    retryable: bool = False

class ValidationFailure(M10Error): pass
class PolicyFailure(M10Error): pass
class CapabilityFailure(M10Error): retryable = True
class QualityFailure(M10Error): pass
class InvariantFailure(M10Error): pass
