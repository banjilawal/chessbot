# src/chess/token/validator/exception/exception.py

"""
Module: chess.token.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import ValidationException

__all__ = [
    # ======================# TOKEN_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "TokenContextValidationException",
]

from chess.token import TokenContextException


# ======================# TOKEN_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class TokenContextValidationException(TokenContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a TokenContext. The
        encapsulated exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   TokenContextException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "TokenContext validation failed."