# src/chess/vector/validator/exception/exception.py

"""
Module: chess.vector.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.vector import VectorException
from chess.system import ValidationException

_
__all__ = [
    # ======================# VECTOR_VALIDATION_FAILURE #======================#
    "InvalidVectorException",
]


# ======================# VECTOR_VALIDATION_FAILURE #======================#
class InvalidVectorException(VectorException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a vector. The exception chain traces the ultimate source of failure.
    
    # PARENT:
        *   VectorException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VECTOR_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Vector validation failed."