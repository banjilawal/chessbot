# src/chess/arena/exception.py

"""
Module: chess.game.arena.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  # ====================== ARENA EXCEPTION #======================#
  'ArenaException',
]


# ====================== ARENA EXCEPTION #======================#
class ArenaException(ChessException):
  """
  # ROLE: Exception Wrapper, Catchall Exception

  # RESPONSIBILITIES:
  1.  Parent of exceptions raised by Arena objects.
  2.  Catchall for conditions which are not covered by lower level Arena exceptions.

  # PARENT:
      *   ChessException

  # PROVIDES:
  None

  # LOCAL ATTRIBUTES:
  None

  # INHERITED ATTRIBUTES:
  None
  """
  ERROR_CODE = "ARENA_ERROR"
  DEFAULT_MESSAGE = "Arena raised an exception."