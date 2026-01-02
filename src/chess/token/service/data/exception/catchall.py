# src/chess/token/service/data/exception/catchall.py

"""
Module: chess.token.service.data.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenException
from chess.system import DataServiceException


__all__ = [
    # ======================# TOKEN_DATA_SERVICE EXCEPTION #======================#
    "TokenDataServiceException",
]

# ======================# TOKEN_DATA_SERVICE EXCEPTION #======================#
class TokenDataServiceException(TokenException, DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by TokenDataService methods that return Result objects.

    # PARENT:
        *   TokenException
        *   DataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TokenDataService raised an exception."