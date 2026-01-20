# src/chess/team/roster/exception/insertion/duplicate.py

"""
Module: chess.team.roster.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_ALREADY_ON_ROSTER EXCEPTION #======================#
    "TokenAlreadyOnTeamRosterException",
]

from chess.team import TeamRosterException, TeamException


# ======================# TOKEN_ALREADY_ON_ROSTER EXCEPTION #======================#
class TokenAlreadyOnTeamRosterException(TeamRosterException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a roster member failed because the token was already present.

    # PARENT:
        *   TeamRosterException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_ALREADY_ON_ROSTER_ERROR"
    DEFAULT_MESSAGE = "Adding roster member failed: The token was already on the roster."