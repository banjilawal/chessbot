# src/chess/system/validate/exception/failure.py

"""
Module: chess.system.validate.exception.failure
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ValidatorException

__all__ = [
    # ======================# VALIDATION_FAILED EXCEPTION #======================#
    "ValidationFailedException",
]


#======================# VALIDATION_FAILED EXCEPTION #======================#
class ValidationFailedException(ValidatorException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exception verifying correctness of candidate
    2.  Wraps unhandled exception that hit the try-finally block of a Validator method.
  
    # PARENT:
        *   ValidatorException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VALIDATION_FAILED_ERROR"
    DEFAULT_MESSAGE = "Validation failed."
