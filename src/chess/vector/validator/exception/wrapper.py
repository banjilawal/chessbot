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
    1.  A debug exception is created when a Vector candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidVectorException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidVectorException chain is useful for tracing a  failure to its source.
    
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