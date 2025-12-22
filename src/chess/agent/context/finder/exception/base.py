# src/chess/agent/map/finder/exception/base.py

"""
Module: chess.agent.cntext.finder.exception.base
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import FinderException

__all__ = [
    #======================# AGENT_FINDER EXCEPTION #======================#
    "AgentFinderException",
]


#======================# AGENT_FINDER EXCEPTION #======================#
class AgentFinderException(AgentException, FinderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exception raised when AgentFinder objects.
    2.  Wraps an exception that hits the try-finally block of an AgentFinder method.
  
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
