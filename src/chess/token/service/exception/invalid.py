# src/chess/token/service/exception/invalid.py

"""
Module: chess.token.service.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.token import TokenServiceException


__all__ = [
    #======================# TOKEN_SERVICE VALIDATION EXCEPTION #======================#
    "InvalidTokenServiceException",
]

#======================# TOKEN_SERVICE VALIDATION EXCEPTION #======================#
class InvalidTokenServiceException(TokenServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during TokenService verification process.
    2.  Wrap an exception that hits the try-finally block of an TokenServiceValidator method.

    # PARENT:
        *   TokenServiceException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TokenService validation failed."