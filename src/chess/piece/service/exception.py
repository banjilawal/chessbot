# src/chess/piece/service/__init__.py

"""
Module: chess.piece.service.__init__
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


# ======================# NULL PIECE_SERVICE EXCEPTIONS #======================#
class NullPieceServiceException(PieceServiceException, NullException):
    """Raised if an entity, method, or operation requires PieceService but gets validation instead."""
    ERROR_CODE = "NULL_PIECE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PieceService cannot be validation."


# ======================# PIECE_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidPieceServiceException(PieceServiceException, ValidationException):
    """Catchall Exception for PieceServiceValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "PIECE_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PieceService validation failed."


# ====================== PIECE_SERVICE BUILD EXCEPTIONS #======================#
class PieceServiceBuildFailedException(PieceServiceException, BuildFailedException):
    """Catchall Exception for PieceServiceBuilder when it stops because of an error."""
    ERROR_CODE = "PIECE_SERVICE_BUILD_FAILED"
    DEFAULT_MESSAGE = "PieceService build failed."

