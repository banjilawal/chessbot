# src/chess/vector/validator/exception/bounds/exception.py

"""
Module: chess.vector.validator.exception.bounds.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BoundsException
from chess.vector import InvalidVectorException

__all__ = [
    "VectorAboveBoundsException",
    "VectorBelowBoundsException",
]


# ======================# VECTOR BOUNDS EXCEPTIONS #======================#  
class VectorAboveBoundsException(InvalidVectorException, BoundsException):
    """
    A Vector with a component whose magnitude > 7 will cause an ArrayIndexOutOfBounds error when the Vector is
    added or subtracted from a Coord.
    """
    ERROR_CODE = "VECTOR_ABOVE_BOUNDS"
    DEFAULT_MESSAGE = (
        "Vector is above bounds. Arithmetic rollback with a Coord will produce a "
        "Coord whose row or column value is outside the Board's range."
    )


class VectorBelowBoundsException(InvalidVectorException):
    """
    A Vector with a component whose magnitude < -7 will cause an ArrayIndexOutOfBounds error when the Vector is
    added or subtracted from a Coord.
    """
    ERROR_CODE = "VECTOR_BELOW_BOUNDS_EXCEPTION"
    DEFAULT_MESSAGE = (
        "Vector is below bounds. Arithmetic rollback with a Coord will produce a "
        "Coord whose row or column value is outside the Board's range."
    )