__all__ = [
    # ======================# DEBUG EXCEPTION #======================#
    "DebugException",
]

from chess.system import ChessException


# ======================# DEBUG EXCEPTION #======================#
class DebugException(ChessException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Identifies the code block in a method where the error occurred.
    2.  Describe what condition or state prevented an operation from completing successfully.
    3.  Lowest part of the 3-layer exception chain. Should not contain other exceptions.
    
    # ERROR CODE CONVENTION:
    1.  All caps, snake case description of the error with _ERROR as the suffix.
    
    # DEFAULT MSG CONVENTION:
    1.  Wrapper msg followed by a colon. Description of the error after the colon.
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
    ERR_CODE = "DEBUG_ERROR"
    MSG = "An error occurred."