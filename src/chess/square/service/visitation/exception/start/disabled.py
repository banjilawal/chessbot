# src/chess/square/service/visitation/exception/start/disabled.py

"""
Module: chess.square.service.visitation.exception.start.disabled
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_VISITOR_DISABLED EXCEPTION #======================#
    "SquareVisitorDisabledException",
]

from chess.square import SquareDebugException


# ======================# SQUARE_VISITOR_DISABLED EXCEPTION #======================#
class SquareVisitorDisabledException(SquareDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    A failing UpdateResult was returned because a disabled token attempted to occupy the square.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_VISITOR_DISABLED_EXCEPTION"
    MSG = "Square visit start failed: A disabled token cannot occupy a square."