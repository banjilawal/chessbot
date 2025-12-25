# src/chess/team/validator/exception/wrapper.py

"""
Module: chess.team.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# TEAM_VALIDATION_FAILURE EXCEPTION #======================#
    "TeamValidationFailedException",
]


# ======================# TEAM_VALIDATION_FAILURE EXCEPTION #======================#
class TeamValidationFailedException(TeamException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Team candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an TeamValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The TeamValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   TeamException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Team validation failed."