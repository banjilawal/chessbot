# src/chess/token/validator/exception/wrapper.py

"""
Module: chess.token.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


__all__ = [
    # ======================# Token_VALIDATION_FAILURE EXCEPTION #======================#
    "TokenValidationFailedException",
]

from chess.token import TokenException
from chess.system import ValidationFailedException


# ======================# Token_VALIDATION_FAILURE EXCEPTION #======================#
class TokenValidationFailedException(TokenException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Token candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an TokenValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The TokenValidationFailedException chain is useful for tracing a  failure to its source.

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
    ERROR_CODE = "Token_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Token validation failed."