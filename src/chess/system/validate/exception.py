# src/chess/system/validate/exception.py

"""
Module: chess.system.validate.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# VALIDATION_FAILED EXCEPTION #======================#
    "ValidationFailedException",
]


#======================# VALIDATION_FAILED EXCEPTION #======================#
class ValidationFailedException(ChessException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining
  
    # RESPONSIBILITIES:
    1.  Parent of exception verifying correctness of candidate
    2.  Wraps an exception that hits the try-finally block of a Validator method.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VALIDATION_FAILED_ERROR"
    DEFAULT_MESSAGE = "Validation failed."
