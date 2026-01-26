# src/chess/square/service/exception/occupant/remove/empty.py

"""
Module: chess.square.service.exception.occupant.remove.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_IS_EMPTY EXCEPTION #======================#
    "NothingToRemoveFromEmptySquareException",
]

from chess.square import SquareDebugException


# ======================# SQUARE_IS_EMPTY EXCEPTION #======================#
class NothingToRemoveFromEmptySquareException(SquareDebugException):
      
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that removing a occupant from a square failed because the square was empty.

    # PARENT:
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_IS_EMPTY_ERROR"
    DEFAULT_MESSAGE = "Removing occupant from square failed: The square was empty. Nothing to remove."