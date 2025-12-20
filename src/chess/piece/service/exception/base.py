# src/chess/piece/service/exception/exception.py

"""
Module: chess.piece.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    #======================# PIECE_SERVICE EXCEPTION #======================#
    "PieceServiceException",
]


#======================# PIECE_SERVICE EXCEPTION #======================#
class PieceServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an PieceService's organic fields or methods run into a
        condition that leads to an operation failing.
    2.  Parent of exceptions raised by classes that highly cohere with PieceService objects.
    3.  Catchall for PieceService failure states that are not covered by a lower level
        PieceService exception.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "PieceService raised an exception."