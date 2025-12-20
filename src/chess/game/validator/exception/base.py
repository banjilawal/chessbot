# src/chess/game/validator/exception/base.py

"""
Module: chess.game.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.game import GameException
from chess.system import ValidationFailedException

__all__ = [
    #======================# GAME VALIDATION EXCEPTION #======================#
    "InvalidGameException",
]


#======================# GAME VALIDATION EXCEPTION #======================#
class InvalidGameException(GameException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during an Game verification process.
    2.  Catchall Exception for GameValidator when a candidate fails a sanity check.
    3.  Wraps unhandled exception that hit the try-finally block of an GameValidator method.

    # PARENT:
        *   GameException
        *   ValidationFailedException

    # PROVIDES:
    InvalidGameException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Game validation failed."

