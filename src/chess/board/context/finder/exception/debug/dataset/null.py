# src/chess/board/context/finder/exception/dataset/null.py

"""
Module: chess.board.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.board import BoardException
from chess.system import NullDatasetException

_all__ = [
    # ======================# BOARD_SEARCH_NULL_DATASET EXCEPTION #======================#
    "BoardSearchNullDatasetException",
]


# ======================# BOARD_SEARCH_NULL_DATASET EXCEPTION #======================#
class BoardSearchNullDatasetException(BoardException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Board search operation failed because no dataset was provided for the query.

    # PARENT:
        *   BoardException
        *   NullDatasetException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SEARCH_NULL_DATASET_ERROR"
    DEFAULT_MESSAGE = "Board search failed: There was no dataset to search"