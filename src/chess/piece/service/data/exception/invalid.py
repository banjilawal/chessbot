# src/chess/piece/service/data/exception/invalid.py

"""
Module: chess.piece.service.data.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.piece import PieceDataServiceException


__all__ = [
    #======================# PIECE_DATA_SERVICE VALIDATION EXCEPTION #======================#
    "InvalidPieceDataServiceException",
]

#======================# PIECE_DATA_SERVICE VALIDATION EXCEPTION #======================#
class InvalidPieceDataServiceException(PieceDataServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during PieceDataService verification process.
    2.  Wrap an exception that hit the try-finally block of an PieceDataServiceValidator method.

    # PARENT:
        *   PieceDataServiceException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_DATA_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PieceDataService validation failed."