# src/chess/agent/service/data/base.py

"""
Module: chess.agent.service.data.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import DataServiceException, NullException

__all__ = [
    "AgentDataServiceException",
    "AgentNullDataSetException",
]

# ======================# AGENT SERVICE EXCEPTIONS #======================#
class AgentDataServiceException(DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an AgentDataService's organic fields or methods run into a
        condition that leads to an operation failing.
    2.  Parent of exceptions raised by classes that highly cohere with AgentDataService objects.
    3.  Catchall for AgentDataService failure that are not covered by a lower level Agent exception.

    # PARENT
        *   DataServiceException

    # PROVIDES:
    AgentDataServiceException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentService raised an exception."

class AgentNullDataSetException(AgentDataServiceException, NullException):
    ERROR_CODE = "AGENT_NULL_DATA_SET_ERROR"
    DEFAULT_MESSAGE = "AgentDataService cannot have a null list of items."