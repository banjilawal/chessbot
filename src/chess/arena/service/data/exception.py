___all__ = [
    # ======================# ARENA_DATA_SERVICE EXCEPTION #======================#
    "ArenaDataServiceException",
]

from chess.arena import ArenaException
from chess.system import ServiceException


# ======================# ARENA_DATA_SERVICE EXCEPTION #======================#
class ArenaDataServiceException(ArenaException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an ArenaDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a ArenaDataService method.

    # PARENT:
        *   ServiceException
        *   ArenaDataException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "ArenaDataService raised an exception."