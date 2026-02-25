# src/chess/system/service/request/validator/wrapper.py

"""
Module: chess.system.service.request.validator.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from chess.system import ValidationException

__all__ = [
    # ======================# SERVICE_REQUEST_VALIDATION_FAILURE #======================#
    "ServiceRequestValidationException",
]

# ======================# SERVICE_REQUEST_VALIDATION_FAILURE #======================#
class ServiceRequestValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that An error occurred in ServiceRequestValidator.validator.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ServiceRequest.validate error:D"
    MSG = "An exception was raised in ServiceRequestValidator.validator."