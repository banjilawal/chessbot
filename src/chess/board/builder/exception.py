# src/chess/board/builder/exception.py

"""
Module: chess.board.builder.exception
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""


from chess.board import BoardException
from chess.system import BuildFailedException

__all__ = [
    #======================# BOARD BUILD EXCEPTION #======================#
    "BoardBuildFailedException",
]


#======================# BOARD BUILD EXCEPTION #======================#
class BoardBuildFailedException(BoardException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by BoardBuilder
    prevents successful Board creation.
    """
    ERROR_CODE = "BOARD_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Board build failed."