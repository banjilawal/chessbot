# src/logic/system/build/exception/route.py

"""
Module: logic.system.build.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_BUILD_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
    "ExecutionRouteException",
]

from logic.system import ExecutionRouteException


# ======================# NO_BUILD_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
class NoExecutionRouteException(ExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Super Exception

    # RESPONSIBILITIES:
    1.  Indicate that a build failed because there was no execution route for the specified option.

    # PARENT:
        *   ExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_BUILD_ROUTE_FOR_SELECTED_OPTION_EXCEPTION"
    MSG = "Build failed: No build route was defined for the specified option."