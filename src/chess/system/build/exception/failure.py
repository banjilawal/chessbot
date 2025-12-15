# src/chess/system/builder/exception/failure.py

"""
Module: chess.system.builder.exception.failure
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuilderException, OperationFailedException

__all__ = [
    #======================# FAILED ENTITY BUILD OPERATION EXCEPTION #======================#
    "BuildFailedException",
]


#======================# FAILED ENTITY BUILD OPERATION EXCEPTION #======================#
class BuildFailedException(BuilderException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions when an entity building process fails.
    2.  Wraps unhandled exceptions that hit the try-finally block of a Builder method.
  
    # PARENT:
        *   BuilderException
        *   OperationFailedException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "build failed."
