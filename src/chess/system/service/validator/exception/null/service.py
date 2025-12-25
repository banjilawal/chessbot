# src/chess/system/service/validator/exception/null/service.py

"""
Module: chess.system.service.validator.exception.null.service
Author: Banji Lawal
Created: 2025-11-18
"""

__all__ = [
    # ======================# NULL_SERVICE EXCEPTION #======================#
    "NullServiceException",
]

from chess.system import NullException, ServiceException


# ======================# NULL_SERVICE EXCEPTION #======================#
class NullServiceException(ServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Service certification because it was null.

    # PARENT:
        *   NullException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SERVICE_ERROR"
    DEFAULT_MESSAGE = "Service validation failed: The candidate was null."