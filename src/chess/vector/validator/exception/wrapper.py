# src/chess/vector/validator/exception/wrapper.py

"""
Module: chess.vector.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# VECTOR_VALIDATION_FAILURE #======================#
    "VectorValidationException",
]


# ======================# VECTOR_VALIDATION_FAILURE #======================#
class VectorValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in VectorValidator.validate that, prevented A successful validation result 
        from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VECTOR_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Vector validation failed."