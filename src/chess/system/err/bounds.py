# src/chess/system/err/bounds.py

"""
Module: chess.system.err.bounds
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from chess.system import ChessException


___all__ = [
#======================# BOUNDS EXCEPTION #======================#
    "BoundsException",
#======================# ABOVE BOUNDS EXCEPTION #======================#
    "AboveBoundsException",
#======================# BELOW BOUNDS EXCEPTION #======================#
    "BelowBoundsException"
]


#======================# BOUNDS EXCEPTION #======================#
class BoundsException(ChessException):
    """Base class for out of Bounds errors."""
    DEFAULT_CODE = "OUT_OF__BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Out of bounds."


#======================# ABOVE BOUNDS EXCEPTION #======================#
class AboveBoundsException(BoundsException):
    """Base class for above bounds exception."""
    DEFAULT_CODE = "ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Above bounds."


#======================# BELOW BOUNDS EXCEPTION #======================#
class BelowBoundsException(BoundsException):
    """Base class for above bounds exception."""
    DEFAULT_CODE = "BELOW_BOUNDS_RROR"
    DEFAULT_MESSAGE = "Below bounds."
