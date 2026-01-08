# src/chess/player/service/exception/catchall.py

"""
Module: chess.player.service.exception.catchall
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import ServiceException

___all__ = [
    # ======================# PLAYER_SERVICE EXCEPTION #======================#
    "AgentServiceException",
]


# ======================# PLAYER_SERVICE EXCEPTION #======================#
class AgentServiceException(AgentException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  Indicate that an AgentService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an AgentService method.
        
    # PARENT:
        *   AgentException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentService raised an exception."