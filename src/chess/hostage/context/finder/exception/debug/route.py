# src/chess/hostage/context/finder/exception/debug/route.py

"""
Module: chess.hostage.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_HOSTAGE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "HostageSearchRouteException",
]

from chess.system import NoExecutionRouteException
from chess.hostage import HostageException


# ======================# NO_HOSTAGE_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class HostageSearchRouteException(HostageException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the Hostage search failed because there was no search method for the Hostage
        attribute that was supported in the HostageContext.

    # PARENT:
        *   HostageException
        *   oSearchRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_HOSTAGE_SEARCH_ROUTE_ROUTE_EXCEPTION"
    MSG = (
        "Hostage search failed: No search method was provided for the Hostage attribute."
    )