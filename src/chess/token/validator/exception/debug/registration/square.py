# src/chess/token/validator/exception/debug/registration/__init__.py

"""
Module: chess.token.validator.exception.debug.registration.__init__
Author: Banji Lawal
Created: 2026-01-08
version: 1.0.0
"""

from chess.token import TokenDebugException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# TOKEN_NOT_REGISTERED_WITH_SQUARE EXCEPTION #======================#
    "TokenNotRegisteredSquareException",
]


# ======================# TOKEN_NOT_REGISTERED_WITH_SQUARE EXCEPTION #======================#
class TokenNotRegisteredSquareException(TokenDebugException, NotRegisteredException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the candidate token had not registered with its square.

    # PARENT:
        *   TokenDebugException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_NOT_REGISTERED_WITH_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Token validation failed: The candidate token had not registered with its square."