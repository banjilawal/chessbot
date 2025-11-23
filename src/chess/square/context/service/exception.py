# src/chess/square/context/service/exception.py

"""
Module: chess.square.context.service.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import SearchContextServiceException

__all__ = [
    "SquareContextServiceException",
]


class SquareContextServiceException(SearchContextServiceException):
    """
     Super class of exceptions raised by SquareContextService objects. Do not use directly. Subclasses give
     precise, fined-grained, debugging info.
     """
    ERROR_CODE = "SQUARE_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareContextService raised an exception."