# src/chess/square/service/data/exception/deletion/unfound.py

"""
Module: chess.square.service.data.exception.deletion.unfound
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.square import SquareDataServiceException

__all__ = [
    # ======================# SQUARE_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
    "SquareDoesNotExistForRemovalException",
]


# ======================# SQUARE_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
class SquareDoesNotExistForRemovalException(SquareDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a square by a unique attribute failed because no items
        matching the property were found in the dataset.

    # PARENT:
        *   SquareDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_DOES_NOT_EXIST_FOR_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "Square deletion failed: The square was not found in the dataset. Nothing to remove."