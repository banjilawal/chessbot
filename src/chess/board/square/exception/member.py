# src/chess/team/board.square/exception/member.py

"""
Module: chess.team.board.square.exception.member
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_SQUARE_MEMBER EXCEPTION #======================#
    "BoardSquareMemberException",
]

from chess.board import BoardException
from chess.square import SquareException
from chess.system import DebugException


# ======================# BOARD_SQUARE_MEMBER EXCEPTION #======================#
class BoardSquareMemberException(BoardException, SquareException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a BoardSquare member experienced an exception.

    # PARENT:
        *   BoardException
        *   SquareException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SQUARE_MEMBER_ERROR"
    DEFAULT_MESSAGE = "BoardSquareMember raised an exception."