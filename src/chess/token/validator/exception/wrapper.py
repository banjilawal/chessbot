# src/chess/token/validator/exception/wrapper.py

"""
Module: chess.token.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


__all__ = [
    # ======================# TOKEN_VALIDATION_FAILURE #======================#
    "TokenValidationException",
]

from chess.token import TokenException
from chess.system import ValidationException


# ======================# TOKEN_VALIDATION_FAILURE #======================#
class TokenValidationException(TokenException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a token validation operation failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   TokenException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Token validation failed."