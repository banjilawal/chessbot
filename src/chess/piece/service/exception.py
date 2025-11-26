# src/chess/piece/service/exception.py

"""
Module: chess.piece.service.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import ServiceException, NullException, ValidationException

__all__ = [
    "PieceServiceException",
    
# ======================# NULL PIECE_SERVICE EXCEPTIONS #======================#
    "NullPieceServiceException",
    
# ======================# NULL PIECE_SERVICE EXCEPTIONS #======================#
    "InvalidPieceServiceException",
    
# ====================== PIECE_SERVICE BUILD EXCEPTIONS #======================#
    "PieceServiceBuildFailedException",
]

class PieceServiceException(ServiceException):
    """
    Super class for exceptions raised by PieceService objects. DO NOT USE DIRECTLY. Subclasses
    give more useful debugging messages.
    """
    ERROR_CODE = "PIECE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PieceService raised an exception."





# ====================== PIECE_SERVICE BUILD EXCEPTIONS #======================#
class PieceServiceBuildFailedException(PieceServiceException, BuildFailedException):
    """Catchall Exception for PieceServiceBuilder when it stops because of an error."""
    ERROR_CODE = "PIECE_SERVICE_BUILD_FAILED"
    DEFAULT_MESSAGE = "PieceService build failed."

