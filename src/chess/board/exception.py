# src/chess/board/exception.py

"""
Module: chess.board.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  # ======================# BOARD EXCEPTION #======================#
  "BoardException",
]


# ======================# BOARD EXCEPTION #======================#
class BoardException(ChessException):
  """
  # ROLE: Catchall Exception

  # RESPONSIBILITIES:
  1.  Catchall for Board errors not covered by BoardException subclasses.

  # PARENT:
      *   ChessException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
  ERROR_CODE = "BOARD_ERROR"
  DEFAULT_MESSAGE = "Board raised an exception."