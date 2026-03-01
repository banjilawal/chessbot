# src/logic/token/service/exception.py

"""
Module: logic.token.service.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from logic.system import ServiceException
from logic.piece import PieceContextException

__all__ = [
    # ======================# PIECE_CONTEXT_SERVICE EXCEPTION #======================#
    "PieceContextServiceException",
]


# ======================# PIECE_CONTEXT_SERVICE EXCEPTION #======================#
class PieceContextServiceException(PieceContextException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an TokenContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an TokenContextService method.

    # PARENT:
        *   ServiceException
        *   TokenContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PIECE_CONTEXT_SERVICE_EXCEPTION"
    MSG = "TokenContextService raised an exception."