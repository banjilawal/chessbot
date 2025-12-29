# src/chess/team/context/builder/exception/route.py

"""
Module: chess.team.context.builder.exception.route
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_TEAM_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "TeamContextBuildRouteException",
]

from chess.system import UnhandledRouteException
from chess.team import TeamContextException


# ======================# UNHANDLED_TEAM_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class TeamContextBuildRouteException(TeamContextException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that TeamContextBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use TeamContext. There are different configurations of TeamContext that are correct. Each
        configuration must have a build route to guarantee all TeamContext products are safe. If a
        TeamContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a TeamContextBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_TEAM_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The TeamContextBuilder did not handle one of the paths necessary to guarantee TeamContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )