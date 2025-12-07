# src/chess/team/validator/exception/null/exception.py

"""
Module: chess.team.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.system import NullException
from chess.team import InvalidTeamException

__all__ = [
    "NullTeamException",
]


# ======================# TEAM VALIDATION EXCEPTIONS #======================#
class NullTeamException(InvalidTeamException, NullException):
    """Raised if an entity, method, or operation requires Team but gets null instead."""
    ERROR_CODE = "NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = "Team cannot be validation"

