# src/chess/square/context/service/exception/super.py

"""
Module: chess.square.context.service.exception.super
Author: Banji Lawal
Created: 2025-02-23
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    # ======================# SQUARE_CONTEXT_SERVICE EXCEPTION #======================#
    "SquareContextServiceException",
]


# ======================# SQUARE_CONTEXT_SERVICE EXCEPTION #======================#
class SquareContextServiceException(ServiceException):
    """
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a failure occurred in SquareContextService.
    2.  The method where the error occurred is identified in the exception nested directly underneath.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_CONTEXT_SERVICE_EXCEPTION"
    MSG = "SquareContextService raised an exception."