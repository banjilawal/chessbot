# src/chess/system/search/exception/route.py

"""
Module: chess.system.search.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SEARCH_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
    "NoSearchRouteException",
]

from chess.system import NoExecutionRouteException


# ======================# NO_SEARCH_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
class NoSearchRouteException(NoExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a search failed because no search routed had been implemented for selected attribute.

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_SEARCH_ROUTE_FOR_SELECTED_OPTION_ERROR"
    DEFAULT_MESSAGE = "Search failed: No search route had been implemented for selected attribute."