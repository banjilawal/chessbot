__all__ = [
    # ======================# CATCHALL EXCEPTION #======================#
    "CatchallException",
]

from chess.system import ChessException


# ======================# CATCHALL EXCEPTION #======================#
class CatchallException(ChessException):
    """
    # ROLE: Catchall

    # RESPONSIBILITIES:
    1.  Parent of a collection of debug and wrapper exceptions for an entity objects that support it
    2.  Raised when subclasses do not provide coverage for an error case.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "CATCHALL EXCEPTION"
    DEFAULT_MESSAGE = "CatchallException"