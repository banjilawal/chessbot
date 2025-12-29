# src/chess/token/service/exception/invalid.py

"""
Module: chess.token.service.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceOperationFailedException
from chess.token import TokenServiceException

__all__ = [
    # ======================# TOKEN_SERVICE_OPERATION EXCEPTION #======================#
    "TokenServiceOperationFailedException",
]


# ======================# TOKEN_SERVICE_OPERATION EXCEPTION #======================#
class TokenServiceOperationFailedException(TokenServiceException, ServiceOperationFailedException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate That  a TokenService's method caught an unhandled exception in its try-catch-finally block.

    # PARENT:
        *   TokenServiceException
        *   ServiceOperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_SERVICE_OPERATION_ERROR"
    DEFAULT_MESSAGE = "TokenService operation failed."