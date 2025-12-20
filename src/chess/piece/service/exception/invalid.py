# src/chess/piece/service/exception/invalid.py

"""
Module: chess.piece.service.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.piece import PieceServiceException


__all__ = [
    #======================# PIECE_SERVICE VALIDATION EXCEPTION #======================#
    "InvalidPieceServiceException",
]

#======================# PIECE_SERVICE VALIDATION EXCEPTION #======================#
class InvalidPieceServiceException(PieceServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during PieceService verification process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an PieceServiceValidator method.

    # PARENT:
        *   PieceServiceException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PieceService validation failed."