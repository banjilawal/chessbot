___all__ = [
    # ======================# BOARD_DATA_SERVICE EXCEPTION #======================#
    "BoardDataServiceException",
]

from chess.board import BoardException
from chess.system import ServiceException


# ======================# BOARD_DATA_SERVICE EXCEPTION #======================#
class BoardDataServiceException(BoardException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an BoardDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a BoardDataService method.

    # PARENT:
        *   ServiceException
        *   BoardDataException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "BoardDataService raised an exception."