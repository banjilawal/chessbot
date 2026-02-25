# src/chess/team/validator/exception/null.py

"""
Module: chess.team.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_TEAM EXCEPTION #======================#
    "NullTeamException",
]

from chess.system import NullException
from chess.team import TeamDebugException


# ======================# NULL_TEAM EXCEPTION #======================#
class NullTeamException(TeamDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the candidate was null instead of a Team.

    # PARENT:
        *   TeamDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The candidate cannot be null."