__all__ = [
    # ======================# ARENA_SERVICE EXCEPTION #======================#
    "ArenaServiceException",
]

from chess.arena import ArenaException
from chess.system import ServiceException


# ======================# ARENA_SERVICE EXCEPTION #======================#
class ArenaServiceException(ArenaException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an ArenaService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a ArenaService method.

    # PARENT:
        *   ServiceException
        *   ArenaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "ArenaService raised an exception."