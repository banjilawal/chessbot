# src/chess/vector/validator/exception/exception.py

"""
Module: chess.vector.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.vector import VectorException
from chess.system import ValidationException


__all__ = [
    "InvalidVectorException",
]

#======================# VECTOR VALIDATION EXCEPTIONS #======================#

class InvalidVectorException(VectorException, ValidationException):
    """Catchall Exception for VectorValidator when a candidate fails a sanity check.""""""
    ERROR_CODE = "VECTOR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Vector validation failed."
