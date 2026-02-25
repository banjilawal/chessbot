# src/chess/base/validator/exception/wrapper.py

"""
Module: chess.base.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# BASE_VALIDATION_FAILURE #======================#
    "BaseValidationException",
]


# ======================# BASE_VALIDATION_FAILURE #======================#
class BaseValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in BaseValidator.validate that, prevented A successful validation result 
        from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BASE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Base validation failed."