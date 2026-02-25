# src/chess/team/exception/super.py

"""
Module: chess.team.exception.super
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM EXCEPTION #======================#
    "TeamException",
]

from chess.system import SuperClassException


# ======================# TEAM EXCEPTION #======================#
class TeamException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of TeamDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "TEAM_ERROR"
    MSG = "Team raised an exception."