# src/chess/player/validator/exception/wrapper.py

"""
Module: chess.player.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# PLAYER_VALIDATION_FAILURE #======================#
    "PlayerValidationException",
]


# ======================# PLAYER_VALIDATION_FAILURE #======================#
class PlayerValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in PlayerValidator.validate that, prevented A successful validation result 
        from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PLAYER_VALIDATION_FAILURE"
    MSG = "Player validation failed."
