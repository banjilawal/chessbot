# src/chess/system/err/base.py

"""
Module: chess.system.err.base
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from chess.system import ChessException


___all__ = [
    "BoundsException",
    "AboveBoundsException",
    "BelowBoundsException"
]


class BoundsException(ChessException):
    """Base class for out of Bounds errors."""
    DEFAULT_CODE = "OUT_OF__BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Out of bounds."


class AboveBoundsException(BoundsException):
    """Base class for above bounds exceptions."""
    DEFAULT_CODE = "ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Above bounds."


class BelowBoundsException(BoundsException):
    """Base class for above bounds exceptions."""
    DEFAULT_CODE = "BELOW_BOUNDS_RROR"
    DEFAULT_MESSAGE = "Below bounds."
