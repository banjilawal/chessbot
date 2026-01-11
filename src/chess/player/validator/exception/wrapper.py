# src/chess/player/validator/exception/_base.py

"""
Module: chess.player.validator.exception._base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.player import PlayerException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# PLAYER_VALIDATION_FAILURE EXCEPTION #======================#
    "PlayerValidationFailedException",
]


#======================# PLAYER_VALIDATION_FAILURE EXCEPTION #======================#
class PlayerValidationFailedException(PlayerException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Player. The encapsulated
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   PlayerException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PLAYER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Player validation failed."

