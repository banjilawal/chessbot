# src/chess/node/context/finder/exception/dataset/null.py

"""
Module: chess.node.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.node import NodeException
from chess.system import NullDatasetException

_all__ = [
    # ======================# NODE_SEARCH_NULL_DATASET EXCEPTION #======================#
    "NodeSearchNullDatasetException",
]


# ======================# NODE_SEARCH_NULL_DATASET EXCEPTION #======================#
class NodeSearchNullDatasetException(NodeException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Node search operation failed because no dataset was provided for the query.

    # PARENT:
        *   NodeException
        *   NullDatasetException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_SEARCH_NULL_DATASET_ERROR"
    DEFAULT_MESSAGE = "Node search failed: There was no dataset to search"