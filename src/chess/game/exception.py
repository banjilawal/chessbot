# src/chess/game/exception.py

"""
Module: chess.game.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# GAME EXCEPTION #======================#
    "GameException",
]


# ======================# GAME EXCEPTION #======================#
class GameException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when a Game's organic fields or methods run into a condition that
        leads to an operation failing.
    2.  Parent of exception raised by Game Builders and Validators or any other classes that highly
        cohere with Game objects.
    3.  Catchall for Game errors not covered by lower level  Game exception.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_ERROR"
    DEFAULT_MESSAGE = "Game raised an exception."
