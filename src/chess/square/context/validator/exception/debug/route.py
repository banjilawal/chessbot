# src/chess/route/context/validator/exception/debug/route.py

"""
Module: chess.route.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "RouteContextValidationRouteException",
]

from chess.route import RouteContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_ROUTE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class RouteContextValidationRouteException(RouteContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the RouteContext validation failed because there was no build route for the RouteContext key.

    # PARENT:
        *   RouteContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_ROUTE_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "RouteContext validation failed: No validation route was provided for the Route attribute."