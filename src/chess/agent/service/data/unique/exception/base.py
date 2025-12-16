# src/chess/player_agent/service/data/unique/exception/base.py

"""
Module: chess.player_agent.service.data.unique.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import UniqueDataServiceException

__all__ = [
    #======================# UNIQUE_AGENT_DATA_SERVICE EXCEPTIONS #======================#
    "UniqueAgentDataServiceException",
]


#======================# UNIQUE_AGENT_DATA_SERVICE EXCEPTIONS #======================#
class UniqueAgentDataServiceException(UniqueDataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by UniqueAgentDataService objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of an UniqueDataAgent's method.

    # PARENT:
        *   UniqueDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_AGENT_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueAgentDataService raised an exception."