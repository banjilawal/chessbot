# src/chess/square/database/core/exception/insertion/wrapper.py

"""
Module: chess.square.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_INSERTION_FAILURE #======================#
    "SquareInsertionFailedException",
]

from chess.square import SquareException
from chess.system import InsertionFailedException


# ======================# SQUARE_INSERTION_FAILURE #======================#
class SquareInsertionFailedException(SquareException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that add a occupant to the roster failed.

    # PARENT:
        *   SquareException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_INSERTION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Square insertion failed."