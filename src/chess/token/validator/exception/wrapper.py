# src/chess/token/validator/exception/wrapper.py

"""
Module: chess.token.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


__all__ = [
    # ======================# TOKEN_VALIDATION_FAILURE EXCEPTION #======================#
    "TokenValidationFailedException",
]

from chess.token import TokenException
from chess.system import ValidationFailedException


# ======================# TOKEN_VALIDATION_FAILURE EXCEPTION #======================#
class TokenValidationFailedException(TokenException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Token. The exception chain
        traces the ultimate source of failure.

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