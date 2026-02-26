# src/chess/system/relation/exception/super.py

"""
Module: chess.system.relation.exception.super
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# RELATION_EXCEPTION #======================#
    "RelationException",
]

from chess.system import SuperClassException


# ======================# RELATION_EXCEPTION #======================#
class RelationException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of RelationDebugException
