__all__ = [
    # ======================# DEBUG EXCEPTION #======================#
    "DebugException",
]

from chess.system import ChessException


# ======================# DEBUG EXCEPTION #======================#
class DebugException(ChessException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Leaf node of an exception which contains a description of the condition that caused a transaction or
        operation failure.
    2.  Should be encapsulated inside a WrapperException or CatchallException
    .
    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "DEBUG_ERROR"
    DEFAULT_MESSAGE = "An error occurred."