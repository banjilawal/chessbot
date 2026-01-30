# src/chess/board/service/data/exception/deletion/empty.py

"""
Module: chess.board.service.data.exception.deletion.empty
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.board import BoardException

__all__ = [
    # ======================# POPPING_EMPTY_BOARD_STACK EXCEPTION #======================#
    "PoppingEmptyBoardStackException",
]


# ======================# POPPING_EMPTY_BOARD_STACK EXCEPTION #======================#
class PoppingEmptyBoardStackException(BoardException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a board failed because the stack was empty

    # PARENT:
        *   BoardException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_BOARD_STACK_ERROR"
    DEFAULT_MESSAGE = "Board deletion failed: BoardStackService does not own any boards."