# src/logic/token/service/exception/unfound.py

"""
Module: logic.token.service.exception.unfound
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.system import NullException
from logic.token import TokenDebugException

__all__ = [
    # ======================# TOKEN_OPENING_SQUARE_NULL EXCEPTION #======================#
    "TokenOpeningSquareNotFoundException",
]


# ======================# TOKEN_OPENING_SQUARE_NULL EXCEPTION #======================#
class TokenOpeningSquareNotFoundException(TokenDebugException, NullException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an operation failed because the Token.opening_square_name is null.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_OPENING_SQUARE_NULL_EXCEPTION"
    MSG = "Token.opening_square_name cannot be null."
