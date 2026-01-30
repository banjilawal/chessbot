# src/chess/token/validator/exception/flag/zero.py

"""
Module: chess.token.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.token import TokenContextException

__all__ = [
    # ========================= ZERO_TOKEN_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroTokenContextFlagsException"
]


# ========================= ZERO_TOKEN_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroTokenContextFlagsException(TokenContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted TokenContext certification because no TokenContext flag
        was enabled.

    # PARENT:
        *   ContextFlagCountException
        *   TokenContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_TOKEN_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "TokenContext validation failed: No attributes were set. One attribute-value should be enabled."
    )