# src/chess/player/exception.py

"""
Module: chess.player.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import ContextException


__all__ = [
    #======================# PLAYER_CONTEXT EXCEPTION #======================#
    "AgentContextException",
]


#======================# PLAYER_CONTEXT EXCEPTION #======================#
class AgentContextException(AgentException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by AgentContext objects.
    2.  Catchall for conditions which are not covered by lower level AgentContext exception.
    
    # PARENT:
        *   AgentException
        *   ContextException
        
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "AgentContext raised an exception."