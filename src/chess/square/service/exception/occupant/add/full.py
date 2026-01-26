# src/chess/square/service/exception/occupant/add/full.py

"""
Module: chess.square.service.exception.occupant.add.full
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_IS_FULL EXCEPTION #======================#
    "CannotEnterOccupiedSquareException",
]

from chess.square import SquareDebugException


# ======================# SQUARE_IS_FULL EXCEPTION #======================#
class CannotEnterOccupiedSquareException(SquareDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a token could not enter a square because it already had an occupant.
    
    # PARENT:
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_IS_FULL_ERROR"
    DEFAULT_MESSAGE = "Token entering a square failed: The square is full."