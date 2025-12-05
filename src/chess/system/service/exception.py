# src/chess/system/service/exception.py

"""
Module: chess.system.service.exception
Author: Banji Lawal
Created: 2025-11-19
"""

from chess.system import ChessException

__all__ = [
    "ServiceException",
]


# ======================# SERVICE EXCEPTIONS #======================#
class ServiceException(ChessException):
    """
    Super class of exceptions raised by Service objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SERVICE_ERROR"
    DEFAULT_MESSAGE = "Service raised an exception."