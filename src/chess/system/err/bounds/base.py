# src/chess/system/err/bounds/base.py

"""
Module: chess.system.err.bounds.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException


___all__ = [
#======================# OUT_OF_BOUNDS EXCEPTION #======================#
    "BoundsException",
]


#======================# BOUNDS EXCEPTION #======================#
class BoundsException(ChessException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  Indicate that a value is out of bounds.
    2.  Catchall for conditions which are not covered by BoundsException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Out of bounds:"