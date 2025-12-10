# src/chess/game/context/validator/exception/flag/exception.py

"""
Module: chess.game.context.validator.exception.flag.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.game import InvalidGameContextException

__all__ = [
    #========================= NO_GAME_CONTEXT_FLAG EXCEPTION =========================#
    "NoGameContextFlagException",
    #========================= TOO_MANY_GAME_CONTEXT_FLAGS EXCEPTION =========================#
    "TooManyGameContextFlagsException"
]


#========================= NO_GAME_CONTEXT_FLAG EXCEPTION =========================#
class NoGameContextFlagException(InvalidGameContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no GameContext flag is provided with a searcher value.
    
    # PARENT
        *   InvalidGameContextException
        *   ContextFlagCountException

    # PROVIDES:
    NoGameContextFlagException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_GAME_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No GameContext flag was selected. A context flag must be turned on with a target value."


#========================= TOO_MANY_GAME_CONTEXT_FLAGS EXCEPTION =========================#
class TooManyGameContextFlagsException(InvalidGameContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, GameContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Game attribute is going to be used in an GameSnapshotFinder.
    
    # PARENT
        *   InvalidGameContextException
        *   ContextFlagCountException

    # PROVIDES:
    TooManyGameContextFlagsException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_GAME_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one GameContext flag was selected. Only one context flag is allowed."
