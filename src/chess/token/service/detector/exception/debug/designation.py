# src/chess/token/service/detector/exception/debug/designation.py

"""
Module: chess.token.service.detector.exception.debug.designation
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_DESIGNATION_COLLISION EXCEPTION #======================#
    "TokenDesignationCollisionException",
]

from chess.token import TokenStackException


# ======================# TOKEN_DESIGNATION_COLLISION EXCEPTION #======================#
class TokenDesignationCollisionException(TokenStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing a token onto the stack failed because its designation was already in use.

    # PARENT:
        *   TokenStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_DESIGNATION_COLLISION_ERROR"
    DEFAULT_MESSAGE = "Pushing token failed: The designation was already in use."