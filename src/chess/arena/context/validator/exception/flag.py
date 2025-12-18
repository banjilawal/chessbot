# src/chess/arena/context/validator/exception/flag.py

"""
Module: chess.arena.arena.context.validator.exception.flag
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.arena import InvalidArenaContextException

__all__ = [
    # ========================= NO_ARENA_CONTEXT_FLAG EXCEPTION =========================#
    "NoArenaContextFlagException",
    # ========================= TOO_MANY_ARENA_CONTEXT_FLAGS EXCEPTION =========================#
    "TooManyArenaContextFlagsException"
]


# ========================= NO_ARENA_CONTEXT_FLAG EXCEPTION =========================#
class NoArenaContextFlagException(InvalidArenaContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no ArenaContext flag is provided with a searcher value.

    # PARENT:
        *   InvalidArenaContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_ARENA_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No ArenaContext flag was selected. A context flag must be turned on with a target value."


# ========================= TOO_MANY_ARENA_CONTEXT_FLAGS EXCEPTION =========================#
class TooManyArenaContextFlagsException(InvalidArenaContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, ArenaContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Arena attribute is going to be used in an ArenaSnapshotFinder.

    # PARENT:
        *   InvalidArenaContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_ARENA_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one ArenaContext flag was selected. Only one context flag is allowed."