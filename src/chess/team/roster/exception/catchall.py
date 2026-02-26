# src/chess/team/roster/exception/super.py

"""
Module: chess.team.roster.exception.super
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


from chess.team import TeamException

__all__ = [
    # ======================# TEAM_ROSTER EXCEPTION #======================#
    "TeamRosterException",
]

# ======================# TEAM_ROSTER EXCEPTION #======================#
class TeamRosterException(TeamException):
    """
    # ROLE: Super Exception
  
    # RESPONSIBILITIES:
    1.  Super for RosterService errors.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    None
  
    # ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_ROSTER_ERROR"
    MSG = "RosterService raised an exception."