# GENERATED-DEEP-PREPROGRAMMED
class M02Error(Exception):
    retryable: bool = False

class ValidationFailure(M02Error): pass
class PolicyFailure(M02Error): pass
class CapabilityFailure(M02Error): retryable = True
class QualityFailure(M02Error): pass
class InvariantFailure(M02Error): pass
