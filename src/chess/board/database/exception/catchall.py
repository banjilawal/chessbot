# src/chess/board/database/exception/catchall.py

"""
Module: chess.board.database.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# BOARD_DATABASE EXCEPTION #======================#
    "BoardDatabaseException",
]

from chess.system import DatabaseException


# ======================# BOARD_DATABASE EXCEPTION #======================#
class BoardDatabaseException(DatabaseException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an BoardDatabase encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a BoardDatabase method.

    # PARENT:
        *   DatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_DATABASE_ERROR"
    DEFAULT_MESSAGE = "BoardDatabase raised an exception."