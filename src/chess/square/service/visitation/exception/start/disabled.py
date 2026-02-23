# src/chess/square/service/visitation/exception/start/disabled.py

"""
Module: chess.square.service.visitation.exception.start.disabled
Author: Banji Lawal
Created: 2026-02-22
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
    1.  Indicate that a item occupation attempt failed because the occupant was disabled.

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
    DEFAULT_MESSAGE = "Token entering a item failed: A disabled occupant cannot occupy a item."