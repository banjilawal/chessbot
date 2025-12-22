# src/chess/agent/map/service/exception.py

"""
Module: chess.agent.map.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentContext
from chess.system import ServiceException

__all__ = [
    #======================# AGENT_CONTEXT_SERVICE EXCEPTION #======================#
    "AgentContextServiceException",
]


#======================# AGENT_CONTEXT_SERVICE EXCEPTION #======================#
class AgentContextServiceException(AgentContext, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  Indicate that an AgentContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an AgentContextService method.
        
    # PARENT:
        *   AgentException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentContextService raised an exception."