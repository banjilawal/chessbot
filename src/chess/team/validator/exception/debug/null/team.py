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
from chess.team import TeamException


# ======================# NULL_TEAM EXCEPTION #======================#
class NullTeamException(TeamException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Team certification because it was null.
    
    # PARENT:
        *   NullException
        *   TeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The candidate was null."