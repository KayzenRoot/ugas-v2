# GENERATED-DEEP-PREPROGRAMMED
class M23Error(Exception):
    retryable: bool = False

class ValidationFailure(M23Error): pass
class PolicyFailure(M23Error): pass
class CapabilityFailure(M23Error): retryable = True
class QualityFailure(M23Error): pass
class InvariantFailure(M23Error): pass
