# src/chess/coord/context/builder/exception/route.py

"""
Module: chess.coord.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_COORD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "CoordContextBuildRouteException",
]

from chess.coord import CoordContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_COORD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class CoordContextBuildRouteException(CoordContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CoordContext build failed because there was no build route for the Coord key.

    # PARENT:
        *   CoordContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_COORD_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "CoordContext build failed: No build path existed for the Coord key."