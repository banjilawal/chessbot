# src/chess/system/service/request/validator/exception/debug/null.py

"""
Module: chess.system.service.request.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_REQUEST_NULL EXCEPTION #======================#
    "ServiceRequestNullException",
]

from chess.system import ServiceRequestDebugException


# ======================# SERVICE_REQUEST_NULL EXCEPTION #======================#
class ServiceRequestNullException(ServiceRequestDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a ServiceRequest candidate failed the not-null validation test.

    # PARENT:
        *   NullException
        *   ServiceRequestDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SERVICE_REQUEST_NULL_ERROR"
    MSG = "ServiceRequest validation failed: The candidate cannot be null."