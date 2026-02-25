# src/chess/system/relation/exception/super.py

"""
Module: chess.system.relation.exception.super
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

__all__ = [
    # ======================# RELATION EXCEPTION #======================#
    "RelationException",
]

from chess.system import SuperClassException


# ======================# RELATION EXCEPTION #======================#
class RelationException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of RelationDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "RELATION_ERROR"
    MSG = "Relation raised an exception."