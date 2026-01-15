# src/chess/square/context/finder/exception/dataset/null.py

"""
Module: chess.square.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import NullDatasetException

_all__ = [
    # ======================# SQUARE_SEARCH_NULL_DATASET EXCEPTION #======================#
    "SquareSearchNullDatasetException",
]


# ======================# SQUARE_SEARCH_NULL_DATASET EXCEPTION #======================#
class SquareSearchNullDatasetException(SquareException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Square search operation failed because no dataset was provided for the query.

    # PARENT:
        *   SquareException
        *   NullDatasetException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_SEARCH_NULL_DATASET_ERROR"
    DEFAULT_MESSAGE = "Square search failed: There was no dataset to search"