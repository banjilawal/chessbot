# src/chess/board/exception/base.py

"""
Module: chess.board.exception.base.py
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    "BoardException",
]


class BoardException(ChessException):
    """
    Super class of exceptions raised by Board objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "BOARD_ERROR"
    DEFAULT_MESSAGE = "Board raised an exception."


