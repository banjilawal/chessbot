# src/chess/team/context/builder/exception/route.py

"""
Module: chess.team.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_TEAM_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "TeamContextBuildRouteException",
]

from chess.team import TeamContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_TEAM_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class TeamContextBuildRouteException(TeamContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the TeamContext build failed because there was no build route for the Team key.

    # PARENT:
        *   TeamContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_TEAM_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "TeamContext build failed: No build path existed for the Team key."