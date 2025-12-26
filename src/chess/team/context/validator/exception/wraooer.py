# src/chess/team/validator/exception/exception.py

"""
Module: chess.team.validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.team import TeamException

__all__ = [
    # ======================# TEAM_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "TeamContextValidationFailedException",
]


# ======================# TEAM_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class TeamContextValidationFailedException(TeamException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a TeamContext candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an TeamContextValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The TeamContextValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   TeamContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "TeamContext validation failed."