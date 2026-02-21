# src/chess/system/database/exception/catchall.py

"""
Module: chess.system.database.exception.catchall
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    #======================# DATABASE EXCEPTION #======================#
    "DatabaseException",
]


#======================# DATABASE EXCEPTION #======================#
class DatabaseException(ChessException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exception raised by Database objects.
    2.  Wraps an exception that hits the try-finally block of an Database object.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DATABASE_ERROR"
    DEFAULT_MESSAGE = "Database raised an exception."