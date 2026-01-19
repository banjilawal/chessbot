# src/chess/hostage/context/validator/exception/debug/excess.py

"""
Module: chess.hostage.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.hostage import CaptivityContextException

__all__ = [
    # ========================= EXCESSIVE_CAPTIVITY_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveCaptivityContextFlagsException"
]


# ========================= EXCESSIVE_CAPTIVITY_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveCaptivityContextFlagsException(CaptivityContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a CaptivityContext because more than one of its attributes
        was enabled.

    # PARENT:
        *   ContextFlagCountException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_CAPTIVITY_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "CaptivityContext validation failed: More than one flag was enable."