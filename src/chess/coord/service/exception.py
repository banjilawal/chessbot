# src/chess/coord/service/base.py

"""
Module: chess.coord.entity_service.exception
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    "CoordServiceException",
]


class CoordServiceException(ServiceException):
    """
    Super class of exceptions raised by CoordService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordService raised an exception."
