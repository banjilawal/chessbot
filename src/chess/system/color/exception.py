# src/chess/system/color/collision.py

"""
Module: chess.system.color.exception
Author: Banji Lawal
Created: 2025-07-24
"""


from chess.system import ChessException, NullException, ValidationException

__all__ = [
    "GameColorException",
    
#======================# GAME_COLOR VALIDATION EXCEPTION #======================#
    "NullGameColorException",
    "InvalidGameColorException",
]


class GameColorException(ChessException):
    """
    Super class of exception raised by GameColor objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERR_CODE = "GAME_COLOR_ERROR"
    MSG = "GameColor raised an exception."


#======================# GAME_COLOR VALIDATION EXCEPTION #======================#
class NullGameColorException(GameColorException, NullException):
    """Raised if an entity, method, or operation requires GameColor but gets null instead."""
    ERR_CODE = "NULL_GAME_COLOR_ERROR"
    MSG = "GameColor cannot be null."


class InvalidGameColorException(GameColorException, ValidationException):
    """Super Exception for GameColorValidator when a candidate fails a sanity check.""""""
    ERR_CODE = "GAME_COLOR_VALIDATION_ERROR"
    MSG = "GameColor validation failed."