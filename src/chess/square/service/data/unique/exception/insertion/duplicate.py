# src/chess/square/service/data/unique/exception/insertion/duplicate.py

"""
Module: chess.square.service.data.unique.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.square import UniqueSquareDataServiceException

__all__ = [
    # ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
    "AddingDuplicateSquareException",
]


# ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
class AddingDuplicateSquareException(UniqueSquareDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a square to the UniqueSquareDataService's dataset failed because the square was
        already in the collection

    # PARENT:
        *   UniqueSquareDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Unique square insertion failed: The square is already in the collection."