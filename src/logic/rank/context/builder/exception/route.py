# src/logic/route/context/build/exception/route.py

"""
Module: logic.rank.context.build.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_RANK_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "RankContextBuildRouteException",
]

from logic.rank import RankContextException
from logic.system import ExecutionRouteException


# ======================# NO_RANK_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class RankContextBuildRouteException(RankContextException, ExecutionRouteException):
    """
    Role:Fallback Result, Debugging

    Responsibilities:
    1.  Indicate that the RankContext build failed because there was no build route for the Rank key.

    Super Class:
        *   RankContextException
        *   ExecutionRouteException

    # PROVIDES
    None


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_RANK_CONTEXT_BUILD_ROUTE_EXCEPTION"
    MSG = "RankContext build failed: No build path existed for the Rank key."