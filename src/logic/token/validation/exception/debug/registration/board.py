# src/logic/token/validation/exception/debug/registration/__init__.py

"""
Module: logic.token.validation.exception.debug.registration.__init__
Author: Banji Lawal
Created: 2026-01-08
version: 1.0.0
"""

from logic.token import TokenDebugException
from logic.system import NotRegisteredException

__all__ = [
    # ======================# TOKEN_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
    "TokenNotRegisteredBoardException",
]


# ======================# TOKEN_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
class TokenNotRegisteredBoardException(TokenDebugException, NotRegisteredException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing ValidationResult was returned because the candidate token had not registered with its board.

    Super Class:
        *   TokenDebugException
        *   NotRegisteredException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_NOT_REGISTERED_WITH_BOARD_EXCEPTION"
    MSG = "Token validation failed: The candidate token had not registered with its board."