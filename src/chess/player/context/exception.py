# src/chess/player/exception.py

"""
Module: chess.player.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.player import PlayerException
from chess.system import ContextException


__all__ = [
    #======================# PLAYER_CONTEXT EXCEPTION #======================#
    "PlayerContextException",
]


#======================# PLAYER_CONTEXT EXCEPTION #======================#
class PlayerContextException(PlayerException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by PlayerContext objects.
    2.  Catchall for conditions which are not covered by lower level PlayerContext exception.
    
    # PARENT:
        *   PlayerException
        *   ContextException
        
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PLAYER_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "PlayerContext raised an exception."