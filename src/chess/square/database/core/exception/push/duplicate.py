# src/chess/square/service/collision/exception/debug/duplicate.py

"""
Module: chess.square.service.collision.exception.debug.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.square import SquareStackServiceException

__all__ = [
    # ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
    "AddingDuplicateSquareException",
]


# ======================# ADDING_DUPLICATE_SQUARE EXCEPTION #======================#
class AddingDuplicateSquareException(SquareStackServiceException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

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
    ERROR_CODE = "ADDING_DUPLICATE_SQUARE_ERROR"
    DEFAULT_MESSAGE = "SquareStack push failed: Cannot add a duplicate square to the stack."