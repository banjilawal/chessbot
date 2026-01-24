# src/chess/arena/exception/catchall.py

"""
Module: chess.arena.exception.catchall
Author: Banji Lawal
Created: 2025-01-24
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
  1.  Catchall for Arena and parent of exceptions raised by things Arena is responsible for.

  # PARENT:
      *   ChessException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
  ERROR_CODE = "ARENA_ERROR"
  DEFAULT_MESSAGE = "Arena raised an exception."