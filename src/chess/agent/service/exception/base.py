# src/chess/agent/service/exception/exception.py

"""
Module: chess.agent.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    #======================# AGENT_SERVICE EXCEPTIONS #======================#
    "AgentServiceException",
]


#======================# AGENT_SERVICE EXCEPTIONS #======================#
class AgentServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an PlayerAgentService's organic fields or methods run into a
        condition that leads to an operation failing.
    2.  Parent of exceptions raised by classes that highly cohere with PlayerAgentService objects.
    3.  Catchall for PlayerAgentService failure states that are not covered by a lower level
        PlayerAgentService exception.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "PlayerAgentService raised an exception."