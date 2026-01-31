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

from chess.square import SquareStackException


# ======================# SQUARE_TO_DELETE_NOT_FOUND EXCEPTION #======================#
class SquareToDeleteNotFoundException(SquareStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
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
    DEFAULT_MESSAGE = "Square deletion failed: The item was not found in the dataset. Nothing to remove."