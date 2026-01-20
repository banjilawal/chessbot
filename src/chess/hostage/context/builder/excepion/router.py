# src/chess/captivity/context/builder/exception/route.py

"""
Module: chess.captivity.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_CAPTIVITY_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "CaptivityContextBuildRouteException",
]

from chess.captivity import CaptivityContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_CAPTIVITY_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class CaptivityContextBuildRouteException(CaptivityContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CaptivityContext build failed because there was no build route for the Captivity key.

    # PARENT:
        *   CaptivityContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_CAPTIVITY_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "CaptivityContext build failed: No build path existed for the Captivity key."