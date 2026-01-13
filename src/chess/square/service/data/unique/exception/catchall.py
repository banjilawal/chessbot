from chess.system import UniqueDataServiceException

___all__ = [
    # ======================# PLAYER_DATA_SERVICE EXCEPTION #======================#
    "UniqueSquareDataServiceException",
]

from chess.square import SquareException
from chess.system import ServiceException


# ======================# UNIQUE_SQUARE_DATA_SERVICE EXCEPTION #======================#
class UniqueSquareDataServiceException(SquareException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an UniqueSquareDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a UniqueSquareDataService method.

    # PARENT:
        *   ServiceException
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueSquareDataService raised an exception."