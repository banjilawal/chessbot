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
    1.  Contains a description of the condition that caused a failure.
    Leaf node in an exception chain.
    2.  Are the desired exception type in a Result.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "DEBUG_EXCEPTION"
    DEFAULT_MESSAGE = "DebugException"