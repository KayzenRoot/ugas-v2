# GENERATED-DEEP-PREPROGRAMMED
class M35Error(Exception):
    retryable: bool = False

class ValidationFailure(M35Error): pass
class PolicyFailure(M35Error): pass
class CapabilityFailure(M35Error): retryable = True
class QualityFailure(M35Error): pass
class InvariantFailure(M35Error): pass
