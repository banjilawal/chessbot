# src/chess/system/service/request/validator/exception/debug/null.py

"""
Module: chess.system.service.request.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# NUMBER_OF_ARGUMENTS EXCEPTION #======================#
    "NumberOfArgumentsException",
]

from chess.system import ServiceRequestDebugException


# ======================# NUMBER_OF_ARGUMENTS EXCEPTION #======================#
class NumberOfArgumentsException(ServiceRequestDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a ServiceRequest candidate failed because the len(request.params) != len(operation.arguments)

    # PARENT:
        *  ServiceRequestDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NUMBER_OF_ARGUMENTS_ERROR"
    MSG = "ServiceRequest validation failed: len(request.params) != len(operation.arguments)."