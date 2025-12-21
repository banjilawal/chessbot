# src/chess/system/validate/exception/exception.py

"""
Module: chess.system.validate.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    #======================# VALIDATOR EXCEPTION #======================#
    "ValidatorException",

]


#======================# VALIDATOR EXCEPTION #======================#
class ValidatorException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exception raised by Validator objects
    2.  Catchall for Validator errors not coveredby lower level  Validator exception.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    ValidatorException
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VALIDATOR_ERROR"
    DEFAULT_MESSAGE = "Validator raised an exception."
