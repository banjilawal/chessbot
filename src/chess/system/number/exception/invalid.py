# src/chess/system/number/exception/invalid.py

"""
Module: chess.system.number.exception.invalid
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import NumberException, ValidationFailedException

__all__ = [
    "InvalidNumberException",
]


# ====================== NUMBER VALIDATION EXCEPTION #======================#
class InvalidNumberException(NumberException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an existing object violates Number integrity constraints.
    2.  Wraps unhandled exceptions that hit the finally-block in number validating methods.

    # PARENT:
        *   NumberException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NUMBER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Number validation failed."
