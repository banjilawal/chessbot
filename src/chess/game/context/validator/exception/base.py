# src/chess/game/validator/exception/base.py

"""
Module: chess.game.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.game import GameContextException

__all__ = [
    # ======================# GAME_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidGameContextException",
]


# ======================# GAME_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidGameContextException(GameContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a GameContext candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidGameContextException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidGameContextException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   GameContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "GameContext validation failed."