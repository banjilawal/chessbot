# src/logic/system/text/exception/invalid.py

"""
Module: logic.system.text.exception.invalid
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import StringException, ValidationException

__all__ = [
    # ======================# STRING_VALIDATION_FAILURE #======================#
    "InvalidStringException",

]


# ======================# STRING_VALIDATION_FAILURE #======================#
class InvalidStringException(StringException, ValidationException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Indicate That  a candidate failed String validation checks.
    2.  Wraps an exception that hits the try-finally block of a StringValidationProcess method.

    Super Class:
        *   StringException
        *   ValidationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "STRING_VALIDATION_FAILED_EXCEPTION"
    MSG = "String validation failed."
