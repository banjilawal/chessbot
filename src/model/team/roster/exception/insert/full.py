# src/model/team/roster/exception/insertion/full.py

"""
Module: model.team.roster.exception.insertion.full
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ROSTER_IS_FULL EXCEPTION #======================#
    "TeamRosterIsFullException",
]

from model.team import TeamRosterException


# ======================# ROSTER_IS_FULL EXCEPTION #======================#
class TeamRosterIsFullException(TeamRosterException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that adding a item to the team failed because the roster has all sixteen tokens.

    Super Class:
        *   RosterException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ROSTER_IS_FULL_EXCEPTION"
    MSG = "Adding roster member failed: The roster has all sixteen chess pieces."