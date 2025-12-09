# src/chess/system/validate/exception/certification.py

"""
Module: chess.system.validate.exception.certification
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ValidatorException, NullException

__all__ = [
    #======================# UNRELIABLE_VALIDATOR_EXCEPTION #======================#
    "UnreliableValidatorException",
    #======================# NULL_VALIDATOR_EXCEPTION #======================#
    "NullValidatorException",
]


#======================# UNRELIABLE_VALIDATOR_EXCEPTION #======================#
class UnreliableValidatorException(ValidatorException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    Catchall for when Validator certification check hits the try-finally block with an unhandled exception.
    
    # PARENT
        *   ValidatorException
        *   ValidationFailedException
  
    # PROVIDES:
    UnreliableValidatorException
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VALIDATOR_CERTIFICATION_ERROR"
    DEFAULT_MESSAGE = "Validator certification failed. Do not rely on this validator."


#======================# NULL_VALIDATOR_EXCEPTION #======================#
class NullValidatorException(UnreliableValidatorException, NullException):
    """
    # ROLE: Error Tracing, Debugging
  
    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required aValidator but got null instead.
  
    # PARENT
        *   InvalidValidatorException
        *   NullException
  
    # PROVIDES:
    NullValidatorException
  
    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_VALIDATOR_ERROR"
    DEFAULT_MESSAGE = "Validator cannot be null."
