# src/chess/board/context/service/exception.py

"""
Module: chess.board.context.service.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ServiceException
from chess.board import BoardContextException

__all__ = [
    # ======================# BOARD_CONTEXT_SERVICE EXCEPTION #======================#
    "BoardContextServiceException",
]


# ======================# BOARD_CONTEXT_SERVICE EXCEPTION #======================#
class BoardContextServiceException(BoardContextException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an BoardContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an BoardContextService method.

    # PARENT:
        *   ServiceException
        *   BoardContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "BoardContextService raised an exception."