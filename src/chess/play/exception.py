# src/chess/play/exception.py

"""
Module: chess.play.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system.err import ChessException

__all__ = [
    "PlayException",
]


class PlayException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Play objects.
    2.  Catchall for conditions which are not covered by lower level Play exceptions.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PLAY_ERROR"
    DEFAULT_MESSAGE = "Play raised an exception."

