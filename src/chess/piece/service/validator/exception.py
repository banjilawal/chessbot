# src/chess/piece/service/validator/base.py

"""
Module: chess.piece.service.validator.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""


from chess.piece import PieceServiceException
from chess.system import NullException, ValidationException

__all__ = [
    "InvalidPieceServiceException",
    "NullPieceServiceException",
]


# ======================# PIECE_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidPieceServiceException(PieceServiceException, ValidationException):
    """Catchall Exception for PieceServiceValidator when a candidate fails a sanity check."""
    ERROR_CODE = "PIECE_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PieceService validation failed."


# ======================# NULL PIECE_SERVICE EXCEPTIONS #======================#
class NullPieceServiceException(PieceServiceException, NullException):
    """Raised if an entity, method, or operation requires PieceService but gets null instead."""
    ERROR_CODE = "NULL_PIECE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PieceService cannot be null."
    
    



