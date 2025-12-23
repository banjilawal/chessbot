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
    """Base class for above bounds exception."""
    DEFAULT_CODE = "BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Below bounds:"
