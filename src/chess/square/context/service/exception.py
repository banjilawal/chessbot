# src/chess/square/map/service/exception.py

"""
Module: chess.square.map.service.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    "SquareContextServiceException",
]


class SquareContextServiceException(FinderException):
    """
     Super class of exception raised by SquareContextService objects. Do not use directly. Subclasses give
     precise, fined-grained, debugging info.
     """
    ERROR_CODE = "SQUARE_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareContextService raised an exception."