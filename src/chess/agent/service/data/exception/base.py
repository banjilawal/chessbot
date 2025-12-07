# src/chess/agent/entity_service/data/exception/base.py

"""
Module: chess.agent.entity_service.data.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    # ======================# AGENT_DATA_SERVICE EXCEPTIONS #======================#
    "AgentDataServiceException",
]


# ======================# AGENT_DATA_SERVICE EXCEPTIONS #======================#
class AgentDataServiceException(DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an AgentDataService's organic fields or methods run into a
        conditioncthat leads to an operation failing.
    2.  Parent of exceptions raised by classes that highly cohere with AgentDataService objects.
    3.  Catchall for AgentDataService failure states that are not covered by a lower level
        AgentDataService exception.

    # PARENT
        *   DataServiceException

    # PROVIDES:
    AgentDataServiceException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_DATA_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "AgentDataService raised an exception."