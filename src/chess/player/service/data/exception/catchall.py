# src/chess/player/service/data/_exception.py

"""
Module: chess.player.service.data._exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import DataServiceException

___all__ = [
    # ======================# PLAYER_DATA_SERVICE EXCEPTION #======================#
    "AgentDataServiceException",
]

from chess.agent import AgentException
from chess.system import ServiceException


# ======================# PLAYER_DATA_SERVICE EXCEPTION #======================#
class AgentDataServiceException(AgentException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an AgentDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a AgentDataService method.

    # PARENT:
        *   ServiceException
        *   AgentDataException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentDataService raised an exception."