__all__ = [
    # ======================# NULL_VECTOR_Y_AXIS EXCEPTION #======================#
    "VectorNullXAxisException",
]

from chess.system import NullException
from chess.vector.validator.exception.wrapper import InvalidVectorException


# ======================# NULL_VECTOR_Y_AXIS EXCEPTION #======================#
class VectorNullYAxisException(InvalidVectorException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that Vector validation failed because the y_ax was null.

    # PARENT:
        *   NullException
        *   InvalidVectorException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_VECTOR_Y_AXIS_ERROR"
    DEFAULT_MESSAGE = "Vector validation failed: The y axis was null."