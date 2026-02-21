# src/chess/token/database/core/exception/catchall.py

"""
Module: chess.token.database.core.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# TOKEN_STACK_SERVICE EXCEPTION #======================#
    "RankQuotaManagerException",
]

from chess.system import ChessException


# ======================# TOKEN_STACK_SERVICE EXCEPTION #======================#
class RankQuotaManagerException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by TokenStack methods that return Result objects.

    # PARENT:
        *   TokenException
        *   StackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_STACK_ERROR"
    DEFAULT_MESSAGE = "TokenStack raised an exception."