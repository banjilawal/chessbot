# src/chess/board/exception.py

"""
Module: chess.board.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  # ====================== BOARD EXCEPTION #======================#
  'BoardException',
]


# ====================== BOARD EXCEPTION #======================#
class BoardException(ChessException):
  """
  # ROLE: Exception Wrapper, Catchall Exception

  # RESPONSIBILITIES:
  1.  Parent of exception raised by Board objects.
  2.  Catchall for conditions which are not covered by lower level Board exception.

  # PARENT:
      *   ChessException

  # PROVIDES:
  None

  # LOCAL ATTRIBUTES:
  None

  # INHERITED ATTRIBUTES:
  None
  """
  ERROR_CODE = "BOARD_ERROR"
  DEFAULT_MESSAGE = "Board raised an exception."