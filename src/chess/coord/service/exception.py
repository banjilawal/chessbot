# src/chess/coord/service/exception.py

"""
Module: chess.coord.service.exception
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    "CoordServiceException",
    "AddingDuplicateCoordException",
    "RemovingNullCoordException",
]


class CoordServiceException(DataServiceException):
    """
    Super class of exceptions raised by CoordService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordService raised an exception."


class AddingDuplicateCoordException(ServiceException):
    """Raised when trying to add a duplicate Coord to a list of Coords."""
    ERROR_CODE = "DUPLICATE_COORD_ADDITION_ERROR"
    DEFAULT_MESSAGE = "CoordService cannot add duplicate Coords to the list."


class RemovingNullCoordException(ServiceException):
    """Raised when trying  to remove a Coord not in the list."""
    ERROR_CODE = "REMOVING_NON_EXISTENT_COORD_ERROR"
    DEFAULT_MESSAGE = "CoordService cannot aremove a Coord not in the list."



    

