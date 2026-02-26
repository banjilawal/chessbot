# src/chess/square/service/exception/super.py

"""
Module: chess.square.service.exception.super
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""


from chess.system import ServiceException

__all__ = [
    # ======================# SQUARE_SERVICE EXCEPTION #======================#
    "SquareServiceException",
]


# ======================# SQUARE_SERVICE EXCEPTION #======================#
class SquareServiceException(ServiceException):
    """
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a failure occurred in SquareService.
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
    ERR_CODE = "SQUARE_SERVICE_ERROR"
    MSG = "SquareService raised an exception."