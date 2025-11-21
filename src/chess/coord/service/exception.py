# src/chess/coord/service/collision.py

"""
Module: chess.coord.service.exception
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from chess.system import BuildFailedException, NullException, ServiceException, ValidationException

__all__ = [
    "CoordServiceException",
    
    # ====================== NULL COORD_SERVICE EXCEPTIONS #======================#
    "NullCoordServiceException",
    
    # ====================== COORD_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidCoordServiceException",
    
    # ====================== COORD_SERVICE BUILD EXCEPTIONS #======================#
    "CoordServiceBuildFailedException",
]


class CoordServiceException(ServiceException):
    """
    Super class of exceptions raised by CoordService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordService raised an exception."


# ====================== NULL COORD EXCEPTIONS #======================#
class NullCoordServiceException(CoordServiceException, NullException):
    """Raised if an entity, method, or operation requires Coord but gets null instead."""
    ERROR_CODE = "NULL_COORD_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordService cannot be null."


# ====================== COORD_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidCoordServiceException(CoordServiceException, ValidationException):
    """Catchall Exception for CoordSERVICEValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "COORD_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CoordService validation failed."
    
# ====================== COORD_SERVICE BUILD EXCEPTIONS #======================#
class CoordServiceBuildFailedException(CoordServiceException, BuildFailedException):
    """Catchall Exception for CoordServiceBuilder when it stops because of an error."""
    ERROR_CODE = "COORD_SERVICE_BUILD_FAILED"
    DEFAULT_MESSAGE = "CoordService build failed."
