# src/chess/token/database/core/exception/push/wrapper.py

"""
Module: chess.token.database.core.exception.push.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# PUSHING_TOKEN_FAILURE #======================#
    "PushingTokenException",
]

from chess.token import TokenStackException
from chess.system import PushException


# ======================# PUSHING_TOKEN_FAILURE #======================#
class PushingTokenException(TokenStackException, PushException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why pushing a token failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   TokenException
        *   PushException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PUSHING_TOKEN_FAILURE"
    DEFAULT_MESSAGE = "Pushing token failed."