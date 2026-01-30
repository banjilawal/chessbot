# src/chess/square/database/exception/occupant/add/unfound.py

"""
Module: chess.square.database.exception.occupant.add.unfound
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_TO_OCCUPY_NOT_FOUND EXCEPTION #======================#
    "SquareToOccupyNotFoundException",
]

from chess.square import SquareDatabaseException


# ======================# SQUARE_TO_OCCUPY_NOT_FOUND EXCEPTION #======================#
class SquareToOccupyNotFoundException(SquareDatabaseException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a token could not occupy a item because the item was not found in the database.

    # PARENT:
        *   SquareDatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_TO_OCCUPY_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = (
        "Square occupation failed: The item was not found in the database. Nothing for the token to occupy."
    )