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
    # ======================# TOKEN_NOT_REGISTERED_WITH_TEAM EXCEPTION #======================#
    "TokenNotRegisteredTeamException",
]


# ======================# TOKEN_NOT_REGISTERED_WITH_TEAM EXCEPTION #======================#
class TokenNotRegisteredTeamException(TokenDebugException, NotRegisteredException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing ValidationResult was returned because the rank token had not registered with its team.

    Super Class:
        *   TokenDebugException
        *   NotRegisteredException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_NOT_REGISTERED_WITH_TEAM_EXCEPTION"
    MSG = "Token validation failed: The rank token had not registered with its team."