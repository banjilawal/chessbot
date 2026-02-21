# src/chess/system/validate/exception/wrapper.py

"""
Module: chess.system.validate.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import OperationFailedException

__all__ = [
    # ======================# VALIDATION_FAILURE EXCEPTION #======================#
    "ValidationException",
]


#======================# VALIDATION_FAILURE EXCEPTION #======================#
class ValidationException(OperationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining
  
    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a validation operation failed. The exception chain
        traces the ultimate source of failure.

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
