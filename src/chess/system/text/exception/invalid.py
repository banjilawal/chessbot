# src/chess/system/text/exception/invalid.py

"""
Module: chess.system.text.exception.invalid
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import StringException, ValidationFailedException

__all__ = [
    # ======================# STRING_VALIDATION_FAILED EXCEPTION #======================#
    "InvalidStringException",

]


# ======================# STRING_VALIDATION_FAILED EXCEPTION #======================#
class InvalidStringException(StringException, ValidationFailedException):
    """Raised if StringValidator candidate fails a check."""
    ERROR_CODE = "STRING_VALIDATION_FAILED_ERROR"
    DEFAULT_MESSAGE = "String validation failed."
