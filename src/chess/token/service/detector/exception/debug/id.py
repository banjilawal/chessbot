# src/chess/token/service/detector/exception/debug/id.py

"""
Module: chess.token.service.detector.exception.debug.id
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_ID_ALREADY_USED EXCEPTION #======================#
    "TokenIdAlreadyInUseException",
]

from chess.token import TokenStackException


# ======================# TOKEN_ID_ALREADY_USED EXCEPTION #======================#
class TokenIdAlreadyInUseException(TokenStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing a token onto the stack failed because its id was already in use.

    # PARENT:
        *   TokenStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_ID_ALREADY_USED_ERROR"
    DEFAULT_MESSAGE = "Pushing token failed: The id was already in use."