# src/chess/system/service/exception.py

"""
Module: chess.system.service.exception
Author: Banji Lawal
Created: 2025-11-19
"""

from chess.system import ChessException, NullException, ValidationFailedException, OperationFailedException

__all__ = [
    "ServiceException",
    "InvalidServiceException",
    "NullServiceException",
    "ServiceOperationFailedException",
]


#======================# SERVICE EXCEPTIONS #======================#
class ServiceException(ChessException):
    """
    Super class of exceptions raised by EntityService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SERVICE_ERROR"
    DEFAULT_MESSAGE = "EntityService raised an exception."


class InvalidServiceException(ServiceException, ValidationFailedException):
    """Raised when an EntityService fails a safety check."""
    ERROR_CODE = "SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "EntityService validation failed."


class NullServiceException(InvalidServiceException, NullException):
    """Raised when a object, module or method is expecting an EntityService but gets null instead."""
    ERROR_CODE = "NULL_SERVICE_ERROR"
    DEFAULT_MESSAGE = "EntityService cannot be null."
    

# ======================# SERVICE_OPERATION EXCEPTION #======================#
class ServiceOperationFailedException(ServiceException, OperationFailedException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates a Service's method caught an unhandled exception in its try-catch-finally block.

    # PARENT:
        *   ServiceException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SERVICE_OPERATION_ERROR"
    DEFAULT_MESSAGE = "Service operation failed."