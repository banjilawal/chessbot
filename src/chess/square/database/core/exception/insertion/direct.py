# src/chess/square/database/core/exception/insertion/direct.py

"""
Module: chess.square.database.core.exception.insertion.direct
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# APPENDING_SQUARE_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
    "AppendingSquareDirectlyIntoItemsFailedException",
]

from chess.square import SquareDataServiceException


# ======================# APPENDING_SQUARE_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
class AppendingSquareDirectlyIntoItemsFailedException(SquareDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that appending the square directly into self.items was not in the list after running items.append.

    # PARENT:
        *   SquareDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "APPENDING_SQUARE_DIRECTLY_INTO_ITEMS_ERROR"
    DEFAULT_MESSAGE = "Square insertion failed: The square was not found in self.items after running self.items.append."