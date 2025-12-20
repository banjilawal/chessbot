# src/chess/game/context/validator/exception/flag.py

"""
Module: chess.game.context.validator.exception.flag
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.game import InvalidGameContextException

__all__ = [
    #========================= NO_GAME_CONTEXT_FLAG EXCEPTION =========================#
    "ZeroGameContextFlagsException",
]


#========================= NO_GAME_CONTEXT_FLAG EXCEPTION =========================#
class ZeroGameContextFlagsException(InvalidGameContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no GameContext flag is provided with a searcher value.
    
    # PARENT:
        *   InvalidGameContextException
        *   ContextFlagCountException

    # PROVIDES:
    ZeroGameContextFlagsException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_GAME_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No GameContext flag was selected. A context flag must be turned on with a target value."
