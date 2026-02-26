# src/chess/system/err/consistency/collision.py

"""
Module: chess.system.err.consistency.collision
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# COLLISION EXCEPTION #======================#
    "UniqueAttributeException",
]

from chess.system import DebugException


# ======================# COLLISION EXCEPTION #======================#
class UniqueAttributeException(DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a set of bag of the same class, has two bag share a value for their unique property

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "COLLISION_ERROR"
    MSG = "UniqueAttributeException"