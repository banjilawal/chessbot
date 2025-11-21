# src/chess/square.service/service/collision.py

"""
Module: chess.square.service.service.exception
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""


from chess.system import ServiceException, ValidationException, NullException

__all__ = [
    "SquareServiceException",
    
# ======================# NULL SQUARE_SERVICE EXCEPTIONS #======================#
    "NullSquareServiceException",
    
# ======================# SQUARE_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidSquareServiceException",

# ======================# SQUARE_SERVICE BUILD EXCEPTIONS #======================#
    "SquareServiceBuildFailedException",
]


class SquareServiceException(ServiceException):
    """
    Super class of exceptions raised by SquareService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareService raised an exception."


# ======================# NULL SQUARE_SERVICE EXCEPTIONS #======================#
class NullSquareServiceException(SquareServiceException, NullException):
    """Raised if an entity, method, or operation requires SquareService but gets null instead."""
    ERROR_CODE = "NULL_SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareService cannot be null."


# ======================# SQUARE_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidSquareServiceException(SquareServiceException, ValidationException):
    """Catchall Exception for when SquareServiceValidator fails candidates on a Piece-SquareService relationship test."""
    ERROR_CODE = "INVALID_SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareService validation failed."


# ======================# SQUARE_SERVICE BUILD EXCEPTIONS #======================#
class SquareServiceBuildFailedException(SquareServiceException, BuildFailedException):
    """Catchall Exception for SquareServiceBuilder when it encounters an error building a Square."""
    ERROR_CODE = "SQUARE_SERVICE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "SquareService build failed."



