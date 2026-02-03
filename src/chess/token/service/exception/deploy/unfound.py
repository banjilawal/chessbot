# src/chess/token/service/exception/unopened.py

"""
Module: chess.token.service.exception.unopened
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.token import TokenException

__all__ = [
    # ======================# TOKEN_OPENING_SQUARE_NULL EXCEPTION #======================#
    "TokenOpeningSquareNotFoundException",
]


# ======================# TOKEN_OPENING_SQUARE_NULL EXCEPTION #======================#
class TokenOpeningSquareNotFoundException(TokenException, NullException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an operation failed because the Token.opening_square is null.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_OPENING_SQUARE_NULL_ERROR"
    DEFAULT_MESSAGE = "Token.opening_square cannot be null."
