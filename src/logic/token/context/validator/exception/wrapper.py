# src/logic/token/validator/exception/exception.py

"""
Module: logic.token.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from logic.system import ValidationException

__all__ = [
    # ======================# TOKEN_CONTEXT_VALIDATION_FAILURE #======================#
    "TokenContextValidationException",
]

from logic.token import TokenContextException


# ======================# TOKEN_CONTEXT_VALIDATION_FAILURE #======================#
class TokenContextValidationException(TokenContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a token_context validation operation failed. The exception chain
        traces the ultimate source of failure.

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
    ERR_CODE = "TOKEN_CONTEXT_VALIDATION_FAILURE"
    MSG = "TokenContext validation failed."