# src/logic/system/err/bounds/anchor.py

"""
Module: logic.system.err.bounds.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import DebugException

___all__ = [
#======================# OUT_OF_BOUNDS EXCEPTION #======================#
    "BoundsException",
]


#======================# BOUNDS EXCEPTION #======================#
class BoundsException(DebugException):
    """
    Role:Error Tracing, Debugging, Super Exception
    
    Responsibilities:
    1.  Indicate that a value is out of bounds.
    2.  Super for conditions which are not covered by BoundsException subclasses.

    Super Class:
        *   ChessException

    # PROVIDES:
    


    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "OUT_OF_BOUNDS_EXCEPTION"
    MSG = "Out of bounds:"