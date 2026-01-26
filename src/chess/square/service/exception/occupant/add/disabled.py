# src/chess/square/service/exception/occupant/add/disabled.py

"""
Module: chess.square.service.exception.occupant.add.disabled
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# DISABLED_TOKEN_OCCUPYING_SQUARE EXCEPTION #======================#
    "DisabledTokenOccupyingSquareException",
]

from chess.square import SquareDebugException


# ======================# DISABLED_TOKEN_OCCUPYING_SQUARE EXCEPTION #======================#
class DisabledTokenOccupyingSquareException(SquareDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a square occupation attempt failed because the occupant was disabled.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DISABLED_TOKEN_OCCUPYING_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Token entering a square failed: A disabled occupant cannot occupy a square."