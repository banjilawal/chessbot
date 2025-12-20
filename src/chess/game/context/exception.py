# src/chess/game/context/exception.py

"""
Module: chess.game.context.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextException


__all__ = [
    #======================# GAME_CONTEXT EXCEPTION #======================#
    "GameContextException",
]


#======================# GAME_CONTEXT EXCEPTION #======================#
class GameContextException(ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when an GameContext's organic fields or methods run into a condition that
        leads to an operation failing.
    2.  Parent of exception raised by GameContext Builders and Validators or any other classes that highly
        cohere with GameContext objects.
    3.  Catchall for GameContext failure states that are not covered by a lower level GameContext exception.
    
    # PARENT:
        *   ContextException
        
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "GameContext raised an exception."