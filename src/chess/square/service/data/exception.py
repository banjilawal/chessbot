# src/chess/square/service/data/exception.py

"""
Module: chess.square.service.data.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import DataServiceException, ServiceException, ValidationException, NullException

__all__ = [
    "SquareDataServiceException",
    "AddingDuplicateSquareException",
    "RemovingNonExistentSquareException",
]


class SquareDataServiceException(DataServiceException):
    """
    Super class of exceptions raised by SquareDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SQUARE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareDataService raised an exception."


class AddingDuplicateSquareException(SquareDataServiceException):
    """Raised when trying to add a duplicate Square to a list of Squares."""
    ERROR_CODE = "DUPLICATE_SQUARE_ADDITION_ERROR"
    DEFAULT_MESSAGE = "SquareDataService cannot add duplicate Squares to the list."


class RemovingNonExistentSquareException(SquareDataServiceException):
    """Raised when trying  to remove a Square not in the list."""
    ERROR_CODE = "REMOVING_NON_EXISTENT_SQUARE_ERROR"
    DEFAULT_MESSAGE = "SquareDataService cannot remove a Square not in the list."