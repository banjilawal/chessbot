# src/chess/square/exception/super.py

"""
Module: chess.square.exception.super
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE EXCEPTION #======================#
    "SquareException",
]

from chess.system import SuperClassException


# ======================# SQUARE EXCEPTION #======================#
class SquareException(SuperClassException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Layer-0 of Exception chain which is the Parent of SquareDebugException

    # PARENT:
        *   SuperClassException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_ERROR"
    MSG = "Square raised an exception."