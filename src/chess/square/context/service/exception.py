# src/chess/square/context/service/exception.py

"""
Module: chess.square.context.service.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ServiceException
from chess.square import SquareContextException

__all__ = [
    # ======================# SQUARE_CONTEXT_SERVICE EXCEPTION #======================#
    "SquareContextServiceException",
]


# ======================# SQUARE_CONTEXT_SERVICE EXCEPTION #======================#
class SquareContextServiceException(SquareContextException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SquareContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an SquareContextService method.

    # PARENT:
        *   ServiceException
        *   SquareContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareContextService raised an exception."