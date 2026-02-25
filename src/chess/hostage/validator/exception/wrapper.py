# src/chess/Hostage/validator/exception/wrapper.py

"""
Module: chess.Hostage.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# Hostage_VALIDATION_FAILURE #======================#
    "HostageValidationException",
]


# ======================# Hostage_VALIDATION_FAILURE #======================#
class HostageValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in HostageValidator.validate that, prevented A successful validation result
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
    ERR_CODE = "Hostage_VALIDATION_FAILURE"
    MSG = "Hostage validation failed."
