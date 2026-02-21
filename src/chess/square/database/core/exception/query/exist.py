# src/chess/square/database/core/exception/query/exist.py

"""
Module: chess.square.database.core.exception.query.exist
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""



__all__ = [
    # ======================# SQUARE_NOT_FOUND EXCEPTION #======================#
    "SquareNotFoundException",
]

from chess.square import SquareDebugException


# ======================# SQUARE_NOT_FOUND EXCEPTION #======================#
class SquareNotFoundException(SquareDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   NullException
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "Square deletion failed: The item was not found in the dataset. Nothing to remove."