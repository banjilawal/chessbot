# src/chess/team/validator/exception/wrapper.py

"""
Module: chess.team.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import ValidationException

__all__ = [
    # ======================# TEAM_VALIDATION_FAILURE #======================#
    "TeamValidationException",
]


# ======================# TEAM_VALIDATION_FAILURE #======================#
class TeamValidationException(TeamException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Team. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   TeamException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Team validation failed."