# src/chess/agent/service/data/exception/exception.py

"""
Module: chess.agent.service.data.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    #======================# AGENT_DATA_SERVICE EXCEPTIONS #======================#
    "AgentDataServiceException",
]


#======================# AGENT_DATA_SERVICE EXCEPTIONS #======================#
class AgentDataServiceException(DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by either AgentDataService objects.
    2.  Catchall for AgentDataService failure states that are not covered by a lower level
        AgentDataService exception.

    # PARENT:
        *   DataServiceException

    # PROVIDES:
    AgentDataServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_DATA_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "AgentDataService raised an exception."