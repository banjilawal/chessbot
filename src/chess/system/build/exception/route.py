# src/chess/system/build/exception/route.py

"""
Module: chess.system.build.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_BUILD_ROUTE_FOR_OPTION EXCEPTION #======================#
    "NoBuildRouteException",
]

from chess.system import NoExecutionRouteException


# ======================# NO_BUILD_ROUTE_FOR_OPTION EXCEPTION #======================#
class NoBuildRouteException(NoExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an operation failed because there was no coverage for at least one of its optional
        success paths.

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_BUILD_ROUTE_FOR_OPTION_ERROR"
    DEFAULT_MESSAGE = "Build failed: No build route exists for option."