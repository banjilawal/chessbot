# src/chess/token/service/detector/exception/debug/square.py

"""
Module: chess.token.service.detector.exception.debug.square
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_OPENING)SQUARE_COLLISION EXCEPTION #======================#
    "TokenOpeningSquareCollisionException",
]

from chess.token import TokenStackException


# ======================# TOKEN_OPENING)SQUARE_COLLISION EXCEPTION #======================#
class TokenOpeningSquareCollisionException(TokenStackException):
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
    ERROR_CODE = "TOKEN_OPENING)SQUARE_COLLISION_ERROR"
    DEFAULT_MESSAGE = "Pushing token failed: The opening square was already in use."