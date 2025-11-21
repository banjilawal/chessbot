# src/chess/board/builder/exception.py

"""
Module: chess.board.builder.exception
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""


from chess.board import BoardException
from chess.system import BuildFailedException

__all__ = ["BoardBuildFailedException"]

class BoardBuildFailedException(BoardException, BuildFailedException):
    """Catchall Exception for BoardBuilder when it encounters an error building a Board."""
    ERROR_CODE = "BOARD_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Board build failed."