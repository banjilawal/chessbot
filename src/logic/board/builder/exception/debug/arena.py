# src/logic/board/builder/exception/debug/board.py

"""
Module: logic.board.builder.exception.debug.board
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_ALREADY_CONTAINS_BOARD EXCEPTION #======================#
    "BoardAlreadyContainsBoardException",
]

from logic.board import BoardException


# ======================# BOARD_ALREADY_CONTAINS_BOARD EXCEPTION #======================#
class BoardAlreadyContainsBoardException(BoardException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a board build failed because the board for the board was already occupied.

    # PARENT:
        *   BoardException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_ALREADY_CONTAINS_BOARD_EXCEPTION"
    MSG = "Board build failed: The board already contains a board."