# src/chess/board/database/core/exception/deletion/unfound.py

"""
Module: chess.board.database.core.exception.deletion.unfound
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
    "BoardDoesNotExistForRemovalException",
]

from chess.board import BoardException


# ======================# BOARD_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
class BoardDoesNotExistForRemovalException(BoardException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a board by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   BoardException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_DOES_NOT_EXIST_FOR_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "Board deletion failed: The board was not found in the dataset. Nothing to remove."