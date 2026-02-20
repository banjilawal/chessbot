# src/chess/edge/exception/debug.py

"""
Module: chess.edge.exception.debug
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# EDGE_DEBUG EXCEPTION #======================#
    "EdgeDebugException",
]

from chess.edge import EdgeException
from chess.system import DebugException


# ======================# EDGE_DEBUG EXCEPTION #======================#
class EdgeDebugException(EdgeException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Edge operation failure.

    # PARENT:
        *   EdgeException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "EDGE_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A item debug error occurred."