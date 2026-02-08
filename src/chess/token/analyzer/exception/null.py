__all__ = [
    # ======================# NULL_TOKEN_STATE EXCEPTION #======================#
    "ReadinessStateNullException",
]

from chess.system import NullException
from chess.token import TokenStateException


# ======================# NULL_TOKEN_STATE EXCEPTION #======================#
class ReadinessStateNullException(TokenStateException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that TokenState validation failed because the candidate was null.

    # PARENT:
        *   TokenStateException
        *   ReadinessStateNullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TOKEN_STATE_ERROR"
    DEFAULT_MESSAGE = "TokenState validation failed: The candidate was null."