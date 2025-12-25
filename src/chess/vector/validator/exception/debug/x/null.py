__all__ = [
    # ======================# NULL_VECTOR_X_AXIS EXCEPTION #======================#
    "VectorNullXAxisException",
]

from chess.system import NullException
from chess.vector.validator.exception.wrapper import InvalidVectorException


# ======================# NULL_VECTOR_X_AXIS EXCEPTION #======================#
class VectorNullXAxisException(InvalidVectorException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that Vector validation failed because the x_axis was null.

    # PARENT:
        *   NullException
        *   InvalidVectorException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_VECTOR_X_AXIS_ERROR"
    DEFAULT_MESSAGE = "Vector validation failed: The x axis was null."