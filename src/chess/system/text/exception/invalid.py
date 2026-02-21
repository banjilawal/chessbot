# src/chess/system/text/exception/invalid.py

"""
Module: chess.system.text.exception.invalid
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import StringException, ValidationFailedException

__all__ = [
    # ======================# STRING_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidStringException",

]


# ======================# STRING_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidStringException(StringException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate That  a candidate failed String validation checks.
    2.  Wraps an exception that hits the try-finally block of a StringValidator method.

    # PARENT:
        *   StringException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "STRING_VALIDATION_FAILED_ERROR"
    DEFAULT_MESSAGE = "String validation failed."
