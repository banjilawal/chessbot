# src/chess/piece/validator/null/exception.py

"""
Module: chess.piece.validator.null.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_TOKEN_CONTEXT EXCEPTION #======================#
    "NullTokenContextException",
]

from chess.system import NullException
from chess.token import InvalidTokenContextException


# ======================# NULL_TOKEN_CONTEXT EXCEPTION #======================#
class NullTokenContextException(InvalidTokenContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that TokenContext validation failed because the candidate was null.

    # PARENT:
        *   NullTokenContextException
        *   InvalidTokenContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TOKEN_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TokenContext validation failed: The candidate was null."