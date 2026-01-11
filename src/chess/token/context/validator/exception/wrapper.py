# src/chess/token/validator/exception/exception.py

"""
Module: chess.token.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import ValidationFailedException

__all__ = [
    # ======================# TOKEN_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "TokenContextValidationFailedException",
]

from chess.token import TokenContextException


# ======================# TOKEN_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class TokenContextValidationFailedException(TokenContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a TokenContext. The
        encapsulated exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   TokenContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "TokenContext validation failed."