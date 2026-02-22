# src/chess/square/service/collision/exception/debug/duplicate.py

"""
Module: chess.square.service.collision.exception.debug.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.square import SquareStackException

__all__ = [
    # ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
    "AddingDuplicateSquareException",
]


# ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
class AddingDuplicateSquareException(SquareStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a square to teh stack failed because it was already present.

    # PARENT:
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Pushing square onto stack failed: The square is already present."