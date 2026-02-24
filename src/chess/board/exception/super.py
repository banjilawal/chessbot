# src/chess/board/exception.py

"""
Module: chess.board.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD EXCEPTION #======================#
    "BoardException",
]

from chess.system import SuperClassException


# ======================# BOARD EXCEPTION #======================#
class BoardException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of BoardDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERROR_CODE = "BOARD_ERROR"
    DEFAULT_MESSAGE = "Board raised an exception."