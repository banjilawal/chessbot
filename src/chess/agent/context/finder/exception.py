# src/chess/agent/context/finder/__init__.py

"""
Module: chess.agent.cntext.finder.__init__
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import FinderException

__all__ = [
    #======================# AGENT_FINDER EXCEPTIONS #======================#
    "AgentFinderException",
]


#======================# AGENT_FINDER EXCEPTIONS #======================#
class AgentFinderException(AgentException, FinderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when AgentFinder objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of an AgentFinder method.
  
    # PARENT:
        *   AgentException
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
