# src/logic/vector/validator/exception/debug/x/below.py

"""
Module: logic.vector.validator.exception.debug.x.below
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# VECTOR_X_BELOW_BOUNDS EXCEPTION #======================#
    "VectorXBelowBoundsException",
]

from logic.system import BoundsException
from logic.vector import InvalidVectorException


# ======================# VECTOR_X_BELOW_BOUNDS EXCEPTION #======================#
class VectorXBelowBoundsException(InvalidVectorException, BoundsException):
    """
    A Vector with a component whose magnitude > 7 will cause an ArrayIndexOutOfBounds error when the Vector is
    added or subtracted from a Coord.
    """
    ERR_CODE = "VECTOR_X_BELOW_BOUNDS_EXCEPTION"
    MSG = (
        "Vector validation failed: x_axis below bounds."
    )