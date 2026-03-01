# src/logic/token/service/detector/exception/debug/id.py

"""
Module: logic.token.service.detector.exception.debug.id
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_ID_COLLISION EXCEPTION #======================#
    "TokenIdCollisionException",
]

from logic.token import TokenStackException


# ======================# TOKEN_ID_COLLISION EXCEPTION #======================#
class TokenIdCollisionException(TokenStackException):
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
    ERR_CODE = "TOKEN_ID_COLLISION_EXCEPTION"
    MSG = "Pushing token failed: The id was already in use."