# src/chess/token/service/exception/null.py

"""
Module: chess.token.service.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.token import InvalidTokenServiceException


__all__ = [
    "NullTokenServiceException",
]


#======================# NULL TOKEN_SERVICE EXCEPTION #======================#
class NullTokenServiceException(InvalidTokenServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an TokenService but got null instead.

    # PARENT:
        *   InvalidTokenServiceException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TOKEN_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TokenService cannot be null."
