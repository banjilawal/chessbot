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
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Game errors not covered by GameException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_ERROR"
    DEFAULT_MESSAGE = "Game raised an exception."
