# src/chess/player_agent/context/exception.py

"""
Module: chess.player_agent.context.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextException


__all__ = [
    #======================# AGENT_CONTEXT EXCEPTION SUPER CLASS #======================#
    "AgentContextException",
]


#======================# AGENT_CONTEXT EXCEPTION SUPER CLASS #======================#
class AgentContextException(ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by AgentContext objects.
    2.  Catchall for conditions which are not covered by lower level AgentContext exceptions.
    
    # PARENT:
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