__all__ = [
    # ======================# NULL_TOKEN_STATE EXCEPTION #======================#
    "ReadinessStateNullException",
]

from logic.system import NullException
from logic.token import TokenStateException


# ======================# NULL_TOKEN_STATE EXCEPTION #======================#
class ReadinessStateNullException(TokenStateException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that TokenState validation failed because the candidate was null.

    Super Class:
        *   TokenStateException
        *   ReadinessStateNullException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_TOKEN_STATE_EXCEPTION"
    MSG = "TokenState validation failed: The candidate was null."