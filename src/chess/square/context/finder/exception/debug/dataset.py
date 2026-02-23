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
    # ======================# SQUARE_DATASET_NOT_PROVIDED EXCEPTION #======================#
    "SquareDatasetNotProvidedException",
]


# ======================# SQUARE_DATASET_NOT_PROVIDED EXCEPTION #======================#
class SquareDatasetNotProvidedException(SquareContextDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing SearchResult was returned because no dataset was provided for the query.

    # PARENT:
        *   SquareContextDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_DATASET_NOT_PROVIDED_ERROR"
    DEFAULT_MESSAGE = "Square search failed: No dataset was provided for the query."