__all__ = [
    # ======================# SCALAR_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidScalarException",
]

from chess.scalar import ScalarException
from chess.system import ValidationFailedException


# ======================# SCALAR_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidScalarException(ScalarException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Scalar candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidScalarException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidScalarException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   ScalarException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCALAR_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Scalar validation failed."