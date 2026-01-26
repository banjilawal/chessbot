# src/chess/occupant/validator/exception/flag/excess.py

"""
Module: chess.occupant.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.token import TokenContextException

__all__ = [
    # ========================= EXCESSIVE_TOKEN_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveTokenContextFlagsException"
]


# ========================= EXCESSIVE_TOKEN_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveTokenContextFlagsException(TokenContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted TokenContext certification because more than one TokenContext
        flag was enabled.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidTokenContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_TOKEN_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "TokenContext validation failed: More than one attribute was set. Only one attribute-value should be enabled."
    )