# src/chess/board/builder/exception/debug/arena.py

"""
Module: chess.board.builder.exception.debug.arena
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# ARENA_ALREADY_CONTAINS_BOARD EXCEPTION #======================#
    "ArenaAlreadyContainsBoardException",
]

from chess.board import BoardException


# ======================# ARENA_ALREADY_CONTAINS_BOARD EXCEPTION #======================#
class ArenaAlreadyContainsBoardException(BoardException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a board build failed because the arena for the board was already occupied.

    # PARENT:
        *   BoardException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_ALREADY_CONTAINS_BOARD_ERROR"
    DEFAULT_MESSAGE = "Board build failed: The arena already contains a board."