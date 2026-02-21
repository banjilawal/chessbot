# src/chess/node/context/finder/exception/wrapper.py

"""
Module: chess.node.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.node import NodeException
from chess.system import SearchException

__all__ = [
    # ======================# NODE_SEARCH_FAILURE EXCEPTION #======================#
    "NodeSearchException",
]


# ======================# NODE_SEARCH_FAILURE EXCEPTION #======================#
class NodeSearchException(NodeException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any condition that prevents a search from completing creates a debug exception that explains why the query
        failed. That debug exception is wrapped in the NodeSearchException which is the middle layer of the
        3-part exception chain.

    # PARENT:
        *   NodeException
        *   SearchException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Node search failed."
