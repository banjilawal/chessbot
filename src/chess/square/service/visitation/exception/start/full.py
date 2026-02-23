# src/chess/square/service/visitation/exception/start/full.py

"""
Module: chess.square.service.visitation.exception.start.full
Author: Banji Lawal
Created: 2026-02-22
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
    1.  Indicate that a occupant could not enter a item because it already had an occupant.
    
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
    DEFAULT_MESSAGE = "Token entering a item failed: The item is full."