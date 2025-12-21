# src/chess/system/service/exception/base.py

"""
Module: chess.system.service.exception.base
Author: Banji Lawal
Created: 2025-11-18
"""

from chess.system import ChessException

__all__ = [
    # ======================# SERVICE EXCEPTION #======================#
    "ServiceException",
]


# ======================# SERVICE EXCEPTION #======================#
class ServiceException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by Service objects
    3.  Catchall for Service errors not covered by lower level Service exception.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SERVICE_ERROR"
    DEFAULT_MESSAGE = "Service raised an exception."