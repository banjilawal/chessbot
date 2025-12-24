# src/chess/piece/service/exception/invalid.py

"""
Module: chess.piece.service.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceOperationFailedException
from chess.piece import PieceServiceException

__all__ = [
    # ======================# PIECE_SERVICE_OPERATION EXCEPTION #======================#
    "PieceServiceOperationFailedException",
]


# ======================# PIECE_SERVICE_OPERATION EXCEPTION #======================#
class PieceServiceOperationFailedException(PieceServiceException, ServiceOperationFailedException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate That  a PieceService's method caught an unhandled exception in its try-catch-finally block.

    # PARENT:
        *   PieceServiceException
        *   ServiceOperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_SERVICE_OPERATION_ERROR"
    DEFAULT_MESSAGE = "PieceService operation failed."