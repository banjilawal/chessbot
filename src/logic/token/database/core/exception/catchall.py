# src/logic/token/database/core/exception/super.py

"""
Module: logic.token.database.core.exception.super
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from logic.token import TokenException
from logic.system import StackServiceException


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
    ERR_CODE = "TOKEN_STACK_EXCEPTION"
    MSG = "TokenStack raised an exception."