# src/chess/square/service/collision/exception/debug/id.py

"""
Module: chess.square.service.collision.exception.debug.id
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_ID_COLLISION EXCEPTION #======================#
    "SquareIdCollisionException",
]

from chess.square import SquareDebugException


# ======================# SQUARE_ID_COLLISION EXCEPTION #======================#
class SquareIdCollisionException(SquareDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    At least two squares two are sharing a id that should be unique to a square.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_ID_COLLISION_EXCEPTION"
    MSG = "Square collision detected: At least two squares have the same id."