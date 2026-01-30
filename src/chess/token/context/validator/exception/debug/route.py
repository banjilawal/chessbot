# src/chess/token/context/validator/exception/debug/route.py

"""
Module: chess.token.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "TokenContextValidationRouteException",
]

from chess.token import TokenContextException
from chess.system import NoValidationRouteException



# ======================# UNHANDLED_TOKEN_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class TokenContextValidationRouteException(TokenContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the TokenContext validation failed because there was no build route for the TokenContext key.

    # PARENT:
        *   TokenContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_TOKEN_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "TokenContext validation failed: No validation route was provided for the Token attribute."