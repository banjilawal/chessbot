# src/chess/hostageManifest/context/finder/exception/debug/route.py

"""
Module: chess.hostageManifest.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_HOSTAGEMANIFEST_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
    "HostageManifestSearchRouteException",
]

from chess.system import NoSearchRouteException
from chess.hostage import HostageManifestException


# ======================# UNHANDLED_HOSTAGE_MANIFEST_SEARCH_ROUTE_ROUTE EXCEPTION #======================#
class HostageManifestSearchRouteException(HostageManifestException, NoSearchRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the HostageManifest search failed because there was no search method for the HostageManifest
        attribute that was supported in the HostageManifestContext.

    # PARENT:
        *   HostageManifestException
        *   oSearchRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_HOSTAGE_MANIFEST_SEARCH_ROUTE_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "HostageManifest search failed: No search method was provided for the HostageManifest attribute."
    )