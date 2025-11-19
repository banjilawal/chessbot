# src/chess/piece/stack/service/exception.py

"""
Module: chess.piece.stack.service.exception
Author: Banji Lawal
Created: 2025-11-18
version: 1.0.0
"""

# src/chess/piece/stack/exception.py

"""
Module: chess.piece.stack.exception
Author: Banji Lawal
Created: 2025-09-30
version: 1.0.0
"""

from chess.system import ServiceException, ValidationException, NullException

__all__ = [
    "CoordStackServiceException",
    
    # ======================# NULL COORD_STACK_SERVICE EXCEPTIONS #======================#
    "NullCoordStackServiceException",
    
    # ======================# COORD_STACK_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidCoordStackServiceException",
    "CannotRunServiceWithoutCoordStackException",
    
    # ======================# COORD_STACK_SERVICE OPERATION EXCEPTIONS #======================#
    "PoppingEmptyCoordStackException",
    "PushingDuplicateCoordException",
    "PushingNullException",
    
    # ======================# COORD_STACK_SERVICE EXCEPTIONS #======================#
    "CoordStackServiceServiceException",
    
    # ======================# NULL COORD_STACK_SERVICE EXCEPTIONS #======================#
    "NullCoordStackServiceServiceException",
    
    # ======================# COORD_STACK_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidCoordStackServiceServiceException",
]


class CoordStackServiceException(ServiceException):
    """
    Super class for exceptions raised by CoordStackService objects. DO NOT USE DIRECTLY. Subclasses
    give more useful debugging messages.
    """
    ERROR_CODE = "COORD_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordStackService raised an exception."


# ======================# NULL COORD_STACK_SERVICE EXCEPTIONS #======================#
class NullCoordStackServiceException(CoordStackServiceException, NullException):
    """Raised if an entity, method, or operation requires CoordStackService but gets null instead."""
    ERROR_CODE = "NULL_COORD_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordStackService cannot be null."


# ======================# COORD_STACK_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidCoordStackServiceException(CoordStackServiceException, ValidationException):
    """Catchall Exception for CoordStackServiceValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "COORD_STACK_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CoordStackService validation failed."


class CannotRunServiceWithoutCoordStackException(CoordStackServiceException):
    """Raised if the service does not have a CoordStack."""
    ERROR_CODE = "NO_COORD_STACK_FOR_SERVICE_ERROR"
    DEFAULT_MESSAGE = (
        "The service does not have a CoordStack to manage. CoordStackService"
        " requires a CoordStack."
    )


# ======================# COORD_STACK_SERVICE OPERATION EXCEPTIONS #======================#
class PoppingEmptyCoordStackException(CoordStackServiceException):
    """Raised when trying to pop from an empty CoordStackService."""
    ERROR_CODE = "POPPING_EMPTY_STACK_ERROR"
    DEFAULT_MESSAGE = "Cannot pop from an empty CoordStackService."


class PushingDuplicateCoordException(CoordStackServiceException):
    """Raised when trying to push the same coord onto the stack."""
    ERROR_CODE = "PUSHING_DUPLICATE_COORD_ERROR"
    DEFAULT_MESSAGE = "Cannot push duplicate coord onto the stack. All Coords must be unique."


class PushingNullException(CoordStackServiceException):
    """Raised when trying to push null item to stack."""
    ERROR_CODE = "PUSHING_NULL_ERROR"
    DEFAULT_MESSAGE = "Cannot push null item onto a CoordStackService."


CannotUndoPreviousTurnException
# ======================# COORD_STACK_SERVICE EXCEPTIONS #======================#
class CoordStackServiceServiceException(ChessException):
    """
    Super class for exceptions raised by CoordStackServiceService objects. DO NOT USE DIRECTLY. Subclasses
    give more useful debugging messages.
    """
    ERROR_CODE = "COORD_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordStackServiceService raised an exception."


# ======================# NULL COORD_STACK_SERVICE EXCEPTIONS #======================#
class NullCoordStackServiceServiceException(CoordStackServiceServiceException, NullException):
    """Raised if an entity, method, or operation requires CoordStackServiceService but gets null instead."""
    ERROR_CODE = "NULL_COORD_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordStackServiceService cannot be null."


# ======================# COORD_STACK_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidCoordStackServiceServiceException(CoordStackServiceServiceException, ValidationException):
    """Catchall Exception for CoordStackServiceServiceValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "COORD_STACK_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CoordStackServiceService validation failed."

