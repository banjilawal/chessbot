# src/chess/coord/service/data/unique.base.py

"""
Module: chess.coord.service.data.unique.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordDataServiceException


__all__ = [
    "UniqueCoordDataServiceException",
    "AddingDuplicateCoordException",
]


class UniqueCoordDataServiceException(CoordDataServiceException):
    """
    Super class of exceptions raised by UniqueCoordDataService objects. Do not
    use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "UNIQUE_COORD_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueCoordDataService raised an exception."


class AddingDuplicateCoordException(UniqueCoordDataServiceException):
    """Raised when trying to add a duplicate Coord to a list of Coords."""
    ERROR_CODE = "DUPLICATE_COORD_ADDITION_ERROR"
    DEFAULT_MESSAGE = "UniqueCoordDatatService cannot add duplicate Coords to the list."
