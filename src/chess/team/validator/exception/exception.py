# src/chess/team/validator/exception/exception.py

"""
Module: chess.team.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import ValidationException

__all__ = [
    # ======================# TEAM VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidTeamException",
]


# ======================# TEAM VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidTeamException(TeamException, ValidationException):
    """Catchall Exception for TeamValidator when a candidate fails a sanity check."""
    ERROR_CODE = "TEAM_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Team validation failed."