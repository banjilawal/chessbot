# src/logic/board/build/exception/debug/board.py

"""
Module: logic.board.build.exception.debug.board
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
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that a board build failed because the board for the board was already occupied.

    Super Class:
        *   BoardException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_ALREADY_CONTAINS_BOARD_EXCEPTION"
    MSG = "Board build failed: The board already contains a board."