# src/chess/token/_context/builder/exception/route.py

"""
Module: chess.token.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_TOKEN_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "TokenContextBuildRouteException",
]

from chess.system import UnhandledRouteException
from chess.token import TokenContextException


# ======================# UNHANDLED_TOKEN_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class TokenContextBuildRouteException(TokenContextException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that TokenContextBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use TokenContext. There are different configurations of TokenContext that are correct. Each
        configuration must have a build route to guarantee all TokenContext products are safe. If a
        TokenContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a TokenContextBuildRouteException.

    # PARENT:
        *   TokenContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_TOKEN_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The TokenContextBuilder did not handle one of the paths necessary to guarantee TokenContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )