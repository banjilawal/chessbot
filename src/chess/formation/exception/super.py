# src/chess/formation/exception.py

"""
Module: chess.formation.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# FORMATION EXCEPTION #======================#
    "FormationException",
]

from chess.system import SuperClassException


# ======================# FORMATION EXCEPTION #======================#
class FormationException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of FormationDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "FORMATION_ERROR"
    MSG = "Formation raised an exception."