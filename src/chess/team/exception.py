
from chess.system import (
  ChessException, TeamColorException, NameException, RollbackException
)

__all__ = [
  # ======================# TEAM EXCEPTION #======================#
  "TeamException",
]


# ======================# TEAM EXCEPTION #======================#
class TeamException(ChessException):
  """
  # ROLE: Catchall Exception

  # RESPONSIBILITIES:
  1.  Catchall for Team errors not covered by TeamException subclasses.

  # PARENT:
      *   ChessException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
  ERROR_CODE = "TEAM_ERROR"
  DEFAULT_MESSAGE = "Team raised an exception."