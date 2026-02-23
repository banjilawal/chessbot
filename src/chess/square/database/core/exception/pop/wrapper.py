# src/chess/square/database/core/exception/deletion/wrapper.py

"""
Module: chess.square.database.core.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_STACK_POP_FAILURE #======================#
    "PoppingSquareException",
]

from chess.system import DeletionException


# ======================# SQUARE_STACK_POP_FAILURE #======================#
class PoppingSquareException(DeletionException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareStackService.pop that prevented a successful InsertionResult.
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
    ERROR_CODE = "SQUARE_STACK_POP_FAILURE"
    DEFAULT_MESSAGE = "SquareStack pop failed."