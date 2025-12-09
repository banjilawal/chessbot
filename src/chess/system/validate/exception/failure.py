# src/chess/system/validate/exception/failure.py

"""
Module: chess.system.validate.exception.failure
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ValidatorException

__all__ = [
    #======================# ENTITY VALIDATION FAILURE EXCEPTION #======================#
    "ValidationFailedException",
]


#======================# ENTITY VALIDATION FAILURE EXCEPTION #======================#
class ValidationFailedException(ValidatorException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions verifying correctness of candidate
    2.  Wraps unhandled exceptions that hit the try-finally block of a Validator method.
  
    # PARENT
        *   ValidatorException
  
    # PROVIDES:
    ValidationFailedException
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FAILED_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Validation failed."
