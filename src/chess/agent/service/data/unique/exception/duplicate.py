# src/chess/agent/service/data/unique/exception.py

"""
Module: chess.agent.service.data.unique.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    # ======================# UNIQUE_AGENT_DATA_SERVICE EXCEPTIONS #======================#
    "UniqueAgentDataServiceException",
    "AddingDuplicateAgentException",
]


# ======================# UNIQUE_AGENT_DATA_SERVICE EXCEPTIONS #======================#
class UniqueAgentDataServiceException(DataServiceException):
    """
    Super class of exceptions raised by UniqueAgentDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "UNIQUE_AGENT_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueAgentDataService raised an exception."


class AddingDuplicateAgentException(UniqueAgentDataServiceException):
    """Raised when trying to add a duplicate Agent to a list of Agents."""
    ERROR_CODE = "DUPLICATE_AGENT_ADDITION_ERROR"
    DEFAULT_MESSAGE = "UniqueAgentDataService cannot add duplicate Agents to the list."