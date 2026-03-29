# src/logic/team/roster/exception/super.py

"""
Module: logic.team.roster.exception.super
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


from logic.team import TeamException

__all__ = [
    # ======================# TEAM_ROSTER EXCEPTION #======================#
    "TeamRosterException",
]

# ======================# TEAM_ROSTER EXCEPTION #======================#
class TeamRosterException(TeamException):
    """
    Role:Super Exception
  
    Responsibilities:
    1.  Super for RosterService errors.
  
    Super Class:
        *   ChessException
  
    Provides:
  
    # ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_ROSTER_EXCEPTION"
    MSG = "RosterService raised an exception."