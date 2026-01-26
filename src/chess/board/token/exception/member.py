# src/chess/board/occupant/exception/member.py

"""
Module: chess.board.occupant.exception.member
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_TOKEN_MEMBER EXCEPTION #======================#
    "BoardTokenMemberException",
]

from chess.board import BoardException
from chess.token import TokenException
from chess.system import DebugException


# ======================# BOARD_TOKEN_MEMBER EXCEPTION #======================#
class BoardTokenMemberException(BoardException, TokenException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a BoardToken member experienced an exception.

    # PARENT:
        *   BoardException
        *   TokenException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_TOKEN_MEMBER_ERROR"
    DEFAULT_MESSAGE = "BoardTokenMember raised an exception."