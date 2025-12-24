# src/chess/square_name.service/service/collision.py

"""
Module: chess.square_name.service.service.exception
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""


from chess.system import ServiceException
from chess.square import SquareException

__all__ = [
    # ======================# SQUARE_SERVICE EXCEPTION #======================#
    "SquareServiceException",
    "AddingDuplicateSquareException",
    "RemovingNonExistentSquareException",
]


# ======================# SQUARE_SERVICE EXCEPTION #======================#
class SquareServiceException(SquareException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SquareService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SquareService method.

    # PARENT:
        *   ServiceException
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
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