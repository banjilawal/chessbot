# src/chess/game/context/validator/exception/flag/excess.py

"""
Module: chess.game.context.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.game import InvalidGameContextException

__all__ = [
    #========================= TOO_MANY_GAME_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveGameContextFlagsException"
]

#========================= TOO_MANY_GAME_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessiveGameContextFlagsException(InvalidGameContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, GameContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Game attribute is going to be used in an GameSnapshotFinder.
    
    # PARENT:
        *   InvalidGameContextException
        *   ContextFlagCountException

    # PROVIDES:
    ExcessiveGameContextFlagsException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_GAME_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one GameContext flag was selected. Only one context flag is allowed."
