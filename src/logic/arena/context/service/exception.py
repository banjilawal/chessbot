# src/logic/arena/service/exception/exception

"""
Module: logic.arena.service.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from logic.system import ServiceException
from logic.arena import ArenaContextException

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
    ERR_CODE = "ARENA_CONTEXT_SERVICE_EXCEPTION"
    MSG = "ArenaContextService raised an exception."