# src/logic/vector/validator/exception/debug/y/below.py

"""
Module: logic.vector.validator.exception.debug.y.below
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# VECTOR_Y_BELOW_BOUNDS EXCEPTION #======================#
    "VectorYBelowBoundsException",
]

from logic.system import BoundsException
from logic.vector import InvalidVectorException


# ======================# VECTOR_Y_BELOW_BOUNDS EXCEPTION #======================#
class VectorYBelowBoundsException(InvalidVectorException, BoundsException):
    """
    A Vector with a component whose magnitude > 7 will cause an ArrayIndexOutOfBounds error when the Vector is
    added or subtracted from a Coord.
    """
    from __future__ import annotations
    from typing import Optional
    ERR_CODE = "VECTOR_Y_BELOW_BOUNDS_EXCEPTION"
    MSG = (
        "Vector validation failed: y_axis below bounds."
    )
