# src/chess/coord/context/service/exception.py

"""
Module: chess.coord.context.service.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import ServiceException


__all__ = ["CoordContextServiceException"]


class CoordContextServiceException(ServiceException):
    """
    Super class of exception raised by CoordContextService objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordContextService raised an exception."