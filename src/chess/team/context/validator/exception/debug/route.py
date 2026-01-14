# src/chess/team/context/validator/exception/debug/route.py

"""
Module: chess.team.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "TeamContextValidationRouteException",
]

from chess.team import TeamContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_TEAM_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class TeamContextValidationRouteException(TeamContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the TeamContext validation failed because there was no build route for the TeamContext key.

    # PARENT:
        *   TeamContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_TEAM_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "TeamContext validation failed: No validation route was provided for the Team attribute."