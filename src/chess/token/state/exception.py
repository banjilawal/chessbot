__all__ = [
    # ======================# TOKEN_STATE EXCEPTION #======================#
    "TokenStateException",
]

from chess.system import ChessException


# ======================# TOKEN_STATE EXCEPTION #======================#
class TokenStateException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for TokenState errors.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_STATE_ERROR"
    DEFAULT_MESSAGE = "TokenState raised an exception."