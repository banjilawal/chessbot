# src/chess/team/exception.py

"""
Module: chess.team.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
  # ======================# TEAM EXCEPTION #======================#
  "TeamException",
]

from chess.system import ChessException


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