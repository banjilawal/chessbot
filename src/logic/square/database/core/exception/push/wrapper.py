# src/logic/square/service/collision/exception/debug/wrapper.py

"""
Module: logic.square.service.collision.exception.debug.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_STACK_PUSH_FAILURE #======================#
    "SquareStackPushException",
]

from logic.system import InsertionException


# ======================# SQUARE_STACK_PUSH_FAILURE #======================#
class SquareStackPushException(InsertionException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

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
    ERR_CODE = "SQUARE_STACK_PUSH_FAILURE"
    MSG = "SquareStack push failed."