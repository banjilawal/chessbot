# src/chess/team/validator/exception/wrapper.py

"""
Module: chess.team.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# TEAM_VALIDATION_FAILURE #======================#
    "TeamValidationException",
]


# ======================# TEAM_VALIDATION_FAILURE #======================#
class TeamValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in TeamValidator.validate that, prevented ValidationResult.success() 
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
    ERROR_CODE = "TEAM_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Team validation failed."