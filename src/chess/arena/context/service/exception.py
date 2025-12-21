# src/chess/agent/map/service/exception/exception

"""
Module: chess.agent.map.service.exception.exception
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
    1.  Parent of exception raised when an AgentContextService's normal operations are halted
        by an error condition.
    2.  Raised when no specific exception exists for the error interrupting AgentContextService's
        processes from their normal flows.
        
    # PARENT:
        *   AgentContext
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