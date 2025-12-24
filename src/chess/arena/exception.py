# src/chess/arena/exception.py

"""
Module: chess.arena.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  # ======================# ARENA EXCEPTION #======================#
  "ArenaException",
]


# ======================# ARENA EXCEPTION #======================#
class ArenaException(ChessException):
  """
  # ROLE: Catchall Exception

  # RESPONSIBILITIES:
  1.  Catchall for Arena errors not covered by ArenaException subclasses.

  # PARENT:
      *   ChessException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
  ERROR_CODE = "ARENA_ERROR"
  DEFAULT_MESSAGE = "Arena raised an exception."