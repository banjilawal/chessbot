# src/chess/system/number/exception/invalid.py

"""
Module: chess.system.number.exception.invalid
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NUMBER_VALIDATION_FAILURE EXCEPTION #======================#
    "NumberValidationFailedException",
]

from chess.system import NumberException, ValidationFailedException


# ======================# NUMBER_VALIDATION_FAILURE EXCEPTION #======================#
class NumberValidationFailedException(NumberException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as an Int. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   NumberException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NUMBER_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Number validation failed."