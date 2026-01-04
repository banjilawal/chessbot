__all__ = [
    # ======================# TEAM_ROSTER EXCEPTION #======================#
    "TeamRosterException",
]

from chess.team import TeamException


# ======================# TEAM_ROSTER EXCEPTION #======================#
class TeamRosterException(TeamException):
    """
    # ROLE: Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Catchall for Team.roster errors.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    None
  
    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = "Team.roster raised an exception."