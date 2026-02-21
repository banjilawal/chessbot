# src/chess/token/database/exception/catchall.py

"""
Module: chess.token.database.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenException
from chess.system import DatabaseException

__all__ = [
    #======================# TOKEN_DATABASE EXCEPTION #======================#
    "TokenDatabaseException",
]




#======================# TOKEN_DATABASE EXCEPTION #======================#
class TokenDatabaseException(TokenException, DatabaseException):
    """
    # ROLE: Exception Wrapper

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
    ERROR_CODE = "TOKEN_DATABASE_ERROR"
    DEFAULT_MESSAGE = "TokenDatabase raised an exception."
