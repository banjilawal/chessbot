# src/logic/system/err/bounds/above.py

"""
Module: logic.system.err.bounds.above
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import BoundsException


___all__ = [
#======================# ABOVE_BOUNDS EXCEPTION #======================#
    "AboveBoundsException",
]

#======================# ABOVE_BOUNDS EXCEPTION #======================#
class AboveBoundsException(BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a value is above bounds.

    Super Class:
        *   BoundsException

    # PROVIDES:



    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "ABOVE_BOUNDS_EXCEPTION"
    MSG = "Above bounds:"