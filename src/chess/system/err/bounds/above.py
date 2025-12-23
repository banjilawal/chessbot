# src/chess/system/err/bounds/above.py

"""
Module: chess.system.err.bounds.above
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BoundsException


___all__ = [
#======================# ABOVE_BOUNDS EXCEPTION #======================#
    "AboveBoundsException",
]

#======================# ABOVE_BOUNDS EXCEPTION #======================#
class AboveBoundsException(BoundsException):
    """Base class for above bounds exception."""
    DEFAULT_CODE = "ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Above bounds:"