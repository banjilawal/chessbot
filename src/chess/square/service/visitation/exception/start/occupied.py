# src/chess/square/service/visitation/exception/start/full.py

"""
Module: chess.square.service.visitation.exception.start.full
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

__all__ = [
    # ======================# VISITING_OCCUPIED_SQUARE EXCEPTION #======================#
    "VisitingOccupiedSquareException",
]

from chess.square import SquareDebugException


# ======================# VISITING_OCCUPIED_SQUARE EXCEPTION #======================#
class VisitingOccupiedSquareException(SquareDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing UpdateResult was returned because a token tried entering an occupied square.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VISITING_OCCUPIED_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square visit start failed: The square was already occupied."
