# src/chess/square/service/data/base.py

"""
Module: chess.square.entity_service.data.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import DataServiceException, NullException

__all__ = [
    "SquareDataServiceException",
    "RemovingNonExistentSquareException",
]


class SquareDataServiceException(DataServiceException):
    """
    Super class of exceptions raised by SquareDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SQUARE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareDataService raised an exception."


class RemovingNonExistentSquareException(SquareDataServiceException, NullException):
    """Raised when trying  to remove a Square not in the list."""
    ERROR_CODE = "REMOVING_NON_EXISTENT_SQUARE_ERROR"
    DEFAULT_MESSAGE = "SquareDataService cannot remove a Square not in the list."