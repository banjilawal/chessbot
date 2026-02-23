# src/chess/token/database/core/exception/catchall.py

"""
Module: chess.token.database.core.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenException
from chess.system import StackServiceException


__all__ = [
    # ======================# TOKEN_STACK EXCEPTION #======================#
    "TokenStackException",
]

# ======================# TOKEN_STACK EXCEPTION #======================#
class TokenStackException(TokenException, StackServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by TokenStack methods that return Result objects.

    # PARENT:
        *   TokenException
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_STACK_ERROR"
    DEFAULT_MESSAGE = "TokenStack raised an exception."