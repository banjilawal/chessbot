# src/chess/system/builder/exception/exception.py

"""
Module: chess.system.builder.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# BUILDER EXCEPTION SUPER CLASS #======================#
    "BuilderException",
]


# ======================# BUILDER EXCEPTION SUPER CLASS #======================#
class BuilderException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Builder objects
    3.  Catchall for Builder failure states that are not covered by a lower level Builder exception.
  
    # PARENT
        *   ChessException
  
    # PROVIDES:
    BuilderException
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BUILDER_ERROR"
    DEFAULT_MESSAGE = "Builder raised an exception."
