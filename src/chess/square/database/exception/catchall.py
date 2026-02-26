# src/chess/square/database/exception/super.py

"""
Module: chess.square.database.exception.super
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# SQUARE_DATABASE EXCEPTION #======================#
    "SquareDatabaseException",
]

from chess.system import DatabaseException

# ======================# SQUARE_DATABASE EXCEPTION #======================#
class SquareDatabaseException(DatabaseException):
    """
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a failure occurred in SquareDatabase.
    2.  The method where the error occurred is identified in the exception nested directly underneath.

    # PARENT:
        *   DatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_DATABASE_ERROR"
    MSG = "SquareDatabase raised an exception."