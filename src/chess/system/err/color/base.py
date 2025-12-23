# src/chess/system/err/color.py

"""
Module: chess.system.err.color
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
#======================# GAME_COLOR EXCEPTION #======================#
    "GameColorException",
]


#======================# GAME_COLOR EXCEPTION #======================#
class GameColorException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for conditions which are not covered by GameColorException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_COLOR_ERROR"
    DEFAULT_MESSAGE = "GameColor raised an exception."