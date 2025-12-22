# src/chess/system/build/builder/exception.py

"""
Module: chess.system.build.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# BUILDER EXCEPTION #======================#
    "BuilderException",
]


# ======================# BUILDER EXCEPTION #======================#
class BuilderException(BuildException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exception raised by Builder objects.
    3.  Catchall for errors not covered by Builder subclasses.
  
    # PARENT:
        *   BuildException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BUILDER_ERROR"
    DEFAULT_MESSAGE = "Builder raised an exception."
