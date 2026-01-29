# src/chess/owner/service/data/unique/exception.py

"""
Module: chess.owner.service.data.unique.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import DatabaseException

__all__ = [
    #======================# UNIQUE_AGENT_DATA_SERVICE EXCEPTION #======================#
    "UniqueAgentDataServiceException",
]


#======================# UNIQUE_AGENT_DATA_SERVICE EXCEPTION #======================#
class UniqueAgentDataServiceException(AgentException, DatabaseException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by UniqueAgentDataService objects.
    2.  Wraps an exception that hits the try-finally block of an UniqueDataAgent's method.

    # PARENT:
        *   DatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_AGENT_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueAgentDataService raised an exception."