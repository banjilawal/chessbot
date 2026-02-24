# src/chess/square/context/finder/exception/dataset/null.py

"""
Module: chess.square.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from chess.square import SquareContextDebugException
from chess.system import NullException

_all__ = [
    # ======================# SQUARE_DATA_SOURCE_EMPTY EXCEPTION #======================#
    "SquareDataSourceEmptyException",
]


# ======================# SQUARE_DATA_SOURCE_EMPTY EXCEPTION #======================#
class SquareDataSourceEmptyException(SquareContextDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing SearchResult was returned because the dataset was empty.

    # PARENT:
        *   SquareContextDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_DATA_SOURCE_EMPTY_ERROR"
    DEFAULT_MESSAGE = "Square search failed: The dataset was empty."