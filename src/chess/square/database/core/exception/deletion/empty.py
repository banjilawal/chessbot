# src/chess/square/database/core/exception/deletion/empty.py

"""
Module: chess.square.database.core.core.exception.deletion.empty
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.square import SquareException

__all__ = [
    # ======================# POPPING_EMPTY_SQUARE_STACK EXCEPTION #======================#
    "PoppingEmptySquareStackException",
]


# ======================# POPPING_EMPTY_SQUARE_STACK EXCEPTION #======================#
class PoppingEmptySquareStackException(SquareException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a square failed because the stack was empty

    # PARENT:
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_SQUARE_STACK_ERROR"
    DEFAULT_MESSAGE = "Square deletion failed: SquareDataService does not own any squares."