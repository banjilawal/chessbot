# src/chess/edge/context/finder/exception/dataset/null.py

"""
Module: chess.edge.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.edge import EdgeException
from chess.system import NullDatasetException

_all__ = [
    # ======================# EDGE_SEARCH_NULL_DATASET EXCEPTION #======================#
    "EdgeSearchNullDatasetException",
]


# ======================# EDGE_SEARCH_NULL_DATASET EXCEPTION #======================#
class EdgeSearchNullDatasetException(EdgeException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Edge search operation failed because no dataset was provided for the query.

    # PARENT:
        *   EdgeException
        *   NullDatasetException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_SEARCH_NULL_DATASET_ERROR"
    DEFAULT_MESSAGE = "Edge search failed: There was no dataset to search"