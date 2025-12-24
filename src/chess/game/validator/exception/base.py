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
    # ======================# GAME_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidGameException",
]


# ======================# GAME_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidGameException(GameException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Game candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidGameException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidGameException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   GameException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Game validation failed."