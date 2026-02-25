# src/chess/square/service/build/request/validator/wrapper.py

"""
Module: chess.square.service.build.request.validator.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SQUARE_BUILD_REQUEST_FAILURE #======================#
    "ServiceRequestValidationException",
]

from chess.system import ServiceRequestValidationException


# ======================# SQUARE_BUILD_REQUEST_FAILURE #======================#
class SquareBuildRequestException(ServiceRequestValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareBuildRequestValidator.validate that, prevented a success
        result from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_BUILD_REQUEST_FAILED"
    MSG = "SquareBuildRequest validation failed."