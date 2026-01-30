___all__ = [
    # ======================# BOARD_STACK_SERVICE EXCEPTION #======================#
    "BoardDataServiceException",
]

from chess.board import BoardException
from chess.system import ServiceException


# ======================# BOARD_STACK_SERVICE EXCEPTION #======================#
class BoardDataServiceException(BoardException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an BoardStackService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a BoardStackService method.

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
    ERROR_CODE = "BOARD_DATABASE_CORE_ERROR"
    DEFAULT_MESSAGE = "BoardStackService raised an exception."