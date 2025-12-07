# src/chess/square.entity_service/service/collision.py

"""
Module: chess.square.service.service.exception
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""


from chess.system import ServiceException, ValidationException, NullException

__all__ = [
    "SquareServiceException",
    "AddingDuplicateSquareException",
    "RemovingNonExistentSquareException",
]


class SquareServiceException(ServiceException):
    """
    Super class of exceptions raised by SquareService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareService raised an exception."


class AddingDuplicateSquareException(ServiceException):
    """Raised when trying to add a duplicate Square to a list of Squares."""
    ERROR_CODE = "DUPLICATE_SQUARE_ADDITION_ERROR"
    DEFAULT_MESSAGE = "SquareService cannot add duplicate Squares to the list."


class RemovingNonExistentSquareException(ServiceException):
    """Raised when trying  to remove a Square not in the list."""
    ERROR_CODE = "REMOVING_NON_EXISTENT_SQUARE_ERROR"
    DEFAULT_MESSAGE = "SquareService cannot remove a Square not in the list."