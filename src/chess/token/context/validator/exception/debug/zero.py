# src/chess/token/validator/exception/flag/zero.py

"""
Module: chess.token.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.token import  TokenContextException

__all__ = [
    # ========================= ZERO_TOKEN_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroTokenContextFlagsException"
]


# ========================= ZERO_TOKEN_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroTokenContextFlagsException(TokenContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  no TokenContext flag was enabled. One and only one Token attribute-value-tuple is required for
        a search.

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
    ERROR_CODE = "ZERO_TOKEN_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "Zero TokenContext flags were set. Cannot search for Tokens if one-and_oly-one "
        "map flag is enabled."
    )
