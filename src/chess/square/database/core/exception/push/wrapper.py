# src/chess/square/service/collision/exception/debug/wrapper.py

"""
Module: chess.square.service.collision.exception.debug.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_STACK_PUSH_FAILURE #======================#
    "SquareStackPushException",
]

from chess.system import InsertionException


# ======================# SQUARE_STACK_PUSH_FAILURE #======================#
class SquareStackPushException(InsertionException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareStackService.push that prevented a successful InsertionResult.
    2.  This error might have occurred in a different SquareStackService method that also returns InsertionResults.

    # PARENT:
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_STACK_PUSH_FAILURE"
    DEFAULT_MESSAGE = "SquareStack push failed."