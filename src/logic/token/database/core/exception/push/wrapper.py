# src/logic/token/database/core/exception/push/wrapper.py

"""
Module: logic.token.database.core.exception.push.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# PUSHING_TOKEN_FAILURE #======================#
    "PushingTokenException",
]

from logic.token import TokenStackException
from logic.system import PushException


# ======================# PUSHING_TOKEN_FAILURE #======================#
class PushingTokenException(TokenStackException, PushException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

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
    ERR_CODE = "PUSHING_TOKEN_FAILURE"
    MSG = "Pushing token failed."