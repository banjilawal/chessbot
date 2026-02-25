# src/chess/system/service/request/validator/exception/debug/null.py

"""
Module: chess.system.service.request.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# WRONG_ARGUMENT_TYPE EXCEPTION #======================#
    "ArgumentTypeException",
]

from chess.system import ServiceRequestDebugException


# ======================# WRONG_ARGUMENT_TYPE EXCEPTION #======================#
class ArgumentTypeException(ServiceRequestDebugException):
    
    SOURCE_CLASS = "ServiceRequest"
    SOURCE_METHOD = "validate"
    
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging
    
    # ERROR SOURCE CLASS:
    ServiceRequestValidator
    
    # ERROR SOURCE METHOD:
    

    # RESPONSIBILITIES:
    1.  Indicate that a failing result was returned By Serive because service_request.arguments[identifier]
        failed a type checking validation test.

    # PARENT:
        *  ServiceRequestDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "WRONG_ARGUMENT_TYPE_ERROR"
    MSG = "service_request.arguments[identifier]: has wrong type"