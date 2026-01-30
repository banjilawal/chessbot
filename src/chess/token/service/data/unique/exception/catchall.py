# src/chess/token/service/data/unique/exception/catchall.py

"""
Module: chess.token.service.data.unique.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenException
from chess.system import DatabaseException

__all__ = [
    #======================# UNIQUE_TOKEN_STACK_SERVICE EXCEPTION #======================#
    "UniqueTokenDataServiceException",
]




#======================# UNIQUE_TOKEN_STACK_SERVICE EXCEPTION #======================#
class UniqueTokenDataServiceException(TokenException, DatabaseException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by TokenDatabase methods that return Result objects.

    # PARENT:
        *   TokenException
        *   DatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_TOKEN_DATABASE_CORE_ERROR"
    DEFAULT_MESSAGE = "TokenDatabase raised an exception."
