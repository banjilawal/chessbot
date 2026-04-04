# src/logic/system/err/bounds/below.py

"""
Module: logic.system.err.bounds.below
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from system import BoundsException


___all__ = [

#======================# BELOW_BOUNDS EXCEPTION #======================#
    "BelowBoundsException"
]

#======================# BELOW_BOUNDS EXCEPTION #======================#
class BelowBoundsException(BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a value is below bounds.

    Super Class:
        *   BoundsException

    # PROVIDES:



    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "BELOW_BOUNDS_EXCEPTION"
    MSG = "Below bounds:"
