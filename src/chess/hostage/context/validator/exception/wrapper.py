# src/chess/hostage/context/validator/exception/wrapper.py

"""
Module: chess.hostage.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.captivity import CaptivityContextException

__all__ = [
    # ======================# CAPTIVITY_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "CaptivityContextValidationFailedException",
]


# ======================# CAPTIVITY_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class CaptivityContextValidationFailedException(CaptivityContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a CaptivityContext. The encapsulated
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   CaptivityContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CAPTIVITY_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "CaptivityContext validation failed."