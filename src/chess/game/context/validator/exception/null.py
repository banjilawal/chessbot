# src/chess/game/context/number_bounds_validator/exception/null.py

"""
Module: chess.game.context.number_bounds_validator.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.game import InvalidGameContextException

__all__ = [
    #======================# GAME_CONTEXT NULL EXCEPTION #======================#
    "NullGameContextException",
]

#======================# GAME_CONTEXT NULL EXCEPTION #======================#
class NullGameContextException(InvalidGameContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an GameContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an GameContext but receives null instead.
    
    # PARENT:
        *   InvalidGameContextException
        *   NullGameContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "GameContext cannot be null."
    
    
    