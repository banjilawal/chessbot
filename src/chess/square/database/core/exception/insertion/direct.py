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

from chess.square import SquareStackException


# ======================# APPENDING_SQUARE_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
class AppendingSquareDirectlyIntoItemsFailedException(SquareStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that appending the item directly into self.bag was not in the list after running bag.append.

    # PARENT:
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "APPENDING_SQUARE_DIRECTLY_INTO_ITEMS_ERROR"
    DEFAULT_MESSAGE = "Square insertion failed: The item was not found in self.bag after running self.bag.append."