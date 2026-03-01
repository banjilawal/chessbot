# src/logic/square/validator/exception/debug/dataset/empty.py

"""
Module: logic.square.validator.exception.debug.dataset.empty
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
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing SearchResult was returned because the dataset was empty.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_DATA_SOURCE_EMPTY_EXCEPTION"
    MSG = "The dataset of squares cannot be empty"