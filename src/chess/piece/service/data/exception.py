# src/chess/piece/service/data/exception/exception.py

"""
Module: chess.piece.service.data.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# PIECE_DATA_SERVICE EXCEPTION #======================#
    "PieceDataServiceException",
]

from chess.piece import PieceException
from chess.system import ServiceException


# ======================# PIECE_DATA_SERVICE EXCEPTION #======================#
class PieceDataServiceException(PieceException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an PieceDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a PieceDataService method.

    # PARENT:
        *   ServiceException
        *   PieceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PieceDataService raised an exception."