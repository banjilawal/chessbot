# src/chess/token/service/data/exception/exception.py

"""
Module: chess.token.service.data.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# TOKEN_DATA_SERVICE EXCEPTION #======================#
    "TokenDataServiceException",
]

from chess.token import TokenException
from chess.system import ServiceException


# ======================# TOKEN_DATA_SERVICE EXCEPTION #======================#
class TokenDataServiceException(TokenException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an TokenDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a TokenDataService method.

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
    ERROR_CODE = "TOKEN_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TokenDataService raised an exception."