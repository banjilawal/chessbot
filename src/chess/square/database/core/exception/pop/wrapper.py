# src/chess/square/database/core/exception/deletion/wrapper.py

"""
Module: chess.square.database.core.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_STACK_POP_FAILURE #======================#
    "SquareStackPopException",
]

from chess.system import DeletionException


# ======================# SQUARE_STACK_POP_FAILURE #======================#
class SquareStackPopException(DeletionException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareStackService.pop that prevented a successful DeletionResult.
    2.  This error might have occurred in a different SquareStackService method that also returns DeletionResults.

    # PARENT:
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_STACK_POP_FAILURE"
    MSG = "SquareStack pop failed."