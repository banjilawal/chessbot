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
    1.  Indicate that SquareContext validation failed because the there was no dataset to search.

    # PARENT:
        *   SquareSearchNullDatasetException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_SEARCH_NULL_DATASET_ERROR"
    DEFAULT_MESSAGE = "Square search failed: No dataset provided for search"