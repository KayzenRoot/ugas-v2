# GENERATED-DEEP-PREPROGRAMMED
class M18Error(Exception):
    retryable: bool = False

class ValidationFailure(M18Error): pass
class PolicyFailure(M18Error): pass
class CapabilityFailure(M18Error): retryable = True
class QualityFailure(M18Error): pass
class InvariantFailure(M18Error): pass
