# src/chess/coord/context/builder/exception/route.py

"""
Module: chess.coord.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_COORD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "CoordContextBuildRouteException",
]

from chess.coord import CoordContextException
from chess.system import NoExecutionRouteException


# ======================# NO_COORD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class CoordContextBuildRouteException(CoordContextException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CoordContext build failed because there was no build route for the Coord key.

    # PARENT:
        *   CoordContextException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_COORD_CONTEXT_BUILD_ROUTE_EXCEPTION"
    MSG = "CoordContext build failed: No build path existed for the Coord key."