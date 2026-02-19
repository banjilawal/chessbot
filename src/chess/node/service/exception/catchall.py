# src/chess/node/service/exception/catchall.py

"""
Module: chess.node.service.exception.catchall
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.node import NodeException
from chess.system import ServiceException


__all__ = [
    # ======================# NODE_SERVICE EXCEPTION #======================#
    "NodeServiceException",
]


# ======================# NODE_SERVICE EXCEPTION #======================#
class NodeServiceException(NodeException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an NodeService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a NodeService method.

    # PARENT:
        *   NodeException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "NodeService raised an exception."