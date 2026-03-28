# src/logic/scalar/validation/exception/work.py

"""
Module: logic.scalar.validation.exception.work
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from logic.system import ValidationException

__all__ = [
    # ======================# SCALAR_VALIDATION_FAILURE #======================#
    "ScalarValidationException",
]


# ======================# SCALAR_VALIDATION_FAILURE #======================#
class ScalarValidationException(ValidationException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  An error occurred in ScalarValidationTransaction.validate that, prevented A successful validation result
        from being returned.

    Super Class:
        *   ValidationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SCALAR_VALIDATION_FAILURE"
    MSG = "Scalar validation failed."