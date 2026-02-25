# src/chess/system/service/request/validator/exception/debug/null.py

"""
Module: chess.system.service.request.validator.exception..debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_REQUEST_NULL EXCEPTION #======================#
    "ServiceRequestNullException",
]

from chess.system import NullException, ServiceRequestDebugException


# ======================# SERVICE_REQUEST_NULL EXCEPTION #======================#
class ServiceRequestNullException(ServiceRequestDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the candidate was null instead
        of a ServiceRequest instance.

    # PARENT:
        *   NullException
        *   NullServiceRequestDebugException


    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SERVICE_REQUEST_NULL_ERROR"
    DEFAULT_MESSAGE = "ServiceRequest validation failed: The candidate cannot be null."