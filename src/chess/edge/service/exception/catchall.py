# src/chess/edge/service/exception/catchall.py

"""
Module: chess.edge.service.exception.catchall
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.edge import EdgeException
from chess.system import ServiceException

__all__ = [
    # ======================# EDGE_SERVICE EXCEPTION #======================#
    "EdgeServiceException",
]


# ======================# EDGE_SERVICE EXCEPTION #======================#
class EdgeServiceException(EdgeException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an EdgeService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a EdgeService method.

    # PARENT:
        *   ServiceException
        *   EdgeException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "EdgeService raised an exception."