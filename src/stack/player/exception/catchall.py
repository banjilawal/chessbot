# src/logic/player/database/kernel/_exception.py

"""
Module: logic.player.database.kernel._exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.agent import AgentException
from system import DataServiceException

___all__ = [
    # ======================# PLAYER_STACK_SERVICE EXCEPTION #======================#
    "AgentDataServiceException",
]

from logic.agent import AgentException
from system import ServiceException


# ======================# PLAYER_STACK_SERVICE EXCEPTION #======================#
class AgentDataServiceException(AgentException, ServiceException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that an AgentStackService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a AgentStackService method.

    Super Class:
        *   ServiceException
        *   AgentDataException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "AGENT_STACK_EXCEPTION"
    MSG = "AgentStackService raised an exception."