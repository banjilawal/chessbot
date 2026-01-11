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
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Team. The encapsulated
        exceptions create a chain for tracing the source of the failure.

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