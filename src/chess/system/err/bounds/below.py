# src/chess/system/err/bounds.py

"""
Module: chess.system.err.bounds
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from chess.system import BoundsException


___all__ = [

#======================# BELOW_BOUNDS EXCEPTION #======================#
    "BelowBoundsException"
]

#======================# BELOW_BOUNDS EXCEPTION #======================#
class BelowBoundsException(BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a value is below bounds.

    # PARENT:
        *   ChessException

    # PROVIDES:


    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Below bounds:"
