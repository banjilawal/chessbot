# src/chess/rank/factory/exception/route.py

"""
Module: chess.rank.factory.exception.route
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.system import NoBuildRouteException, ResultException

__all__ = [
    # ======================# UNHANDLED_RANK_BUILD_ROUTE EXCEPTION #======================#
    "RankBuildRouteException",
]


# ======================# UNHANDLED_RANK_BUILD_ROUTE EXCEPTION #======================#
class RankBuildRouteException(ResultException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that RankFactory did not handle one of the product build paths. The factory does not 
        have a production line for all the concrete Rank products. last step in the logic will return a
        BuildResult containing a RankBuildRouteException.

    # PARENT:
        *   ResultException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_RANK_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The RankFactory does not have a production line for all concrete Rank classes. Ensure all build branches a"
        "re covered to prevent the execution flow from hit the default failure result outside the if-blocks."
    )