# src/chess/game/map/validator/exception/base.py

"""
Module: chess.game.map.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.game import GameContextException

__all__ = [
    #======================# GAME_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidGameContextException",
]

#======================# GAME_CONTEXT VALIDATION EXCEPTION #======================#
class InvalidGameContextException(GameContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised GameContext validation.
    2.  Wraps an exception that hits the try-finally-block in GameContextValidator methods.
    
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
