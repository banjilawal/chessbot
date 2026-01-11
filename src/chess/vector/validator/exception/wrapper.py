# src/chess/vector/validator/exception/exception.py

"""
Module: chess.vector.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.vector import VectorException
from chess.system import ValidationFailedException

_
__all__ = [
    # ======================# VECTOR_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidVectorException",
]


# ======================# VECTOR_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidVectorException(VectorException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a vector. The encapsulated
        exceptions create a chain for tracing the source of the failure.
    
    # PARENT:
        *   VectorException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VECTOR_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Vector validation failed."