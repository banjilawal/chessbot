# src/chess/agent/service/data/exception/null.py

"""
Module: chess.agent.service.data.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentDataServiceException


__all__ = [
    "NullAgentDataServiceException",
    "AgentNullDataSetException",
]


#======================# NULL AGENT_DATA_SERVICE EXCEPTION #======================#
class NullAgentDataServiceException(InvalidAgentDataServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an AgentDataService but got null instead.

    # PARENT:
        *   InvalidAgentDataServiceException
        *   NullException

    # PROVIDES:
    NullAgentDataServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_AGENT_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentDataService cannot be null."


#======================# AGENT_NULL_DATASET EXCEPTION #======================#
class AgentNullDataSetException(InvalidAgentDataServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that AgentDataService.items does not exist.

    # PARENT:
        *   InvalidAgentDataServiceException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_NULL_DATASET_ERROR"
    DEFAULT_MESSAGE = "AgentDataService cannot have a null list of items."