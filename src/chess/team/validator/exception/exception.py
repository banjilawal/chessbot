# src/chess/team/validator/exception/exception.py

"""
Module: chess.team.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# TEAM_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidTeamException",
]


# ======================# TEAM_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidTeamException(TeamException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Team candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidTeamException creating an exception chain. which is sent tot he caller in a
        ValidationResult.
    2.  The InvalidTeamException chain is useful for tracing a  failure to its source.

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
    ERROR_CODE = "TEAM_VALIDATION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Team validation failed."