# src/chess/edge/context/service/exception.py

"""
Module: chess.edge.context.service.exception
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import ServiceException
from chess.edge import EdgeContextException

__all__ = [
    # ======================# EDGE_CONTEXT_SERVICE EXCEPTION #======================#
    "EdgeContextServiceException",
]


# ======================# EDGE_CONTEXT_SERVICE EXCEPTION #======================#
class EdgeContextServiceException(EdgeContextException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an EdgeContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an EdgeContextService method.

    # PARENT:
        *   ServiceException
        *   EdgeContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "EdgeContextService raised an exception."