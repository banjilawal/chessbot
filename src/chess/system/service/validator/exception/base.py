# src/chess/system/service/validator/exception/base.py

"""
Module: chess.system.service.validator.exception.base
Author: Banji Lawal
Created: 2025-11-18
"""

from chess.system import ServiceException, ValidationFailedException
__all__ = [
    # ======================# SERVICE_VALIDATION EXCEPTION #======================#
    "InvalidServiceException",
]


#======================# SERVICE_VALIDATION EXCEPTION #======================#
class InvalidServiceException(ServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates a candidate failed validation checks for a Service (not null and correct type)
    2.  Wraps an exception that hits the try-finally block of a Validator method.

    # PARENT:
        *   ServiceException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Service validation failed."