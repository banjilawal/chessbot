# src/chess/system/build/exception/exception.py

"""
Module: chess.system.build.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# BUILD EXCEPTION #======================#
    "BuildException",
]


# ======================# BUILD EXCEPTION #======================#
class BuildException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exception raised by Build operations and BUilders.
    3.  Catchall for Builder errors not covered by lower level  Builder exception.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BUILD_ERROR"
    DEFAULT_MESSAGE = "A build related exception was raised exception."
