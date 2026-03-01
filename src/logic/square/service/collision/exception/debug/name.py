# src/logic/square/service/collision/exception/debug/name.py

"""
Module: logic.square.service.collision.exception.debug.name
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_NAME_COLLISION EXCEPTION #======================#
    "SquareNameCollisionException",
]

from logic.square import SquareDebugException


# ======================# SQUARE_NAME_COLLISION EXCEPTION #======================#
class SquareNameCollisionException(SquareDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    At least two squares two are sharing a name that should be unique to a square.
    
    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_NAME_COLLISION_EXCEPTION"
    MSG = "Square collision detected: At least two squares have the same name."