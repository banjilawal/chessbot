# src/logic/token/database/exception/super.py

"""
Module: logic.token.database.exception.super
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from logic.token import TokenException
from logic.system import DatabaseException

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
    ERR_CODE = "TOKEN_DATABASE_EXCEPTION"
    MSG = "TokenDatabase raised an exception."
