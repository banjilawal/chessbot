# src/chess/vector/validator/exception/debug/x/above.py

"""
Module: chess.vector.validator.exception.debug.x.above
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# VECTOR_X_ABOVE_BOUNDS EXCEPTION #======================#
    "VectorXAboveBoundsException",
]

from chess.system import BoundsException
from chess.vector import InvalidVectorException


# ======================# VECTOR_X_ABOVE_BOUNDS EXCEPTION #======================#
class VectorXAboveBoundsException(InvalidVectorException, BoundsException):
    """
    A Vector with a component whose magnitude > 7 will cause an ArrayIndexOutOfBounds error when the Vector is
    added or subtracted from a Coord.
    """
    ERROR_CODE = "VECTOR_X_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = (
        "Vector validation failed: x_axis above bounds."
    )
