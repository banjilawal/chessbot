# src/chess/token/validator/exception/null.py

"""
Module: chess.token.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_TOKEN EXCEPTION #======================#
    "NullTokenException",
]

from chess.system import NullException
from chess.token import TokenDebugException


# ======================# NULL_TOKEN EXCEPTION #======================#
class NullTokenException(TokenDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the validation candidate was null.

    # PARENT:
        *   TokenDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TOKEN_ERROR"
    DEFAULT_MESSAGE = "Token validation failed: The validation candidate cannot be null."