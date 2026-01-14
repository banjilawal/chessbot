# src/chess/route/context/builder/exception/route.py

"""
Module: chess.rank.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_RANK_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "RankContextBuildRouteException",
]

from chess.rank import RankContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_RANK_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class RankContextBuildRouteException(RankContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the RankContext build failed because there was no build route for the Rank key.

    # PARENT:
        *   RankContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_RANK_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "RankContext build failed: No build path existed for the Rank key."