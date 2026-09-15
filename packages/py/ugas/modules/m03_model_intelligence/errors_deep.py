# GENERATED-DEEP-PREPROGRAMMED
class M03Error(Exception):
    retryable: bool = False

class ValidationFailure(M03Error): pass
class PolicyFailure(M03Error): pass
class CapabilityFailure(M03Error): retryable = True
class QualityFailure(M03Error): pass
class InvariantFailure(M03Error): pass
