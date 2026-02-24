# src/chess/arena/validator/exception/wrapper.py

"""
Module: chess.arena.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# ARENA_VALIDATION_FAILURE #======================#
    "ArenaValidationException",
]


# ======================# ARENA_VALIDATION_FAILURE #======================#
class ArenaValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in ArenaValidator.validate that, prevented ValidationResult.success() 
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
    ERROR_CODE = "ARENA_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Arena validation failed."