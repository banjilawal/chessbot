# src/chess/agent/service/exception.py

"""
Module: chess.agent.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import ServiceException

__all__ = [
    #======================# AGENT_SERVICE EXCEPTION #======================#
    "AgentServiceException",
]


#======================# AGENT_SERVICE EXCEPTION #======================#
class AgentServiceException(AgentException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when an AgentService's organic fields or methods run into a
        condition that leads to an operation failing.
    2.  Parent of exception raised by classes that highly cohere with AgentService objects.
    3.  Catchall for AgentService failure states that are not covered by a lower level
        AgentService exception.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "AgentService raised an exception."