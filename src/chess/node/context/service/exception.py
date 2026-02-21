# src/chess/node/context/service/exception.py

"""
Module: chess.node.context.service.exception
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import ServiceException
from chess.node import NodeContextException

__all__ = [
    # ======================# NODE_CONTEXT_SERVICE EXCEPTION #======================#
    "NodeContextServiceException",
]


# ======================# NODE_CONTEXT_SERVICE EXCEPTION #======================#
class NodeContextServiceException(NodeContextException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an NodeContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an NodeContextService method.

    # PARENT:
        *   ServiceException
        *   NodeContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "NodeContextService raised an exception."