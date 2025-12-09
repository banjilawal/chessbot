# src/chess/system/context/exception.py

"""
Module: chess.system.context.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException, BoundsException

__all__ = [
    #======================# CONTEXT EXCEPTIONS #======================#
    "ContextException",
    "ContextFlagCountException",
]


#======================# CONTEXT EXCEPTIONS #======================#
class ContextException(ChessException):
    """
    # ROLE: Parent Exception
  
    # RESPONSIBILITIES:
    1.  Super class of exceptions when a condition halts the normal flow of a Context object's operations.
  
    # PROVIDES:
    ContextException
    
    None
    """
    ERROR_CODE = "CONTEXT_ERROR"
    DEFAULT_MESSAGE = "Context raised an exception."


class ContextFlagCountException(ContextException, BoundsException):
    """
    # ROLE: ContextException, BoundsException
  
    # RESPONSIBILITIES:
    1.  Raised when the number a Context instance has either no flags switched on or, too many.
  
    # PROVIDES:
    ContextException
  
    None
    """
    ERROR_CODE = "CONTEXT_FLAG_COUNT_ERROR"
    DEFAULT_MESSAGE = "The number of Context switches turned on is out of bounds."
