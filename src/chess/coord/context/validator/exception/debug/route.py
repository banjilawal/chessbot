# src/chess/coord/context/validator/exception/debug/route.py

"""
Module: chess.coord.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.coord import CoordContextException

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "CoordContextValidationRouteException",
]

from chess.coord import CoordContextException
from chess.system import UnhandledRouteException


# ======================# UNHANDLED_COORD_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class CoordContextValidationRouteException(CoordContextException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CoordContext validation failed because there was no build route for the CoordContext key.

    # PARENT:
        *   CoordException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_COORD_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "CoordContext validation failed: No validation route was provided for the Coord attribute."