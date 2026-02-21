# src/chess/arena/service/exception/exception

"""
Module: chess.arena.service.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.system import ServiceException
from chess.arena import ArenaContextException

__all__ = [
    # ======================# ARENA_CONTEXT_SERVICE EXCEPTION #======================#
    "ArenaContextServiceException",
]


# ======================# ARENA_CONTEXT_SERVICE EXCEPTION #======================#
class ArenaContextServiceException(ArenaContextException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an ArenaContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an ArenaContextService method.

    # PARENT:
        *   ServiceException
        *   ArenaContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "ArenaContextService raised an exception."