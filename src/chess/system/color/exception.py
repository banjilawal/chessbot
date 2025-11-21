# src/chess/system/color/collision.py

"""
Module: chess.system.color.exception
Author: Banji Lawal
Created: 2025-07-24
"""


from chess.system import ChessException, NullException, ValidationException

__all__ = [
    "GameColorException",
    
# ======================# GAME_COLOR VALIDATION EXCEPTIONS #======================#  
    "NullGameColorException",
    "InvalidGameColorException",
]


class GameColorException(ChessException):
    """
    Super class of exceptions raised by GameColor objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "GAMEC_OLOR_ERROR"
    DEFAULT_MESSAGE = "GameColor raised an exception."


# ======================# GAMECOLOR VALIDATION EXCEPTIONS #======================#  
class NullGameColorException(GameColorException, NullException):
    """Raised if an entity, method, or operation requires GameColor but gets null instead."""
    ERROR_CODE = "NULL_GAME_COLOR_ERROR"
    DEFAULT_MESSAGE = "GameColor cannot be null."


class InvalidGameColorException(GameColorException, ValidationException):
    """Catchall Exception for GameColorValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "GAME_COLOR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameColor validation failed."