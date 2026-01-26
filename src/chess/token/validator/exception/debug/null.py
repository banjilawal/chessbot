# src/chess/occupant/validator/exception/debug/__init__.py

"""
Module: chess.occupant.validator.exception.debug.__init__
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_TOKEN EXCEPTION #======================#
    "NullTokenException",
]

from chess.system import NullException
from chess.token import TokenException


# ======================# NULL_TOKEN EXCEPTION #======================#
class NullTokenException(TokenException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that Token validation failed because the candidate was null.

    # PARENT:
        *   TokenException
        *   NullTokenException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TOKEN_ERROR"
    DEFAULT_MESSAGE = "Token validation failed: The candidate was null."