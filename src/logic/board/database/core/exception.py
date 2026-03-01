___all__ = [
    # ======================# BOARD_STACK_SERVICE EXCEPTION #======================#
    "BoardDataServiceException",
]

from logic.board import BoardException
from logic.system import ServiceException


# ======================# BOARD_STACK_SERVICE EXCEPTION #======================#
class BoardDataServiceException(BoardException, ServiceException):
    """
    # ROLE: Exception Wrapper

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
    ERR_CODE = "BOARD_STACK_EXCEPTION"
    MSG = "BoardStackService raised an exception."