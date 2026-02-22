# src/chess/square/database/core/exception/insertion/wrapper.py

"""
Module: chess.square.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_SQUARE_INSERTION_FAILURE #======================#
    "InsertingSquareInDatabaseFailedException",
]

from chess.square import SquareException
from chess.system import InsertionException


# ======================# UNIQUE_SQUARE_INSERTION_FAILURE #======================#
class InsertingSquareInDatabaseFailedException(SquareException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why inserting a unique item failed. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   SquareException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_SQUARE_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Unique Square insertion failed."