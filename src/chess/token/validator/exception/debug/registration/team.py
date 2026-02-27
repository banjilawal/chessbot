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
    # ======================# TOKEN_NOT_REGISTERED_WITH_TEAM EXCEPTION #======================#
    "TokenNotRegisteredTeamException",
]


# ======================# TOKEN_NOT_REGISTERED_WITH_TEAM EXCEPTION #======================#
class TokenNotRegisteredTeamException(TokenDebugException, NotRegisteredException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the candidate token had not registered with its team.

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
    ERR_CODE = "TOKEN_NOT_REGISTERED_WITH_TEAM_EXCEPTION"
    MSG = "Token validation failed: The candidate token had not registered with its team."