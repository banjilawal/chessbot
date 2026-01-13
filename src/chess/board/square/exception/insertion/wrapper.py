# src/chess/team/board.square/exception/insertion/wrapper.py

"""
Module: chess.team.board.square.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.board import BoardSquareServiceException

__all__ = [
    # ======================# ADDING_TOKEN_TO_BOARD_SQUARE_FAILURE #======================#
    "AddingBoardSquareFailedException",
]


# ======================# ADDING_TOKEN_TO_BOARD_SQUARE_FAILURE #======================#
class AddingBoardSquareFailedException(BoardSquareServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that add a token to the boardSquare failed.

    # PARENT:
        *   UniqueTeamDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_TOKEN_TO_BOARD_SQUARE_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Adding boardSquare member failed."