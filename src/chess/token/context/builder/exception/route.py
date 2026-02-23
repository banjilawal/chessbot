# src/chess/token/context/builder/exception/route.py

"""
Module: chess.token.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_TOKEN_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "TokenContextBuildRouteException",
]

from chess.token import TokenContextException
from chess.system import NoExecutionRouteException


# ======================# NO_TOKEN_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class TokenContextBuildRouteException(TokenContextException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the TokenContext build failed because there was no build route for the Token key.

    # PARENT:
        *   TokenContextException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_TOKEN_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "TokenContext build failed: No build path existed for the Token key."