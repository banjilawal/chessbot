# src/chess/coord/exception/debug.py

"""
Module: chess.coord.exception.debug
Author: Banji Lawal
Created: 2026-01-26
version: 1.0.0
"""

__all__ = [
    # ======================# COORD_DEBUG EXCEPTION #======================#
    "CoordDebugException",
]

from chess.coord import CoordException
from chess.system import DebugException


# ======================# COORD_DEBUG EXCEPTION #======================#
class CoordDebugException(CoordException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Coord operation failure.

    # PARENT:
        *   CoordException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "COORD_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A item debug error occurred."