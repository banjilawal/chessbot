# src/logic/player/service/exception.py

"""
Module: logic.player.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from logic.system import ServiceException
from logic.agent import AgentContextException

__all__ = [
    #======================# PLAYER_CONTEXT_SERVICE EXCEPTION #======================#
    "AgentContextServiceException",
]


#======================# PLAYER_CONTEXT_SERVICE EXCEPTION #======================#
class AgentContextServiceException(AgentContextException, ServiceException):
    """
    # ROLE: Exception Wrapper
    
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
    ERR_CODE = "AGENT_CONTEXT_SERVICE_EXCEPTION"
    MSG = "AgentContextService raised an exception."