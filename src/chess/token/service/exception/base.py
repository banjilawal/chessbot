# src/chess/token/service/exception/exception.py

"""
Module: chess.token.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException
from chess.token import TokenException

__all__ = [
    # ======================# TOKEN_SERVICE EXCEPTION #======================#
    "TokenServiceException",
]


# ======================# TOKEN_SERVICE EXCEPTION #======================#
class TokenServiceException(TokenException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an TokenService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a TokenService method.

    # PARENT:
        *   ServiceException
        *   TokenException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TokenService raised an exception."