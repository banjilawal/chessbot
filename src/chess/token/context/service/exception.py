# src/chess/token/service/exception.py

"""
Module: chess.token.service.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import ServiceException
from chess.piece import PieceContextException

__all__ = [
    # ======================# PIECE_CONTEXT_SERVICE EXCEPTION #======================#
    "PieceContextServiceException",
]


# ======================# PIECE_CONTEXT_SERVICE EXCEPTION #======================#
class PieceContextServiceException(PieceContextException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

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
    ERROR_CODE = "PIECE_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TokenContextService raised an exception."