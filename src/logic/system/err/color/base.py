# src/logic/system/err/color/base.py

"""
Module: logic.system.err.color.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import ChessException

__all__ = [
#======================# GAME_COLOR EXCEPTION #======================#
    "GameColorException",
]


#======================# GAME_COLOR EXCEPTION #======================#
class GameColorException(ChessException):
    """
    Role:Super Exception

    Responsibilities:
    1.  Super for conditions which are not covered by GameColorException subclasses.

    Super Class:
        *   ChessException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "GAME_COLOR_EXCEPTION"
    MSG = "GameColor raised an exception."