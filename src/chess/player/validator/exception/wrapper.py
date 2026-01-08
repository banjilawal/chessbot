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
    1.  Parent of exception raised during an Player verification process.
    2.  Catchall Exception for PlayerValidator when a candidate fails a sanity check.
    3.  Wraps an exception that hits the try-finally block of an PlayerValidator method.

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

