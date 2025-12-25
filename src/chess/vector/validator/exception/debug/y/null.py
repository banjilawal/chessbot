# src/chess/vector/validator/exception/debug/y/null.py

"""
Module: chess.vector.validator.exception.debug.y.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# VECTOR_NULL_Y_AXIS EXCEPTION #======================#
    "VectorNullYException",
]

from chess.system import NullException
from chess.vector import InvalidVectorException


# ======================# VECTOR_NULL_Y_AXIS EXCEPTION #======================#
class VectorNullYException(InvalidVectorException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that Vector validation failed because the y_axis was null.

    # PARENT:
        *   NullException
        *   InvalidVectorException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "VECTOR_NULL_Y_AXIS_ERROR"
    DEFAULT_MESSAGE = "Vector validation failed: The y_axis was null."