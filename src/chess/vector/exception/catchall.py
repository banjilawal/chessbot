# src/chess/vector/exception/catchall.py

"""
Module: chess.vector.exception.catchall
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  # ======================# VECTOR EXCEPTION #======================#
  "VectorException",
]


# ======================# VECTOR EXCEPTION #======================#
class VectorException(ChessException):
  """
  # ROLE: Catchall Exception

  # RESPONSIBILITIES:
  1.  Catchall for Vector errors not covered by VectorException subclasses.

  # PARENT:
      *   ChessException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
  ERROR_CODE = "VECTOR_ERROR"
  DEFAULT_MESSAGE = "Vector raised an exception."














