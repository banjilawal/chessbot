# src/chess/square/database/core/exception/deletion/unfound.py

"""
Module: chess.square.database.core.exception.deletion.unfound
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# SQUARE_TO_DELETE_NOT_FOUND EXCEPTION #======================#
    "SquareToDeleteNotFoundException",
]

from chess.square import SquareDataServiceException


# ======================# SQUARE_TO_DELETE_NOT_FOUND EXCEPTION #======================#
class SquareToDeleteNotFoundException(SquareDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a square by a unique attribute failed because no items
        matching the property were found in the dataset.

    # PARENT:
        *   SquareDataServceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_TO_DELETE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "Square deletion failed: The square was not found in the dataset. Nothing to remove."