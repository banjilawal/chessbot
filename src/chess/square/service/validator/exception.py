# src/chess/square.service/service/collision.py

"""
Module: chess.square.service.service.exception
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""


from chess.square import SquareServiceException
from chess.system import ValidationException, NullException


__all__ = [
    "InvalidSquareServiceException",
    "NullSquareServiceException",
]


# ======================# SQUARE_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidSquareServiceException(SquareServiceException, ValidationException):
    """Catchall Exception for when SquareServiceValidator fails candidates on a Piece-SquareService relationship test."""
    ERROR_CODE = "INVALID_SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareService validation failed."
    

class NullSquareServiceException(SquareServiceException, NullException):
    """Raised if an entity, method, or operation requires SquareService but gets validation instead."""
    ERROR_CODE = "NULL_SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareService cannot be validation."
