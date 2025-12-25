# src/chess/system/service/validator/exception/null/validator.py

"""
Module: chess.system.service.validator.exception.null.validator
Author: Banji Lawal
Created: 2025-11-18
"""

__all__ = [
    # ======================# SERVICE_NULL_VALIDATOR EXCEPTION #======================#
    "ServiceNullValidatorException",
]

from chess.system import NullException, ServiceException


# ======================# SERVICE_NULL_VALIDATOR EXCEPTION #======================#
class ServiceNullValidatorException(ServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Service certification because its validator was null.

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
    ERROR_CODE = "SERVICE_NULL_VALIDATOR"
    DEFAULT_MESSAGE = "Service validation failed: The candidate's validator was null."