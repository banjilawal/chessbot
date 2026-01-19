# src/chess/hostage/context/validator/exception/debug/zero.py

"""
Module: chess.hostage.context.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.hostage import CaptivityContextException

__all__ = [
    # ========================= ZERO_CAPTIVITY_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroCaptivityContextFlagsException"
]


# ========================= ZERO_CAPTIVITY_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroCaptivityContextFlagsException(CaptivityContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a CaptivityContext because none of its attributes was enabled.
        A single CaptivityContext attribute.

    # PARENT:
        *   ContextFlagCountException
        *   CaptivityContextValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_CAPTIVITY_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "CaptivityContext validation failed: None of the flags were set. A single flag must be enabled."