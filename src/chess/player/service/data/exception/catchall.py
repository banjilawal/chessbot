# src/chess/owner/service/data/_exception.py

"""
Module: chess.owner.service.data._exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import DataServiceException

___all__ = [
    # ======================# PLAYER_STACK_SERVICE EXCEPTION #======================#
    "AgentDataServiceException",
]

from chess.agent import AgentException
from chess.system import ServiceException


# ======================# PLAYER_STACK_SERVICE EXCEPTION #======================#
class AgentDataServiceException(AgentException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an AgentStackService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a AgentStackService method.

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
    ERROR_CODE = "AGENT_DATABASE_CORE_ERROR"
    DEFAULT_MESSAGE = "AgentStackService raised an exception."