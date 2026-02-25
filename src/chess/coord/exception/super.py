# src/chess/coord/exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# COORD EXCEPTION #======================#
    "CoordException",
]

from chess.system import SuperClassException


# ======================# COORD EXCEPTION #======================#
class CoordException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of CoordDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "COORD_ERROR"
    MSG = "Coord raised an exception."