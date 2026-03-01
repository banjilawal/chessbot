# src/logic/captivity/context/builder/exception/route.py

"""
Module: logic.captivity.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_CAPTIVITY_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "CaptivityContextBuildRouteException",
]

from logic.hostage import CaptivityContextException
from logic.system import ExecutionRouteException


# ======================# NO_CAPTIVITY_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class CaptivityContextBuildRouteException(CaptivityContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CaptivityContext build failed because there was no build route for the Captivity key.

    # PARENT:
        *   CaptivityContextException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_CAPTIVITY_CONTEXT_BUILD_ROUTE_EXCEPTION"
    MSG = "CaptivityContext build failed: No build path existed for the Captivity key."