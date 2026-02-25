# src/chess/square/service/visitation/exception/start/board.py

"""
Module: chess.square.service.visitation.exception.start.board
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

___all__ = [
    # ======================# VISITOR_FROM_WRONG_BOARD EXCEPTION #======================#
    "VisitorFromWrongBoardException",
]

from chess.square import SquareDebugException

# ======================# VISITOR_FROM_WRONG_BOARD EXCEPTION #======================#
class VisitorFromWrongBoardException(SquareDebugException):

      
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing UpdateResult was returned because a token tried to visit a square on a different board.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VISITOR_FROM_WRONG_BOARD_ERROR"
    MSG = "Square visit start failed: The visitor belongs to a different board."