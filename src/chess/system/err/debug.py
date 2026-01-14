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
    1.  Innermost layer of the 3-part exception chain. Describes the condition that prevented the operation Leaf node of an exception which contains a description of the condition that caused a transaction or
        operation failure.
    2.  Should be encapsulated inside a WrapperException or CatchallException
    
    # ERROR CODE CONVENTION:
    1.  All caps, snake case description of the error with _ERROR as the suffix.
    
    # DEFAULT MESSAGE CONVENTION:
    1.  Wrapper message followed by a colon. Description of the error after the colon.
    2.  The Syntax is: [Class] operation failed: [Description]

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