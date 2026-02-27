# src/chess/team/context/finder/exception/debug/route.py

"""
Module: chess.team.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

__all__ = [
    # ======================# NO_TEAM_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "TeamSearchRouteException",
]

from chess.system import NoExecutionRouteException
from chess.team import TeamException


# ======================# NO_TEAM_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class TeamSearchRouteException(TeamException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Team search failed because there was no search method for the Team attribute that was
        supported in the TeamContext.

    # PARENT:
        *   TeamContext
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_TEAM_SEARCH_ROUTE_ROUTE_EXCEPTION"
    MSG = "Team search failed: No search method was provided for the Team attribute."