# src/chess/vector/validator/exception/debug/x/null.py

"""
Module: chess.vector.validator.exception.debug.x.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

# =========== VECTOR.VALIDATOR.EXCEPTION.DDEBUG.Y PACKAGE CONTENTS ===========#

# Packages
None

# Modules

__all__ = [
    # ======================# VECTOR_NULL_X_AXIS EXCEPTION #======================#
    "VectorNullXException",
]

from chess.system import NullException
from chess.vector import InvalidVectorException


# ======================# VECTOR_NULL_X_AXIS EXCEPTION #======================#
class VectorNullXException(InvalidVectorException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that Vector validation failed because the x_axis was null.

    # PARENT:
        *   NullException
        *   InvalidVectorException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "VECTOR_NULL_X_AXIS_ERROR"
    DEFAULT_MESSAGE = "Vector validation failed: The x_axis was null."