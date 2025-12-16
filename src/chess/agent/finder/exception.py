# src/chess/player_agent/finder/exception

"""
Module: chess.player_agent.finder.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    #======================# AGENT_FINDER EXCEPTIONS #======================#
    "AgentFinderException",
]


#======================# AGENT_FINDER EXCEPTIONS #======================#
class AgentFinderException(FinderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when: data in an AgentFinder's fields or unanticipated conditions
        halt the normal flow of AgentFinder operations.
    2.  Wraps unhandled exceptions that hit the try-finally block of an AgentFactory method.
  
    # PARENT:
        *   FinderException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_FINDER_ERROR"
    DEFAULT_MESSAGE = "AgentFinder raised an exception."
