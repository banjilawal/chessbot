# src/chess/board/exception/exploration/catchall.py

"""
Module: chess.board.exception.exploration.catchall
Author: Banji Lawal
Created: 2026-01-23
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_EXPLORATION_ERROR EXCEPTION #======================#
    "BoardExplorationException",
]

from chess.board import BoardException



# ======================# BOARD_EXPLORATION_ERROR EXCEPTION #======================#

class BoardExplorationException(BoardException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Catchall for any debug errors that occur during span computation.

    # PARENT:
        *   RankException
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_EXPLORATION_ERROR_ERROR"
    DEFAULT_MESSAGE = "Board exploration failed"