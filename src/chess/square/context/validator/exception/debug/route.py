# src/chess/square/context/validator/exception/debug/route.py

"""
Module: chess.square.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_SQUARE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SquareContextValidationRouteException",
]

from chess.square import SquareContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_SQUARE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SquareContextValidationRouteException(SquareContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SquareContext validation failed because there was no validation route for the
        SquareContext key.

    # PARENT:
        *   SquareContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SQUARE_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SquareContext validation failed: No validation route was provided for a SquareContext attribute."