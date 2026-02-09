# src/chess/token/exception/debug.py

"""
Module: chess.token.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_DEBUG EXCEPTION #======================#
    "TokenDebugException",
]

from chess.token import TokenException
from chess.system import DebugException


# ======================# TOKEN_DEBUG EXCEPTION #======================#
class TokenDebugException(TokenException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Token operation failure.

    # PARENT:
        *   TokenException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "TOKEN_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A Token debug error occurred."