# src/chess/system/err/color.py

"""
Module: chess.system.err.color
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException

__all__ = [
#======================# GAME_COLOR EXCEPTION #======================#
    "GameColorException",
    "InvalidGameColorException",
    "NullGameColorException",
]


#======================# GAME_COLOR EXCEPTION #======================#
class GameColorException(ChessException):
    """"""
    ERROR_CODE = "GAME_COLOR_ERROR"
    DEFAULT_MESSAGE = "GameColor raised an exception failed."


#======================# GAME_COLOR VALIDATION EXCEPTION #======================#
class InvalidGameColorException(GameColorException, ValidationException):
    """"""
    ERROR_CODE = "GAME_COLOR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameColor validation failed"


class NullGameColorException(InvalidGameColorException, NullException):
    """"""
    ERROR_CODE = "NULL_GAME_COLOR_ERROR"
    DEFAULT_MESSAGE = "GameColor cannot be null."