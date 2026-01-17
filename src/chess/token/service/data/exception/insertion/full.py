# src/chess/token/service/data/exception/insertion/full.py

"""
Module: chess.token.service.data.exception.insertion.full
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_SERVICE_CAPACITY EXCEPTION #======================#
    "TokenServiceCapacityException",
]

from chess.system import DebugException
from chess.token import TokenServiceException


# ======================# TOKEN_SERVICE_CAPACITY EXCEPTION #======================#
class TokenServiceCapacityException(TokenServiceException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a token to the service failed because the service has reached the limit of
        how many tokens it manages. 

    # PARENT:
        *   DebugException
        *   TokenServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_SERVICE_CAPACITY_ERROR"
    DEFAULT_MESSAGE = "Adding a token to the service failed: The number of tokens managed is at full capacity."