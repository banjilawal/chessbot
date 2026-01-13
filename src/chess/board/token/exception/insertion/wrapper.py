# src/chess/team/board.token/exception/insertion/wrapper.py

"""
Module: chess.team.board.token.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.board import BoardTokenServiceException

__all__ = [
    # ======================# ADDING_TOKEN_TO_BOARD_TOKEN_FAILURE #======================#
    "AddingBoardTokenFailedException",
]


# ======================# ADDING_TOKEN_TO_BOARD_TOKEN_FAILURE #======================#
class AddingBoardTokenFailedException(BoardTokenServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that add a token to the boardToken failed.

    # PARENT:
        *   UniqueTeamDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_TOKEN_TO_BOARD_TOKEN_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Adding boardToken member failed."