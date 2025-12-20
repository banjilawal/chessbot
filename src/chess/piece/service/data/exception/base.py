# src/chess/piece/service/data/exception/exception.py

"""
Module: chess.piece.service.data.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    #======================# PIECE_DATA_SERVICE EXCEPTION #======================#
    "PieceDataServiceException",
]


#======================# PIECE_DATA_SERVICE EXCEPTION #======================#
class PieceDataServiceException(DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by either PieceDataService objects.
    2.  Catchall for PieceDataService failure states that are not covered by a lower level
        PieceDataService exception.

    # PARENT:
        *   DataServiceException

    # PROVIDES:
    PieceDataServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_DATA_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "PieceDataService raised an exception."