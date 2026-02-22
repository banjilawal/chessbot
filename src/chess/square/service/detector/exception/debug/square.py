# src/chess/square/service/detector/exception/debug/square.py

"""
Module: chess.square.service.detector.exception.debug.square
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_OPENING)SQUARE_COLLISION EXCEPTION #======================#
    "SquareCoordCollisionException",
]

from chess.square import SquareStackException


# ======================# SQUARE_OPENING)SQUARE_COLLISION EXCEPTION #======================#
class SquareCoordCollisionException(SquareStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing a square onto the stack failed because its opening square was already in use.

    # PARENT:
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_OPENING)SQUARE_COLLISION_ERROR"
    DEFAULT_MESSAGE = "Pushing square failed: The opening square was already in use."