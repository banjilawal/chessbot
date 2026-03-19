# src/logic/square/validator/exception/debug/collider_candidates/empty.py

"""
Module: logic.square.validator.exception.debug.collider_candidates.empty
Author: Banji Lawal
Created: 2026-02-23
"""

from logic.square import SquareDebugException


_all__ = [
    # ======================# SQUARE_DATA_SOURCE_EMPTY EXCEPTION #======================#
    "SquareDataSourceEmptyException",
]


# ======================# SQUARE_DATA_SOURCE_EMPTY EXCEPTION #======================#
class SquareDataSourceEmptyException(SquareDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing SearchResult was returned because the collider_candidates was empty.

    Super Class:
        *   SquareDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_DATA_SOURCE_EMPTY_EXCEPTION"
    MSG = "The collider_candidates of squares cannot be empty"