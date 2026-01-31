# src/chess/token/database/core/exception/catchall.py

"""
Module: chess.token.database.core.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenException
from chess.system import DataServiceException


__all__ = [
    # ======================# TOKEN_STACK_SERVICE EXCEPTION #======================#
    "TokenDataServiceException",
]

# ======================# TOKEN_STACK_SERVICE EXCEPTION #======================#
class TokenDataServiceException(TokenException, DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

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
    ERROR_CODE = "TOKEN_DATABASE_CORE_ERROR"
    DEFAULT_MESSAGE = "TokenStack raised an exception."