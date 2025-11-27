# src/chess/agent/service/data/exception.py

"""
Module: chess.agent.service.data.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import DataServiceException, NullException

__all__ = [
    "DataServiceException",
    "NullException",
]

# ======================# AGENT SERVICE EXCEPTIONS #======================#
class AgentDataServiceException(DataServiceException):
    ERROR_CODE = "AGENT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentService raised an exception."

class AgentNullDataSetException(AgentDataServiceException, NullException):
    ERROR_CODE = "AGENT_NULL_DATA_SET_ERROR"
    DEFAULT_MESSAGE = "AgentDataService cannot have a null list of items."