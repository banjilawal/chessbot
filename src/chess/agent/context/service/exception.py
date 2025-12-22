# src/chess/agent/service/exception.py

"""
Module: chess.agent.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.system import ServiceException
from chess.agent import AgentContextException

__all__ = [
    #======================# AGENT_CONTEXT_SERVICE EXCEPTION #======================#
    "AgentContextServiceException",
]


#======================# AGENT_CONTEXT_SERVICE EXCEPTION #======================#
class AgentContextServiceException(AgentContextException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  Indicate that an AgentContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an AgentContextService method.
        
    # PARENT:
        *   ServiceException
        *   AgentContextExceptio

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentContextService raised an exception."