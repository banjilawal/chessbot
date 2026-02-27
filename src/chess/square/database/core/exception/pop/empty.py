# src/chess/square/database/core/exception/deletion/empty.py

"""
Module: chess.square.database.core.exception.deletion.empty
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_EMPTY_SQUARE_STACK EXCEPTION #======================#
    "PoppingEmptySquareStackException",
]

from chess.square import SquareStackServiceException


# ======================# POPPING_EMPTY_SQUARE_STACK EXCEPTION #======================#
class PoppingEmptySquareStackException(SquareStackServiceException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    A failing DeletionResult was returned because an attempt was made to pop an empty square stack.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_SQUARE_STACK_EXCEPTION"
    MSG = "SquareStack pop failed: Cannot pop from an empty stack."