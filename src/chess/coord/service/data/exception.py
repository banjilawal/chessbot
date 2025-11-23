# src/chess/coord/service/data/exception.py

"""
Module: chess.coord.service.data.__init__
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import DataServiceException


__all__ = [
    "CoordDataServiceException",
    "AddingDuplicateCoordException",
    "RemovingNullCoordException",
]


class CoordDataServiceException(DataServiceException):
    """
    Super class of exceptions raised by CoordDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordDataService raised an exception."


class AddingDuplicateCoordException(CoordDataServiceException):
    """Raised when trying to add a duplicate Coord to a list of Coords."""
    ERROR_CODE = "DUPLICATE_COORD_ADDITION_ERROR"
    DEFAULT_MESSAGE = "CoordDatatService cannot add duplicate Coords to the list."


class RemovingNullCoordException(CoordDataServiceException):
    """Raised when trying  to remove a Coord not in the list."""
    ERROR_CODE = "REMOVING_NON_EXISTENT_COORD_ERROR"
    DEFAULT_MESSAGE = "CoordDataService cannot remove a Coord not in the list."

