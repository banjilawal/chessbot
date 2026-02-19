# src/chess/edge/context/finder/exception/wrapper.py

"""
Module: chess.edge.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.edge import EdgeException
from chess.system import SearchFailedException

__all__ = [
    # ======================# EDGE_SEARCH_FAILURE EXCEPTION #======================#
    "EdgeSearchFailedException",
]


# ======================# EDGE_SEARCH_FAILURE EXCEPTION #======================#
class EdgeSearchFailedException(EdgeException, SearchFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Any condition that prevents a search from completing creates a debug exception that explains why the query
        failed. That debug exception is wrapped in the EdgeSearchFailedException which is the middle layer of the
        3-part exception chain.

    # PARENT:
        *   EdgeException
        *   SearchFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Edge search failed."
