# src/chess/edge/context/builder/exception/route.py

"""
Module: chess.edge.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_EDGE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "EdgeContextBuildRouteException",
]

from chess.edge import EdgeContextException
from chess.system import ExecutionRouteException


# ======================# NO_EDGE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class EdgeContextBuildRouteException(EdgeContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the EdgeContext build failed because there was no build route for the Edge key.

    # PARENT:
        *   EdgeContextException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_EDGE_CONTEXT_BUILD_ROUTE_EXCEPTION"
    MSG = "EdgeContext build failed: No build path existed for the Edge key."