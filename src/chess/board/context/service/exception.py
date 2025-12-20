# src/chess/board/context/service/exception/exception

"""
Module: chess.board.context.service.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.board import BoardContext
from chess.system import ServiceException

__all__ = [
    # ======================# BOARD_CONTEXT_SERVICE EXCEPTION #======================#
    "BoardContextServiceException",
]


# ======================# BOARD_CONTEXT_SERVICE EXCEPTION #======================#
class BoardContextServiceException(BoardContext, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when an BoardContextService's normal operations are halted
        by an error condition.
    2.  Raised when no specific exception exists for the error interrupting BoardContextService's
        processes from their normal flows.

    # PARENT:
        *   BoardContext
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "BoardContextService raised an exception."