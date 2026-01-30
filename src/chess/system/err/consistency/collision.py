# src/chess/system/err/consistency/collision.py

"""
Module: chess.system.err.consistency.collision
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# COLLISION EXCEPTION #======================#
    "CollisionException",
]

from chess.system import InconsistencyException


# ======================# COLLISION EXCEPTION #======================#
class CollisionException(InconsistencyException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a set of bag of the same class, has two bag share a value for their unique property

    # PARENT:
        *   InconsistencyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "COLLISION_ERROR"
    DEFAULT_MESSAGE = "CollisionException"