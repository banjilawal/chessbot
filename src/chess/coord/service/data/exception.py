# src/chess/coord/entity_service/data/base.py

"""
Module: chess.coord.entity_service.data.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import DataServiceException


__all__ = [
    "CoordDataServiceException",
    "RemovingNullCoordException",
]


class CoordDataServiceException(DataServiceException):
    """
    Super class of exceptions raised by CoordDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordDataService raised an exception."


class RemovingNullCoordException(CoordDataServiceException):
    """Raised when trying  to remove a Coord not in the list."""
    ERROR_CODE = "REMOVING_NON_EXISTENT_COORD_ERROR"
    DEFAULT_MESSAGE = "CoordDataService cannot remove a Coord not in the list."

