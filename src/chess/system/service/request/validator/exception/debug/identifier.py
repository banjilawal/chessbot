# src/chess/system/service/request/validator/exception/debug/null.py

"""
Module: chess.system.service.request.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# IDENTIFIER_NOT_FOUND EXCEPTION #======================#
    "IdentifierException",
]

from chess.system import ServiceRequestDebugException


# ======================# IDENTIFIER_NOT_FOUND EXCEPTION #======================#
class IdentifierException(ServiceRequestDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a ServiceRequest candidate failed because the request had an incorrect identifier.

    # PARENT:
        *  ServiceRequestDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "IDENTIFIER_NOT_FOUND_ERROR"
    MSG = "ServiceRequest validation failed: request had an incorrect identifier."