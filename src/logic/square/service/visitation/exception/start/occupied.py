# src/logic/square/service/visitation/exception/start/full.py

"""
Module: logic.square.service.visitation.exception.start.full
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

__all__ = [
    # ======================# VISITING_OCCUPIED_SQUARE EXCEPTION #======================#
    "VisitingOccupiedSquareException",
]

from logic.square import SquareDebugException


# ======================# VISITING_OCCUPIED_SQUARE EXCEPTION #======================#
class VisitingOccupiedSquareException(SquareDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

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
    ERR_CODE = "VISITING_OCCUPIED_SQUARE_EXCEPTION"
    MSG = "Square visit start failed: The square was already occupied."
