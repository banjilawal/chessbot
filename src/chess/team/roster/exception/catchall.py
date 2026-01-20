# src/chess/team/roster/exception/catchall.py

"""
Module: chess.team.roster.exception.catchall
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
    # ROLE: Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Catchall for RosterService errors.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    None
  
    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = "RosterService raised an exception."