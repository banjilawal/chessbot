# src/logic/token/context/validator/exception/debug/route.py

"""
Module: logic.token.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "TokenContextValidationRouteException",
]

from logic.token import TokenContextException
from logic.system import ExecutionRouteException



# ======================# NO_TOKEN_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class TokenContextValidationRouteException(TokenContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the TokenContext validation failed because there was no build route for the TokenContext key.

    # PARENT:
        *   TokenContextException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_TOKEN_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    MSG = "TokenContext validation failed: No validation route was provided for the Token attribute."