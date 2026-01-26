# src/chess/square/database/core/exception/deletion/unfound.py

"""
Module: chess.square.database.core.exception.deletion.unfound
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# SQUARE_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
    "SquareDoesNotExistForRemovalException",
]

from chess.square import SquareException


# ======================# SQUARE_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
class SquareDoesNotExistForRemovalException(SquareException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a square by a unique attribute failed because no items
        matching the property were found in the dataset.

    # PARENT:
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_DOES_NOT_EXIST_FOR_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "Square deletion failed: The square was not found in the dataset. Nothing to remove."