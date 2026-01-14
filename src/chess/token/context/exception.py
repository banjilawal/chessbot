# src/chess/token/context/exception.py

"""
Module: chess.token.context.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.token import TokenException
from chess.system import ContextException

__all__ = [
    # ======================# TOKEN_CONTEXT EXCEPTION #======================#
    "TokenContextException",
]


# ======================# TOKEN_CONTEXT EXCEPTION #======================#
class TokenContextException(TokenException, ContextException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for TokenContext errors not covered by TokenException subclasses.

    # PARENT:
        *   TokenException
        *   ContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TokenContext raised an exception."