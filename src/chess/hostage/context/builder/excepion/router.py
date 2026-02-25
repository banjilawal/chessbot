# src/chess/captivity/context/builder/exception/route.py

"""
Module: chess.captivity.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_CAPTIVITY_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "CaptivityContextBuildRouteException",
]

from chess.hostage import CaptivityContextException
from chess.system import NoExecutionRouteException


# ======================# NO_CAPTIVITY_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class CaptivityContextBuildRouteException(CaptivityContextException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CaptivityContext build failed because there was no build route for the Captivity key.

    # PARENT:
        *   CaptivityContextException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_CAPTIVITY_CONTEXT_BUILD_ROUTE_ERROR"
    MSG = "CaptivityContext build failed: No build path existed for the Captivity key."