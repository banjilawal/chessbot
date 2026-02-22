# src/chess/square/service/detection/exception/debug/id.py

"""
Module: chess.square.service.detection.exception.debug.id
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_ID_COLLISION EXCEPTION #======================#
    "SquareIdCollisionException",
]

from chess.square import SquareStackException


# ======================# SQUARE_ID_COLLISION EXCEPTION #======================#
class SquareIdCollisionException(SquareStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that inserting a item failed because the id was already in use by a collection member.

    # PARENT:
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_ID_COLLISION_ERROR"
    DEFAULT_MESSAGE = "Square push failed: Another item is already using the id."