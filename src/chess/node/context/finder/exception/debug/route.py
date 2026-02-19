# src/chess/node/context/finder/exception/debug/route.py

"""
Module: chess.node.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_NODE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "NodeSearchRouteException",
]

from chess.system import NoSearchRouteException
from chess.node import NodeException


# ======================# UNHANDLED_NODE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class NodeSearchRouteException(NodeException, NoSearchRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Node search failed because there was no search method for the Node attribute that was
        supported in the NodeContext.

    # PARENT:
        *   NodeException
        *   oSearchRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_NODE_SEARCH_ROUTE_ROUTE_ERROR"
    DEFAULT_MESSAGE = "Node search failed: No search method was provided for the Node attribute."