# src/chess/system/relation/exception/debug/debug.py

"""
Module: chess.system.relation.exception.debug.debug
Author: Banji Lawal
Created: 2025-12-28
version: 1.0.0
"""

__all__ = [
    # ======================# RELATION_DEBUG EXCEPTION #======================#
    "RelationDebugException",
]


from chess.system import DebugException, RelationException


# ======================# RELATION_DEBUG EXCEPTION #======================#
class RelationDebugException(RelationException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Relation operation failure.

    # PARENT:
        *   RelationException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "RELATION_DEBUG_ERROR"
    MSG = "A RelationDebugException was raised."