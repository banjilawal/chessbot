# src/logic/coord/context/validator/exception/debug/route.py

"""
Module: logic.coord.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "CoordContextValidationRouteException",
]

from logic.coord import CoordContextException
from logic.system import ExecutionRouteException


# ======================# NO_COORD_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class CoordContextValidationRouteException(CoordContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CoordContext validation failed because there was no build route for the CoordContext key.

    # PARENT:
        *   CoordContextException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_COORD_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    MSG = "CoordContext validation failed: No validation route was provided for the Coord attribute."