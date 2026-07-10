# src/operand/state/team/roster/exception/insertion/duplicate.py

"""
Module: operand.state.team.roster.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_ALREADY_ON_ROSTER EXCEPTION #======================#
    "TokenAlreadyOnTeamRosterException",
]

from operand.state.team import TeamRosterException


# ======================# TOKEN_ALREADY_ON_ROSTER EXCEPTION #======================#
class TokenAlreadyOnTeamRosterException(TeamRosterException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that adding a roster member failed because the occupant was already present.

    Super Class:
        *   TeamRosterException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_ALREADY_ON_ROSTER_EXCEPTION"
    MSG = "Adding roster member failed: The occupant was already on the roster."