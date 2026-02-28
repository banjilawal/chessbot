# src/chess/route/context/builder/exception/route.py

"""
Module: chess.rank.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_RANK_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "RankContextBuildRouteException",
]

from chess.rank import RankContextException
from chess.system import ExecutionRouteException


# ======================# NO_RANK_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class RankContextBuildRouteException(RankContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the RankContext build failed because there was no build route for the Rank key.

    # PARENT:
        *   RankContextException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_RANK_CONTEXT_BUILD_ROUTE_EXCEPTION"
    MSG = "RankContext build failed: No build path existed for the Rank key."