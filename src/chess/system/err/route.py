# src/chess/system/err/route.py

"""
Module: chess.system.err.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import DebugException

__all__ = [
    # ======================# NO_EXECUTION_ROUTE_FOR_OPTION EXCEPTION #======================#
    "NoExecutionRouteException",
]


# ======================# NO_EXECUTION_ROUTE_FOR_OPTION EXCEPTION #======================#
class NoExecutionRouteException(DebugException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an operation failed because there was no coverage for at least one of its optional
        success paths.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_EXECUTION_ROUTE_FOR_OPTION_ERROR"
    DEFAULT_MESSAGE = "No execution route exists for the operation option."
    