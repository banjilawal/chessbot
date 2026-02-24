# src/chess/scalar/exception.py

"""
Module: chess.scalar.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# SCALAR EXCEPTION #======================#
    "ScalarException",
]

from chess.system import SuperClassException


# ======================# SCALAR EXCEPTION #======================#
class ScalarException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of ScalarDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERROR_CODE = "SCALAR_ERROR"
    DEFAULT_MESSAGE = "Scalar raised an exception."