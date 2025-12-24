# src/chess/game/exception.py

"""
Module: chess.game.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system.err import ChessException

__all__ = [
    "GameException",
]


class GameException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by Game objects.
    2.  Catchall for conditions which are not covered by lower level Game exception.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_ERROR"
    DEFAULT_MESSAGE = "Game raised an exception."

