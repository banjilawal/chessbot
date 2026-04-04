# src/build/board/exception/arena.py

"""
Module: build.board.exception.arena
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

__all__ = [
    # ======================# BOARD_ALREADY_CONTAINS_BOARD EXCEPTION #======================#
    "ArenaAlreadyContainsBoardException",
]

from logic.board import BoardException


# ======================# BOARD_ALREADY_CONTAINS_BOARD EXCEPTION #======================#
class ArenaAlreadyContainsBoardException(BoardException):
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