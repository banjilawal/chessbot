# src/chess/token/validator/exception/wrapper.py

"""
Module: chess.token.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# TOKEN_VALIDATION_FAILURE #======================#
    "TokenValidationException",
]


# ======================# TOKEN_VALIDATION_FAILURE #======================#
class TokenValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in TokenValidator.validate that, prevented A successful validation result 
        from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_VALIDATION_FAILURE"
    MSG = "Token validation failed."