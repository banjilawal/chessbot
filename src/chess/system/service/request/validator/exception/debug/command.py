# src/chess/system/service/request/validator/exception/debug/null.py

"""
Module: chess.system.service.request.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# WRONG_OPERATION EXCEPTION #======================#
    "WrongOperationException",
]

from chess.system import ServiceRequestDebugException


# ======================# WRONG_OPERATION EXCEPTION #======================#
class WrongOperationException(ServiceRequestDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a ServiceRequest candidate failed because the request.command != operation.name.

    # PARENT:
        *  ServiceRequestDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "WRONG_OPERATION_ERROR"
    DEFAULT_MESSAGE = "ServiceRequest validation failed: request.command != operation.name."