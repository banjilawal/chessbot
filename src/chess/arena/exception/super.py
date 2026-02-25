# src/chess/arena/exception.py

"""
Module: chess.arena.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# ARENA EXCEPTION #======================#
    "ArenaException",
]

from chess.system import SuperClassException


# ======================# ARENA EXCEPTION #======================#
class ArenaException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of ArenaDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "ARENA_ERROR"
    MSG = "Arena raised an exception."