# src/logic/token/validator/exception/flag/excess.py

"""
Module: logic.token.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.system import ContextFlagCountException
from logic.token import TokenContextException

__all__ = [
    # ========================= ARENA_TOKEN_CONTEXT_FLAG EXCEPTION =========================#
    "ArenaTokenContextFlagsException"
]


# ========================= ARENA_TOKEN_CONTEXT_FLAG EXCEPTION =========================#
class ArenaTokenContextFlagsException(TokenContextException, ContextFlagCountException):
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
    ERR_CODE = "ARENA_TOKEN_CONTEXT_FLAG_EXCEPTION"
    MSG = (
        "TokenContext validation failed: More than one attribute was set. Only one attribute-value should be enabled."
    )