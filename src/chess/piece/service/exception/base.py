# src/chess/piece/service/exception/exception.py

"""
Module: chess.piece.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException
from chess.piece import PieceException

__all__ = [
    # ======================# PIECE_SERVICE EXCEPTION #======================#
    "PieceServiceException",
]


# ======================# PIECE_SERVICE EXCEPTION #======================#
class PieceServiceException(PieceException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an PieceService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a PieceService method.

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
    ERROR_CODE = "PIECE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PieceService raised an exception."