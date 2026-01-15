# src/chess/team/board/token/exception/insertion/wrapper.py

"""
Module: chess.team.board.token.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ADDING_TOKEN_TO_BOARD_FAILURE #======================#
    "AddingBoardTokenFailedException",
]

from chess.board import BoardException
from chess.token import TokenException
from chess.system import InsertionFailedException


# ======================# ADDING_TOKEN_TO_BOARD_FAILURE #======================#
class AddingBoardTokenFailedException(BoardException, TokenException, InsertionFailedException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that add a token to the boardToken failed.

    # PARENT:
        *   BoardException
        *   TokenException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_TOKEN_TO_BOARD_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Adding boardToken member failed."