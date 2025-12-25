# src/chess/system/service/base/exception.py

"""
Module: chess.system.service.base.exception
Author: Banji Lawal
Created: 2025-11-18
"""

from chess.system import ExceptionWrapper

__all__ = [
    # ======================# SERVICE EXCEPTION #======================#
    "ServiceException",
]


# ======================# SERVICE EXCEPTION #======================#
class ServiceException(ExceptionWrapper):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Basic, Service Primitive

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