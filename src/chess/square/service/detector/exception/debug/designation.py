# src/chess/square/service/detector/exception/debug/designation.py

"""
Module: chess.square.service.detector.exception.debug.designation
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_DESIGNATION_COLLISION EXCEPTION #======================#
    "SquareDesignationCollisionException",
]

from chess.square import SquareStackException


# ======================# SQUARE_DESIGNATION_COLLISION EXCEPTION #======================#
class SquareDesignationCollisionException(SquareStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing a square onto the stack failed because its designation was already in use.

    # PARENT:
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_DESIGNATION_COLLISION_ERROR"
    DEFAULT_MESSAGE = "Pushing square failed: The designation was already in use."