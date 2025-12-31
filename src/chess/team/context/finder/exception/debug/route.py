# src/chess/team/context/finder/exception/debug/route.py

"""
Module: chess.team.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_TEAM_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "TeamSearchRouteException",
]

from chess.system import UnhandledRouteException
from chess.team import TeamException


# ======================# UNHANDLED_TEAM_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class TeamSearchRouteException(TeamException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Team search failed because there was no search method for the Team attribute that was
        supported in the TeamContext.

    # PARENT:
        *   TeamContext
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_TEAM_SEARCH_ROUTE_ROUTE_ERROR"
    DEFAULT_MESSAGE = "Team search failed: No search method was provided for the Team attribute."