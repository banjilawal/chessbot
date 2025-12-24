# src/chess/token/validator/exception/exception.py

"""
Module: chess.token.validator.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.token import TokenException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# TOKEN_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidTokenException",
]


# ======================# TOKEN_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidTokenException(TokenException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Token candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidTokenException creating an exception chain. which is sent tot he caller in a
        ValidationResult.
    2.  The InvalidTokenException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   TokenException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_VALIDATION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Token validation failed."