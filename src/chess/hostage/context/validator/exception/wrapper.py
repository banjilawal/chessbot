# src/chess/hostage/context/validator/exception/wrapper.py

"""
Module: chess.hostage.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.hostage import CaptivityContextException
from chess.system import ValidationException


__all__ = [
    # ======================# CAPTIVITY_CONTEXT_VALIDATION_FAILURE #======================#
    "CaptivityContextValidationException",
]


# ======================# CAPTIVITY_CONTEXT_VALIDATION_FAILURE #======================#
class CaptivityContextValidationException(CaptivityContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a CaptivityContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   CaptivityContextException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CAPTIVITY_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "CaptivityContext validation failed."