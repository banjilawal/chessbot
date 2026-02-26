# src/chess/system/err/route.py

"""
Module: chess.system.err.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional


__all__ = [
    # ======================# NO_EXECUTION_ROUTE_FOR_OPTION EXCEPTION #======================#
    "NoExecutionRouteException",
]

from chess.system import DebugException

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
    ERR_CODE = "NO_EXECUTION_ROUTE_FOR_OPTION_ERROR"
    MSG = "No execution route exists for the operation option."
    