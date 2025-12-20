# src/chess/game/context/number_bounds_validator/exception/exception.py

"""
Module: chess.game.context.number_bounds_validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.game import GameContextException

__all__ = [
    #======================# GAME_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidGameContextException",
]

#======================# GAME_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidGameContextException(GameContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised GameContext validation.
    2.  Wraps unhandled exception that hit the finally-block in GameContextValidator methods.
    
    # PARENT:
        *   GameContextException
        *   ValidationFailedException

    # PROVIDES:
    InvalidGameContextException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameContext validation failed."
