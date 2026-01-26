# src/chess/occupant/context/finder/exception/debug/route.py

"""
Module: chess.occupant.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_TOKEN_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "TokenSearchRouteException",
]

from chess.system import UnhandledRouteException
from chess.token import TokenException


# ======================# UNHANDLED_TOKEN_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class TokenSearchRouteException(TokenException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Token search failed because there was no search method for the Token attribute that was
        supported in the TokenContext.

    # PARENT:
        *   TokenContext
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_TOKEN_SEARCH_ROUTE_ROUTE_ERROR"
    DEFAULT_MESSAGE = "Token search failed: No search method was provided for the Token attribute."