# src/logic/player/database/core/_exception.py

"""
Module: logic.player.database.core._exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.agent import AgentException
from logic.system import DataServiceException

___all__ = [
    # ======================# PLAYER_STACK_SERVICE EXCEPTION #======================#
    "AgentDataServiceException",
]

from logic.agent import AgentException
from logic.system import ServiceException


# ======================# PLAYER_STACK_SERVICE EXCEPTION #======================#
class AgentDataServiceException(AgentException, ServiceException):
    """
    # ROLE: Exception Wrapper

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
    ERR_CODE = "AGENT_STACK_EXCEPTION"
    MSG = "AgentStackService raised an exception."