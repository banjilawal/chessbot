# src/logic/board/database/kernel/exception/deletion/unfound.py

"""
Module: logic.board.database.kernel.exception.deletion.unfound
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
    "BoardDoesNotExistForRemovalException",
]

from logic.board import BoardException


# ======================# BOARD_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
class BoardDoesNotExistForRemovalException(BoardException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove instances of a board by a unique attribute failed because no bag
        matching the property were found in the collider_candidates.

    Super Class:
        *   BoardException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_DOES_NOT_EXIST_FOR_REMOVAL_EXCEPTION"
    MSG = "Board deletion failed: The board was not found in the collider_candidates. Nothing to remove."