# src/chess/token/database/core/exception/insertion/full/stack.py

"""
Module: chess.token.database.core.exception.insertion.full.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# FULL_TOKEN_STACK EXCEPTION #======================#
    "FullTokenStackException",
]

from chess.system import DebugException
from chess.token import TokenStackException


# ======================# FULL_TOKEN_STACK EXCEPTION #======================#
class FullTokenStackException(TokenStackException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing a token to the stack failed because the stack was full.

    # PARENT:
        *   DebugException
        *   TokenServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FULL_TOKEN_STACK_ERROR"
    DEFAULT_MESSAGE = "Pushing token failed: The stack was full."