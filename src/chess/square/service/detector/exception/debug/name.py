# src/chess/square/service/detection/exception/debug/name.py

"""
Module: chess.square.service.detection.exception.debug.name
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_NAME_COLLISION EXCEPTION #======================#
    "SquareNameCollisionException",
]

from chess.square import SquareStackException


# ======================# SQUARE_NAME_COLLISION EXCEPTION #======================#
class SquareNameCollisionException(SquareStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that inserting a item failed because the name was already in use by a collection member.

    # PARENT:
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_NAME_COLLISION_ERROR"
    DEFAULT_MESSAGE = "Square push failed: Another item is already using the name."