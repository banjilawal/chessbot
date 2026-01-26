# src/chess/square/database/exception/insertion/duplicate.py

"""
Module: chess.square.database.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.square import SquareDatabaseException

__all__ = [
    # ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
    "AddingDuplicateSquareException",
]


# ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
class AddingDuplicateSquareException(SquareDatabaseException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a item to the SquareDatabase's dataset failed because it was
        already present.

    # PARENT:
        *   SquareDatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Unique Square insertion failed: The square is already present."