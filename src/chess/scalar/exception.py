# src/chess/scalar/exception.py

"""
Module: chess.scalar.exception
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from chess.system import ChessException, NullException

__all__ = [
  # ======================# SCALAR EXCEPTION #======================#
  "ScalarException",
]


# ======================# SCALAR EXCEPTION #======================#
class ScalarException(ChessException):
  """
  # ROLE: Catchall Exception

  # RESPONSIBILITIES:
  1.  Catchall for Scalar errors not covered by ScalarException subclasses.

  # PARENT:
      *   ChessException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
  ERROR_CODE = "SCALAR_ERROR"
  DEFAULT_MESSAGE = "Scalar raised an exception."