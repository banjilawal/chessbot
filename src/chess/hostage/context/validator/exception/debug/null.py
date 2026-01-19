# src/chess/hostage/context/validator/exception/debug/null.py

"""
Module: chess.hostage.context.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.hostage import CaptivityContextException
from chess.system import NullException

__all__ = [
    # ======================# NULL_CAPTIVITY_CONTEXT EXCEPTION #======================#
    "NullCaptivityContextException",
]


# ======================# NULL_CAPTIVITY_CONTEXT EXCEPTION #======================#
class NullCaptivityContextException(CaptivityContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a CaptivityContext because it was null.

    # PARENT:
        *   CaptivityContextException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_CAPTIVITY_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CaptivityContext validation failed: The candidate was null."