# src/chess/square/context/validator/exception/debug/route.py

"""
Module: chess.square.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import UnhandledRouteException
from chess.square import SquareContextException

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SquareContextValidationRouteException",
]


# ======================# UNHANDLED_SQUARE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SquareContextValidationRouteException(SquareContextException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SquareContext validation failed because there was no build route for the SquareContext key.

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
    ERROR_CODE = "UNHANDLED_SQUARE_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SquareContext validation failed: No validation route was provided for the Square attribute."