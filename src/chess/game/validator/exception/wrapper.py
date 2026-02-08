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
    "GameValidationFailedException",
]


# ======================# GAME_VALIDATION_FAILURE EXCEPTION #======================#
class GameValidationFailedException(GameException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Game. The exception chain traces the ultimate source of failure.

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