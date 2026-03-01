# src/logic/board/database/exception/deletion/wrapper.py

"""
Module: logic.board.database.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# EXHAUSTIVE_BOARD_DELETION_FAILURE #======================#
    "ExhaustiveBoardDeletionException",
]

from logic.board import BoardException
from logic.system import DeletionException


# ======================# EXHAUSTIVE_BOARD_DELETION_FAILURE #======================#
class ExhaustiveBoardDeletionException(BoardException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why deleting all occurrences of a board failed. deletion fails. The
        encapsulated exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   BoardException
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EXHAUSTIVE_BOARD_DELETION_FAILURE"
    MSG = "Exhaustive board deletion failed."