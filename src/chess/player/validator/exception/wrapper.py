# src/chess/owner/validator/exception/_base.py

"""
Module: chess.owner.validator.exception._base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.player import PlayerException
from chess.system import ValidationException

__all__ = [
    # ======================# PLAYER_VALIDATION_FAILURE EXCEPTION #======================#
    "PlayerValidationException",
]


#======================# PLAYER_VALIDATION_FAILURE EXCEPTION #======================#
class PlayerValidationException(PlayerException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Player. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   PlayerException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PLAYER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Player validation failed."

