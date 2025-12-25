# src/chess/system/service/validator/exception/null/builder.py

"""
Module: chess.system.service.validator.exception.null.builder
Author: Banji Lawal
Created: 2025-11-18
"""

__all__ = [
    # ======================# SERVICE_NULL_BUILDER EXCEPTION #======================#
    "ServiceNullBuilderException",
]

from chess.system import NullException, ServiceException


# ======================# SERVICE_NULL_BUILDER EXCEPTION #======================#
class ServiceNullBuilderException(ServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Service certification because its builder was null.

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
    ERROR_CODE = "SERVICE_NULL_BUILDER"
    DEFAULT_MESSAGE = "Service validation failed: The candidate's builder was null."