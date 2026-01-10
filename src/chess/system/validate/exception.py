# src/chess/system/validate/exception.py

"""
Module: chess.system.validate.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ExceptionWrapper

__all__ = [
    # ======================# VALIDATION_FAILED EXCEPTION #======================#
    "ValidationFailedException",
]


#======================# VALIDATION_FAILED EXCEPTION #======================#
class ValidationFailedException(ExceptionWrapper):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining
  
    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a validation operation failed. The encapsulated exceptions create a chain
        for tracing the source of the failure.

    # PARENT:
        *   OperationFailedException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VALIDATION_FAILED_ERROR"
    DEFAULT_MESSAGE = "Validation failed."
