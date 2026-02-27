# src/chess/square/service/collision/exception/debug/duplicate.py

"""
Module: chess.square.service.collision.exception.debug.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.square import SquareDebugException

__all__ = [
    # ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
    "AddingDuplicateSquareException",
]


# ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
class AddingDuplicateSquareException(SquareDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    A failing InsertionResult was returned because an attempt to add a duplicate square to the stack.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_SQUARE_EXCEPTION"
    MSG = "SquareStack push failed: Cannot add a duplicate square to the stack."