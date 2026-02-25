# src/chess/vector/exception.py

"""
Module: chess.vector.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# VECTOR EXCEPTION #======================#
    "VectorException",
]

from chess.system import SuperClassException


# ======================# VECTOR EXCEPTION #======================#
class VectorException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of VectorDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "VECTOR_ERROR"
    MSG = "Vector raised an exception."