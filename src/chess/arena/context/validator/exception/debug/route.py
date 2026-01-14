# src/chess/arena/context/validator/exception/debug/route.py

"""
Module: chess.arena.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "ArenaContextValidationRouteException",
]

from chess.arena import ArenaContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_ARENA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class ArenaContextValidationRouteException(ArenaContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the ArenaContext validation failed because there was no build route for the ArenaContext key.

    # PARENT:
        *   ArenaContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_ARENA_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "ArenaContext validation failed: No validation route was provided for the Arena attribute."