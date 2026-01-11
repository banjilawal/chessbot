__all__ = [
    # ======================# SCALAR_VALIDATION_FAILURE EXCEPTION #======================#
    "ScalarValidationFailedException",
]

from chess.scalar import ScalarException
from chess.system import ValidationFailedException


# ======================# SCALAR_VALIDATION_FAILURE EXCEPTION #======================#
class ScalarValidationFailedException(ScalarException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Scalar. The encapsulated
        exceptions create a chain for tracing the source of the failure.

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