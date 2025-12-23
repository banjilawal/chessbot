# src/chess/system/err/bounds/base.py

"""
Module: chess.system.err.boundsbase
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
    """Base class for out of Bounds errors."""
    DEFAULT_CODE = "OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Out of bounds:"