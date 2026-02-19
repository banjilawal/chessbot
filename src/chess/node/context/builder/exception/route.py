# src/chess/node/context/builder/exception/route.py

"""
Module: chess.node.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_NODE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "NodeContextBuildRouteException",
]

from chess.node import NodeContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_NODE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class NodeContextBuildRouteException(NodeContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the NodeContext build failed because there was no build route for the Node key.

    # PARENT:
        *   NodeContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_NODE_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "NodeContext build failed: No build path existed for the Node key."