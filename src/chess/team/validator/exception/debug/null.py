# src/chess/team/validator/exception/debug/null.py

"""
Module: chess.team.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_TEAM EXCEPTION #======================#
    "NullTeamException",
]

from chess.system import NullException
from chess.team import InvalidTeamException


# ======================# NULL_TEAM EXCEPTION #======================#
class NullTeamException(InvalidTeamException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that Team validation failed because the candidate was null.

    # PARENT:
        *   NullException
        *   InvalidTeamException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAM EXCEPTION_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The candidate was null."