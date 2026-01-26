# src/chess/team/board/square/exception/insertion/wrapper.py

"""
Module: chess.team.board.square.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ADDING_SQUARE_TO_BOARD_FAILURE #======================#
    "AddingBoardSquareFailedException",
]

from chess.board import BoardException
from chess.square import SquareException
from chess.system import InsertionFailedException


# ======================# ADDING_SQUARE_TO_BOARD_FAILURE #======================#
class AddingBoardSquareFailedException(BoardException, SquareException, InsertionFailedException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that add a occupant to the boardSquare failed.

    # PARENT:
        *   BoardException
        *   SquareException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_SQUARE_TO_BOARD_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Adding boardSquare member failed."