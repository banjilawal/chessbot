# src/logic/square/database/core/handler/crud/collision/exception/debug/coord.py

"""
Module: logic.square.database.core.handler.crud.collision.exception.debug.coord
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_COORD_COLLISION EXCEPTION #======================#
    "SquareCoordCollisionException",
]

from logic.square import SquareDebugException


# ======================# SQUARE_COORD_COLLISION EXCEPTION #======================#
class SquareCoordCollisionException(SquareDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    At least two squares two are sharing a coord that should be unique to a square.

    Super Class:
        *   SquareDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_COORD_COLLISION_EXCEPTION"
    MSG = "Square collision detected: At least two squares have the same coord."