# src/chess/square/context/builder/exception/route.py

"""
Module: chess.square.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_SQUARE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "SquareContextBuildRouteException",
]

from chess.square import SquareContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_SQUARE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class SquareContextBuildRouteException(SquareContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SquareContext build failed because there was no build route for the Square key.

    # PARENT:
        *   SquareContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SQUARE_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SquareContext build failed: No build path existed for the Square key."