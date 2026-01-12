# src/chess/owner/service/exception/catchall.py

"""
Module: chess.owner.service.exception.catchall
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.player import PlayerException
from chess.system import ServiceException

___all__ = [
    # ======================# PLAYER_SERVICE EXCEPTION #======================#
    "PlayerServiceException",
]


# ======================# PLAYER_SERVICE EXCEPTION #======================#
class PlayerServiceException(PlayerException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  Indicate that an PlayerService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an PlayerService method.
        
    # PARENT:
        *   PlayerException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PLAYER_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PlayerService raised an exception."