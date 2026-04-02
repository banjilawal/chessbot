# src/logic/system/identity/id/exception.py

"""
Module: logic.system.identity.id.exception
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from logic.system import NumberException, ValidationException

__all__ = [
    # ======================# ID_VALIDATION EXCEPTION #======================#
    "IdValidationException",
]


# ======================# ID_VALIDATION EXCEPTION #======================#
class IdValidationException(NumberException, ValidationException):
    """
    Role:Exception Work

    Responsibilities:
    1.  A debug exception is created when an ID rank fails a validation test. Validation debug exceptions are
        encapsulated inside an IdValidationException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The IdValidationException chain is useful for tracing a  failure to its source.

    Super Class:
        *   NumberException
        *   ValidationException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ID_VALIDATION_EXCEPTION"
    MSG = "Id Validation failed."
