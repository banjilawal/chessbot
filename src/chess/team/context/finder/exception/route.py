# src/chess/team/finder/exception/route.py

"""
Module: chess.team.finder.exception.route
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
    1.  Indicate that TeamSearcher did not handle one of the paths necessary to assure a candidate is a
        safe to use TeamContext. There are different configurations of TeamContext that are correct. Each
        configuration must have a build route to guarantee all TeamContext products are safe. If a
        TeamContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a TeamSearchRouteException.

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
    DEFAULT_MESSAGE = (
        "The TeamSearcher did not handle one of the paths necessary to guarantee TeamContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )