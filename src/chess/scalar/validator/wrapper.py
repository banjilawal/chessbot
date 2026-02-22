__all__ = [
    # ======================# SCALAR_VALIDATION_FAILURE #======================#
    "ScalarValidationException",
]

from chess.scalar import ScalarException
from chess.system import ValidationException


# ======================# SCALAR_VALIDATION_FAILURE #======================#
class ScalarValidationException(ScalarException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Scalar. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   ScalarException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCALAR_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Scalar validation failed."