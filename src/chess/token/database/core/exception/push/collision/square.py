# src/chess/token/database/core/exception/insertion/collision/square.py

"""
Module: chess.token.database.core.exception.insertion.collision.square
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_OPENING_SQUARE_ALREADY_USED EXCEPTION #======================#
    "TokenOpeningSquareAlreadyInUseException",
]

from chess.token import TokenStackException


# ======================# TOKEN_OPENING_SQUARE_ALREADY_USED EXCEPTION #======================#
class TokenOpeningSquareAlreadyInUseException(TokenStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing a token onto the stack failed because its opening square was already in use.

    # PARENT:
        *   TokenStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_OPENING_SQUARE_ALREADY_USED_ERROR"
    DEFAULT_MESSAGE = "Pushing token failed: The opening square was already in use."