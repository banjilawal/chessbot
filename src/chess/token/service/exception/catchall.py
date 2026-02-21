# src/chess/token/service/exception.catchall.py

"""
Module: chess.token.service.exception.catchall
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.token import TokenException
from chess.system import ServiceException

__all__ = [
    # ======================# TOKEN_SERVICE EXCEPTION #======================#
    "TokenServiceException",
]


# ======================# TOKEN_SERVICE EXCEPTION #======================#
class TokenServiceException(TokenException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by TokenService methods that return Result objects.

    # PARENT:
        *   TokenException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TokenService raised an exception."